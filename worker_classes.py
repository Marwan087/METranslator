# METranslator - A powerful game translation tool using AI models.
# Copyright (C) 2026 METranslator Developer.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import time
import threading
import subprocess
import requests
import json
from PySide6.QtCore import QThread, Signal, QObject
import shutil
import urllib.request
import urllib.error
from translations import TRANSLATIONS

def tr_static(lang, key):
    """دالة ترجمة ثابتة لاستخدامها داخل كلاسات العمال"""
    try:
        return TRANSLATIONS.get(lang, TRANSLATIONS['ar']).get(key, key)
    except:
        return key

def run_worker_task(exe_dir, task_name, args, output_callback, progress_callback, check_stop=None, worker_instance=None, lang='ar'):
    """دالة مساعدة لتشغيل مهام worker_tasks.py"""
    python_exe = os.path.join(exe_dir, 'venv', 'Scripts', 'python.exe')
    if not os.path.exists(python_exe):
        python_exe = sys.executable  # Fallback
    script_path = os.path.join(exe_dir, 'worker_tasks.py')
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    cmd = [python_exe, "-u", script_path, task_name] + args # -u for unbuffered
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
            bufsize=1,
            universal_newlines=True,
            encoding='utf-8',
            errors='replace'
        )
        if worker_instance:
            worker_instance.process = process
        for line in iter(process.stdout.readline, ''):
            if check_stop and check_stop():
                process.terminate()
                return False
            line = line.strip()
            if not line: continue
            try:
                if line.startswith('{') and line.endswith('}'):
                    data = json.loads(line)
                    msg_type = data.get("type")
                    if msg_type == "message":
                        output_callback(data.get("content", ""))
                    elif msg_type == "progress":
                        progress_callback(data.get("value", 0))
                    elif msg_type == "result":
                        process.wait()
                        return data.get("success", False)
                else:
                    output_callback(line)
            except:
                output_callback(line)
        process.wait()
        if process.returncode != 0:
            output_callback(f"{tr_static(lang, 'error')}: {process.returncode}")
            return False
        return True
    except Exception as e:
        output_callback(f"{tr_static(lang, 'error')}: {str(e)}")
        return False

class ModelDownloadWorker(QObject):
    """عامل لتحميل النموذج"""
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)

    def __init__(self, exe_dir, model_id=None, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.model_id = model_id or 'Helsinki-NLP/opus-mt-tc-big-en-ar'
        self.lang = lang
        self.should_run = True

    def run(self):
        try:
            self._download_logic()
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
        finally:
            self.finished.emit()

    def _get_remote_size(self, url, timeout=15):
        try:
            resp = requests.head(url, allow_redirects=True, timeout=timeout)
            if resp.status_code == 200:
                cl = resp.headers.get('Content-Length')
                if cl and cl.isdigit(): return int(cl)
        except: pass
        try:
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                cl = resp.getheader('Content-Length')
                if cl and cl.isdigit(): return int(cl)
        except: pass
        return None

    def _download_file(self, url, dest_path, progress_cb=None, size_discovered_cb=None):
        existing = 0
        try:
            if os.path.exists(dest_path): existing = os.path.getsize(dest_path)
        except: pass
        headers = {}
        mode = 'wb'
        if existing > 0:
            headers['Range'] = f'bytes={existing}-'
            mode = 'ab'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                cl = resp.getheader('Content-Length')
                if cl and cl.isdigit() and size_discovered_cb:
                    size_discovered_cb(int(cl))
                with open(dest_path, mode) as out_f:
                    while True:
                        if not self.should_run: return False
                        chunk = resp.read(16*1024)
                        if not chunk: break
                        out_f.write(chunk)
                        if progress_cb: progress_cb(len(chunk))
            return True
        except urllib.error.HTTPError as he:
            if he.code in (416, 403, 401): 
                 if he.code == 416: return True 
                 self.output.emit(f"خطأ HTTP {he.code} عند تنزيل {os.path.basename(dest_path)}")
                 return False
            try:
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)
                with open(dest_path, 'wb') as out_f:
                    with urllib.request.urlopen(url, timeout=30) as resp:
                         while True:
                            if not self.should_run: return False
                            chunk = resp.read(16*1024)
                            if not chunk: break
                            out_f.write(chunk)
                            if progress_cb: progress_cb(len(chunk))
                return True
            except Exception as e:
                self.output.emit(f"{tr_static(self.lang, 'error')} {os.path.basename(dest_path)}: {str(e)}")
                return False
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')} {os.path.basename(dest_path)}: {str(e)}")
            return False

    def _download_logic(self):
        folder_name = os.path.basename(self.model_id)
        model_path = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", folder_name)
        os.makedirs(model_path, exist_ok=True)
        mt_file = os.path.join(model_path, "model.safetensors")
        if (os.path.exists(mt_file) and os.path.getsize(mt_file) > 10*1024*1024):
            self.output.emit(tr_static(self.lang, 'wait') + "...")
            self.progress.emit(0)
            abs_model_path = str(os.path.abspath(model_path))
            success = run_worker_task(
                self.exe_dir, 
                "verify_download", 
                ["--src", abs_model_path, "--lang", self.lang], 
                self.output.emit, 
                self.progress.emit,
                lambda: not self.should_run,
                worker_instance=self
            )
            if success:
                return
            else:
                self.output.emit(tr_static(self.lang, 'wait') + "...")
        self.output.emit(tr_static(self.lang, 'downloading_model_msg') + "...")
        candidate_files = [
                "config.json",
                "generation_config.json",
                "special_tokens_map.json",
                "source.spm",
                "target.spm",
                "tokenizer_config.json",
                "vocab.json",
                "model.safetensors",
            ]
        base_url = f'https://huggingface.co/{self.model_id}/resolve/main'
        total_size = 0
        files_map = []
        for fname in candidate_files:
            url = f"{base_url}/{fname}"
            size = self._get_remote_size(url)
            if size:
                files_map.append((fname, url, size))
                total_size += size
            else:
                if fname in ['config.json', 'model.safetensors']:
                    self.output.emit(f"تحذير: لم يتم العثور على حجم الملف {fname} عن بعد.")
        if not files_map:
            self.output.emit("خطأ: لم يتم العثور على أي ملفات للتحميل. يرجى التحقق من الاتصال أو معرف النموذج.")
            return
        downloaded = 0
        for fname_m, url_m, size_m in files_map:
            dest_m = os.path.join(model_path, fname_m)
            if os.path.exists(dest_m):
                downloaded += os.path.getsize(dest_m)
        if total_size: self.progress.emit(int(downloaded * 100 / total_size))
        def _on_chunk(n):
            nonlocal downloaded
            downloaded += n
            if total_size: self.progress.emit(int(downloaded * 100 / total_size))
        success_count = 0
        for fname, url, size in files_map:
            if not self.should_run: break
            self.output.emit(f"تنزيل {fname}...")
            dest = os.path.join(model_path, fname)
            if self._download_file(url, dest, _on_chunk):
                success_count += 1
        if self.should_run:
            if success_count == 0:
                self.output.emit(tr_static(self.lang, 'download_failed'))
                return
            self.output.emit(tr_static(self.lang, 'wait') + "...")
            abs_model_path = str(os.path.abspath(model_path))
            run_worker_task(
                self.exe_dir, "verify_download", ["--src", abs_model_path, "--lang", self.lang], 
                self.output.emit, self.progress.emit
            )
    def stop_process(self):
        self.should_run = False

class Madlad400DownloadWorker(QObject):
    """عامل لتحميل نموذج MADLAD400"""
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    def __init__(self, exe_dir, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.lang = lang
        self.should_run = True
        self.model_id = 'SoybeanMilk/madlad400-3b-mt-ct2-int8_float16'
    def run(self):
        try:
            self._download_logic()
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
        finally:
            self.finished.emit()
    
    def _get_remote_size(self, url, timeout=15):
        try:
            resp = requests.head(url, allow_redirects=True, timeout=timeout)
            if resp.status_code == 200:
                cl = resp.headers.get('Content-Length')
                if cl and cl.isdigit(): return int(cl)
        except: pass
        try:
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                cl = resp.getheader('Content-Length')
                if cl and cl.isdigit(): return int(cl)
        except: pass
        return None
    
    def _download_file(self, url, dest_path, progress_cb=None, size_discovered_cb=None):
        existing = 0
        try:
            if os.path.exists(dest_path): existing = os.path.getsize(dest_path)
        except: pass
        headers = {}
        mode = 'wb'
        if existing > 0:
            headers['Range'] = f'bytes={existing}-'
            mode = 'ab'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                cl = resp.getheader('Content-Length')
                if cl and cl.isdigit() and size_discovered_cb:
                    size_discovered_cb(int(cl))
                with open(dest_path, mode) as out_f:
                    while True:
                        if not self.should_run: return False
                        chunk = resp.read(16*1024)
                        if not chunk: break
                        out_f.write(chunk)
                        if progress_cb: progress_cb(len(chunk))
            return True
        except urllib.error.HTTPError as he:
            if he.code in (416, 403, 401): 
                 if he.code == 416: return True 
                 self.output.emit(f"خطأ HTTP {he.code} عند تنزيل {os.path.basename(dest_path)}")
                 return False
            try:
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)
                with open(dest_path, 'wb') as out_f:
                    with urllib.request.urlopen(url, timeout=30) as resp:
                         while True:
                            if not self.should_run: return False
                            chunk = resp.read(16*1024)
                            if not chunk: break
                            out_f.write(chunk)
                            if progress_cb: progress_cb(len(chunk))
                return True
            except: return False
        except: return False
    
    def _download_logic(self):
        model_path = os.path.join(self.exe_dir, "models", "multilingual", "madlad400")
        os.makedirs(model_path, exist_ok=True)
        model_file = os.path.join(model_path, "model.bin")
        if os.path.exists(model_file) and os.path.getsize(model_file) > 100*1024*1024:
            self.output.emit(tr_static(self.lang, 'wait') + "...")
            self.progress.emit(0)
            success = run_worker_task(
                self.exe_dir, 
                "verify_madlad400_download", 
                ["--src", model_path, "--lang", self.lang], 
                self.output.emit, 
                self.progress.emit,
                lambda: not self.should_run,
                worker_instance=self
            )
            if success:
                return
            else:
                self.output.emit("التحقق فشل. جاري محاولة استكمال التحميل...")
        self.output.emit(tr_static(self.lang, 'downloading_madlad400_model') + "...")
        candidate_files =  [
                "added_tokens.json",
                "config.json",
                "generation_config.json",
                "shared_vocabulary.json",
                "tokenizer.json",
                "spiece.model",
                "tokenizer_config.json",
                "special_tokens_map.json",
                "model.bin",
            ]
        base_url = f'https://huggingface.co/{self.model_id}/resolve/main'
        total_size = 0
        files_map = []
        for fname in candidate_files:
            url = f"{base_url}/{fname}"
            size = self._get_remote_size(url)
            if size:
                files_map.append((fname, url, size))
                total_size += size
            else:
                files_map.append((fname, url, None))
        downloaded = 0
        for fname_m, url_m, size_m in files_map:
            dest_m = os.path.join(model_path, fname_m)
            if os.path.exists(dest_m):
                downloaded += os.path.getsize(dest_m)
        if total_size: self.progress.emit(int(downloaded * 100 / total_size))
        def _on_chunk(n):
            nonlocal downloaded
            downloaded += n
            if total_size: self.progress.emit(int(downloaded * 100 / total_size))
        success_count = 0
        for fname, url, size in files_map:
            if not self.should_run: break
            self.output.emit(f"تنزيل {fname}...")
            dest = os.path.join(model_path, fname)
            if self._download_file(url, dest, _on_chunk):
                success_count += 1
            else:
                if fname in ["model.bin", "config.json"]:
                    self.output.emit(f"{tr_static(self.lang, 'error')}: {fname}")
                    return
        if self.should_run:
            self.output.emit("تم تحميل الملفات. جاري التحقق...")
            run_worker_task(
                self.exe_dir, "verify_madlad400_download", ["--src", model_path, "--lang", self.lang], 
                self.output.emit, self.progress.emit
            )
    def stop_process(self):
        self.should_run = False

class MBARTLARGE50DownloadWorker(QObject):
    """عامل لتحميل نموذج MBARTLARGE50"""
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    
    def __init__(self, exe_dir, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.lang = lang
        self.should_run = True
        self.model_id = 'facebook/mbart-large-50-many-to-many-mmt'
    
    def run(self):
        try:
            self._download_logic()
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
        finally:
            self.finished.emit()
    
    def _get_remote_size(self, url, timeout=15):
        try:
            resp = requests.head(url, allow_redirects=True, timeout=timeout)
            if resp.status_code == 200:
                cl = resp.headers.get('Content-Length')
                if cl and cl.isdigit(): return int(cl)
        except: pass
        try:
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                cl = resp.getheader('Content-Length')
                if cl and cl.isdigit(): return int(cl)
        except: pass
        return None
    
    def _download_file(self, url, dest_path, progress_cb=None, size_discovered_cb=None):
        existing = 0
        try:
            if os.path.exists(dest_path): existing = os.path.getsize(dest_path)
        except: pass
        headers = {}
        mode = 'wb'
        if existing > 0:
            headers['Range'] = f'bytes={existing}-'
            mode = 'ab'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                cl = resp.getheader('Content-Length')
                if cl and cl.isdigit() and size_discovered_cb:
                    size_discovered_cb(int(cl))
                with open(dest_path, mode) as out_f:
                    while True:
                        if not self.should_run: return False
                        chunk = resp.read(16*1024)
                        if not chunk: break
                        out_f.write(chunk)
                        if progress_cb: progress_cb(len(chunk))
            return True
        except urllib.error.HTTPError as he:
            if he.code in (416, 403, 401): 
                 if he.code == 416: return True 
                 self.output.emit(f"خطأ HTTP {he.code} عند تنزيل {os.path.basename(dest_path)}")
                 return False
            try:
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)
                with open(dest_path, 'wb') as out_f:
                    with urllib.request.urlopen(url, timeout=30) as resp:
                         while True:
                            if not self.should_run: return False
                            chunk = resp.read(16*1024)
                            if not chunk: break
                            out_f.write(chunk)
                            if progress_cb: progress_cb(len(chunk))
                return True
            except: return False
        except: return False
    
    def _download_logic(self):
        model_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50")
        os.makedirs(model_path, exist_ok=True)
        model_file = os.path.join(model_path, "model.safetensors")
        if os.path.exists(model_file) and os.path.getsize(model_file) > 100*1024*1024:
            self.output.emit(tr_static(self.lang, 'wait') + "...")
            self.progress.emit(0)
            success = run_worker_task(
                self.exe_dir, 
                "verify_mbartlarge50_download", 
                ["--src", model_path, "--lang", self.lang], 
                self.output.emit, 
                self.progress.emit,
                lambda: not self.should_run,
                worker_instance=self
            )
            if success:
                return
            else:
                self.output.emit("التحقق فشل. جاري محاولة استكمال التحميل...")
        self.output.emit(tr_static(self.lang, 'downloading_mbartlarge50_model') + "...")
        candidate_files = [
                "config.json",
                "generation_config.json",
                "sentencepiece.bpe.model",
                "tokenizer_config.json",
                "special_tokens_map.json",
                "model.safetensors",
            ]
        base_url = f'https://huggingface.co/{self.model_id}/resolve/main'
        total_size = 0
        files_map = []
        for fname in candidate_files:
            url = f"{base_url}/{fname}"
            size = self._get_remote_size(url)
            files_map.append((fname, url, size))
            if size: total_size += size
        downloaded = 0
        for fname_m, url_m, size_m in files_map:
            dest_m = os.path.join(model_path, fname_m)
            if os.path.exists(dest_m):
                downloaded += os.path.getsize(dest_m)
        if total_size: self.progress.emit(int(downloaded * 100 / total_size))
        def _on_chunk(n):
            nonlocal downloaded
            downloaded += n
            if total_size: self.progress.emit(int(downloaded * 100 / total_size))
        success_count = 0
        for fname, url, size in files_map:
            if not self.should_run: break
            self.output.emit(f"تنزيل {fname}...")
            dest = os.path.join(model_path, fname)
            if self._download_file(url, dest, _on_chunk):
                success_count += 1
            else:
                if fname in ["model.safetensors", "config.json"]:
                    self.output.emit(f"{tr_static(self.lang, 'error')}: {fname}")
                    return
        if self.should_run:
            self.output.emit("تم تحميل الملفات. جاري التحقق...")
            run_worker_task(
                self.exe_dir, "verify_mbartlarge50_download", ["--src", model_path, "--lang", self.lang], 
                self.output.emit, self.progress.emit
            )
    def stop_process(self):
        self.should_run = False

class ConvertToOPUSC2Worker(QObject):
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    def __init__(self, exe_dir, conversion_type, src_model=None, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.conversion_type = conversion_type
        self.src_model = src_model
        self.lang = lang
        self.should_run = True
        
    def run(self):
        src_model = self.src_model or os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", "opus-mt-tc-big-en-ar")
        basename = os.path.basename(src_model)
        parts = basename.split('-')
        pair = '-'.join(parts[-2:]) if len(parts) >= 2 else basename
        dst_root = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", "CTranslate2", f"{pair}-CTranslate2")
        dst_model = os.path.join(dst_root, f"{self.conversion_type}")
        quantization_mapping = {
            "Ct2-int8": "int8", "Ct2-int8_float16": "int8_float16", "Ct2-float16": "float16", "Ct2-bfloat16": "bfloat16"
        }
        q = quantization_mapping.get(self.conversion_type, "int8")
        run_worker_task(
            self.exe_dir, "convert_opus_c2",
            ["--src", src_model, "--lang", self.lang, "--dst", dst_model, "--quantization", q],
            self.output.emit, self.progress.emit, lambda: not self.should_run,
            worker_instance=self, lang=self.lang
        )
        self.finished.emit()
    def stop_process(self): self.should_run = False

class ConvertToMBARTLARGE50C2Worker(QObject):
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    def __init__(self, exe_dir, conversion_type, src_model=None, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.conversion_type = conversion_type
        self.lang = lang
        self.should_run = True

    def run(self):
        src_model = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50")
        dst_model = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50", "CTranslate2", f"{self.conversion_type}")
        quantization_mapping = {
            "Ct2-int8": "int8", "Ct2-int8_float16": "int8_float16", "Ct2-float16": "float16", "Ct2-bfloat16": "bfloat16"
        }
        q = quantization_mapping.get(self.conversion_type, "int8")
        run_worker_task(
            self.exe_dir, "convert_mbart_c2",
            ["--src", src_model, "--lang", self.lang, "--dst", dst_model, "--quantization", q],
            self.output.emit, self.progress.emit, lambda: not self.should_run,
            worker_instance=self, lang=self.lang
        )
        self.finished.emit()
    def stop_process(self): self.should_run = False

class ConvertToMBARTLARGE50ONNXWorker(QObject):
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    def __init__(self, exe_dir, conversion_type, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.conversion_type = conversion_type
        self.lang = lang
        self.should_run = True
        
    def run(self):
        model_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50")
        quantization = None
        if self.conversion_type == "Onnx":
             onnx_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50", "Onnx", "Onnx")
        elif self.conversion_type == "Ox-int8":
             onnx_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50", "Onnx", "Onnx-int8")
             quantization = "int8"
        elif self.conversion_type == "Ox-float16":
             onnx_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50", "Onnx", "Onnx-float16")
             quantization = "float16" 
        args = ["--src", model_path, "--lang", self.lang, "--dst", onnx_path]
        if quantization:
            args.extend(["--quantization", quantization])
        run_worker_task(
             self.exe_dir, "convert_mbart_onnx", args,
             self.output.emit, self.progress.emit, lambda: not self.should_run,
             worker_instance=self, lang=self.lang
        )
        self.finished.emit()
    def stop_process(self): self.should_run = False

class ConvertToONNXWorker(QObject):
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    def __init__(self, exe_dir, conversion_type, src_model=None, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.conversion_type = conversion_type
        self.src_model = src_model
        self.lang = lang
        self.should_run = True
    def run(self):
        model_path = self.src_model or os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", "opus-mt-tc-big-en-ar")
        basename = os.path.basename(model_path)
        parts = basename.split('-')
        pair = '-'.join(parts[-2:]) if len(parts) >= 2 else basename
        base_out = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", "Onnx", f"{pair}-Onnx")
        quantization = None
        if self.conversion_type == "Onnx":
             onnx_path = os.path.join(base_out, "Onnx")
        elif self.conversion_type == "Ox-int8":
             onnx_path = os.path.join(base_out, "Ox-int8")
             quantization = "int8"
        elif self.conversion_type == "Ox-float16":
             onnx_path = os.path.join(base_out, "Ox-float16")
             quantization = "fp16"
        else:
            self.output.emit(tr_static(self.lang, 'error'))
            self.finished.emit()
            return
        args = ["--src", model_path, "--lang", self.lang, "--dst", onnx_path]
        if quantization:
             args.extend(["--quantization", quantization])
        run_worker_task(
            self.exe_dir, "convert_opus_onnx", args,
            self.output.emit, self.progress.emit, lambda: not self.should_run,
            worker_instance=self, lang=self.lang
        )
        self.finished.emit()
    def stop_process(self): self.should_run = False
