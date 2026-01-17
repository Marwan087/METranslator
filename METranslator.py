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
app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)
import subprocess
import threading
import requests
import json
import re
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                                QLabel, QLineEdit, QPushButton, QTextEdit, QTextBrowser, QRadioButton, QSlider,
                                QGroupBox, QCheckBox, QFileDialog, QMessageBox, QComboBox, QFrame,
                                QSplitter, QStatusBar, QDialog, QButtonGroup, QProgressBar)
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Qt, QProcess, QThread, Signal, QObject, QTimer, QMetaObject, QSize
from PySide6.QtGui import QFont, QTextCursor, QTextCharFormat, QIcon
import glob
import shutil
import codecs
import ctypes
from translations import TRANSLATIONS
import tempfile
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
def tr_static(lang, key):
    """دالة ترجمة ثابتة لاستخدامها خارج كلاس MainWindow"""
    try:
        return TRANSLATIONS.get(lang, TRANSLATIONS['ar']).get(key, key)
    except:
        return key
from worker_classes import ModelDownloadWorker, ConvertToOPUSC2Worker, ConvertToONNXWorker, Madlad400DownloadWorker, MBARTLARGE50DownloadWorker, ConvertToMBARTLARGE50C2Worker, ConvertToMBARTLARGE50ONNXWorker, run_worker_task
from server_worker_direct import ServerWorkerDirect

class LibraryVerificationWorker(QObject):
    """عامل للتحقق من المكتبات في الخلفية"""
    finished = Signal()
    output = Signal(str)
    success = Signal(bool)

    def __init__(self, exe_dir, backend, device, lang='ar'):
        super().__init__()
        self.exe_dir = exe_dir
        self.backend = backend
        self.device = device
        self.lang = lang

    def run(self):
        """تشغيل التحقق من البيئة والمكتبات"""
        try:
            # التحقق من وجود البيئة أولاً
            venv_path = os.path.join(self.exe_dir, 'venv')
            if not os.path.exists(venv_path):
                self.output.emit(tr_static(self.lang, 'error') + ": " + tr_static(self.lang, 'settings_file_not_found')) # Reusing settings_file_not_found or similar
                # Better: add a proper key
                self.output.emit('error_verifying_libraries' + ": venv not found") 
                self.finished.emit(False)
                return
            self.output.emit(tr_static(self.lang, 'wait') + "...")
            success = run_worker_task(
                self.exe_dir,
                "verify",
                ["--device", self.device, "--lang", self.lang],
                self.output.emit,
                lambda x: None, # لا نحتاج لشريط تقدم هنا
                check_stop=None,
                worker_instance=self
            )
            if success:
                self.success.emit(True)
            else:
                self.success.emit(False)
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error_verifying_libraries')}: {str(e)}")
            self.success.emit(False)
        finally:
            self.finished.emit()
if sys.platform == 'win32':
    try:
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except (AttributeError, BrokenPipeError):
        pass

def get_application_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def _sanitize(s: str) -> str:
    if not s:
        return s
    return ''.join(ch for ch in s if ch.isprintable()).strip()
def is_port_in_use(host, port):
    """التحقق إذا كان المنفذ مستخدماً"""
    import socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            return result == 0
    except:
        return False

class Worker(QObject):
    """عامل لمعالجة العمليات في الخلفية"""
    finished = Signal()
    output = Signal(str)
    def __init__(self, cmd, env=None, lang='ar'):
        super().__init__()
        self.cmd = cmd
        self.env = env or {}
        self.lang = lang
        self.process = None
    def run(self):
        try:
            self.process = subprocess.Popen(
                self.cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                env=self.env,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
                shell=False
            )
            for line in iter(self.process.stdout.readline, ''):
                self.output.emit(line.strip())
            self.process.stdout.close()
            return_code = self.process.wait()
            self.output.emit(tr_static(self.lang, 'server_stopped_successfully'))
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
        finally:
            self.finished.emit()

    def stop_process(self):
        """إيقاف العملية الخارجية"""
        if hasattr(self, 'process') and self.process:
            try:
                self.process.terminate()
                import time
                time.sleep(0.2)
                if self.process.poll() is None:  # إذا لم تنته العملية
                    self.process.kill()  # إنهاء قسري
            except:
                pass

class SetupWorker(QObject):
    """عامل لإعداد البيئة المحمولة"""
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)  # إشارة لعرض التقدم
    request_cleanup = Signal() # إشارة لطلب تنظيف العمليات
    def __init__(self, requirements_type, install_python, create_venv, recreate_venv, install_reqs, exe_dir, lang='ar'):
        super().__init__()
        self.requirements_type = requirements_type
        self.install_python = install_python
        self.create_venv = create_venv
        self.recreate_venv = recreate_venv
        self.install_reqs = install_reqs
        self.exe_dir = exe_dir
        self.lang = lang
        self.should_run = True
        self.process = None

    def run(self):
        """تشغيل عملية الإعداد"""
        try:
            if not self.should_run:
                return
            total_steps = sum([self.install_python, self.create_venv or self.recreate_venv, self.install_reqs])
            current_step = 0
            if self.install_python:
                self.output.emit(tr_static(self.lang, 'install_python_local') + "...")
                self.progress.emit(int((current_step / total_steps) * 100))
                if not self._install_python():
                    self.output.emit(tr_static(self.lang, 'error'))
                    return
                current_step += 1
                self.progress.emit(int((current_step / total_steps) * 100))
                if not self.should_run:
                    return
            if self.create_venv or self.recreate_venv:
                if self.recreate_venv:
                    self.output.emit(tr_static(self.lang, 'wait') + "...")
                    self.request_cleanup.emit()
                    time.sleep(2)
                    self.output.emit(tr_static(self.lang, 'recreate_virtual_environment') + "...")
                    self.progress.emit(int((current_step / total_steps) * 100))
                    if not self._delete_venv():
                        self.output.emit(tr_static(self.lang, 'error'))
                        return
                    if not self.should_run:
                        return
                self.output.emit(tr_static(self.lang, 'create_virtual_environment') + "...")
                self.progress.emit(int((current_step / total_steps) * 100))
                if not self._create_venv():
                    self.output.emit(tr_static(self.lang, 'error'))
                    return
                current_step += 1
                self.progress.emit(int((current_step / total_steps) * 100))
                if not self.should_run:
                    return
            if self.install_reqs:
                self.output.emit(tr_static(self.lang, 'install_requirements') + "...")
                self.progress.emit(int((current_step / total_steps) * 100))
                if not self._install_requirements():
                    self.output.emit(tr_static(self.lang, 'error'))
                    return
                current_step += 1
                self.progress.emit(int((current_step / total_steps) * 100))
            if self.should_run:
                self.output.emit(tr_static(self.lang, 'environment_setup_finished'))
                self.progress.emit(100)
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
        finally:
            self.finished.emit()

    def _install_python(self):
        """تثبيت بايثون محلي"""
        return True

    def _delete_venv(self):
        """حذف البيئة الافتراضية"""
        try:
            import shutil
            import os
            import time
            import sys
            import stat
            venv_dir = os.path.join(self.exe_dir, 'venv')
            try:
                abs_venv = os.path.abspath(venv_dir).lower()
                abs_prefix = os.path.abspath(sys.prefix).lower()
                abs_exec = os.path.abspath(sys.executable).lower()
                
                if abs_venv in abs_prefix or abs_venv in abs_exec:
                     self.output.emit(tr_static(self.lang, 'fatal_error_venv_active'))
                     return False
            except Exception as e:
                print(f"Error checking paths: {e}")
            if not os.path.exists(venv_dir):
                return True
            self.output.emit(tr_static(self.lang, 'wait') + "...")
            failed_errors = []
            def on_rm_error(func, path, exc_info):
                try:
                    os.chmod(path, stat.S_IWRITE)
                    func(path)
                except Exception as e:
                    failed_errors.append(f"{os.path.basename(path)} ({str(e)})")
            shutil.rmtree(venv_dir, onerror=on_rm_error)
            if os.path.exists(venv_dir):
                time.sleep(1)
                failed_errors = []
                shutil.rmtree(venv_dir, onerror=on_rm_error)
            if os.path.exists(venv_dir):
                self.output.emit(tr_static(self.lang, 'error'))
                return False
            self.output.emit(tr_static(self.lang, 'environment_setup_finished'))
            return True
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error_deleting_venv')}: {str(e)}")
            return False

    def _clean_sys_path(self):
        """تنظيف sys.path من مسارات venv"""
        try:
            venv_path = os.path.join(self.exe_dir, 'venv').lower()
            new_path = [p for p in sys.path if venv_path not in p.lower()]
            sys.path[:] = new_path
        except:
            pass

    def _create_venv(self):
        """إنشاء بيئة افتراضية"""
        try:
            import subprocess
            import os
            python_exe = os.path.join(self.exe_dir, 'python_runtime', 'python.exe')
            venv_dir = os.path.join(self.exe_dir, 'venv')
            if os.path.exists(venv_dir):
                self.output.emit(tr_static(self.lang, 'venv_exists'))
                return True
            if not os.path.exists(python_exe):
                import glob
                python_candidates = glob.glob(os.path.join(self.exe_dir, 'python_runtime', '**', 'python.exe'), recursive=True)
                if python_candidates:
                    python_exe = python_candidates[0]
                    self.output.emit(f"تم العثور على بايثون في: {python_exe}")
                else:
                    self.output.emit(tr_static(self.lang, 'error'))
                    return False
            self.output.emit(tr_static(self.lang, 'create_virtual_environment'))
            
            # Try using venv first
            cmd = [python_exe, '-m', 'venv', venv_dir]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.exe_dir,
                                  creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
            
            if result.returncode != 0:
                # If venv fails, it might be an embedded python, try virtualenv
                self.output.emit(tr_static(self.lang, 'venv_virtualenv_not_found'))
                cmd_ve = [python_exe, '-m', 'virtualenv', venv_dir]
                result_ve = subprocess.run(cmd_ve, capture_output=True, text=True, cwd=self.exe_dir,
                                      creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
                if result_ve.returncode != 0:
                    self.output.emit(f"{tr_static(self.lang, 'venv_creation_failed')}: {result_ve.stderr or result.stderr}")
                    return False
            
            self.output.emit(tr_static(self.lang, 'venv_created_success'))
            return True
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
            return False

    def _install_requirements(self):
        """تثبيت المتطلبات"""
        try:
            import subprocess
            import os
            pip_exe = os.path.join(self.exe_dir, 'venv', 'Scripts', 'pip.exe')
            requirements_file = os.path.join(self.exe_dir, f'requirements{self.requirements_type}.txt')
            if not os.path.exists(pip_exe):
                self.output.emit(tr_static(self.lang, 'error'))
                return False
            if not os.path.exists(requirements_file):
                self.output.emit(f"{tr_static(self.lang, 'requirements_file_not_found')}: {requirements_file}")
                return False
            self.output.emit(f"{tr_static(self.lang, 'installing_requirements_from')} {os.path.basename(requirements_file)}...")
            cmd = [pip_exe, 'install', '-r', requirements_file]
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=self.exe_dir,
                bufsize=1,
                universal_newlines=True,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            line_count = 0
            estimated_total_lines = 170
            current_progress = 66
            max_progress_for_step = 33
            for line in iter(self.process.stdout.readline, ''):
                if not self.should_run:
                    self.process.terminate()
                    return False
                if line.strip():
                    self.output.emit(line.strip())
                    line_count += 1
                    if line_count <= estimated_total_lines:
                        incremental_progress = (line_count / estimated_total_lines) * max_progress_for_step
                        new_progress = current_progress + incremental_progress
                        self.progress.emit(int(min(new_progress, 99)))
                    else:
                        self.progress.emit(99)
            return_code = self.process.wait()
            if return_code != 0:
                if not self.should_run:
                    return False
                self.output.emit(f"{tr_static(self.lang, 'error')}: {return_code}")
                return False
            self.progress.emit(99)
            self.output.emit(tr_static(self.lang, 'environment_setup_finished'))
            self.progress.emit(100)  # الوصول إلى 100% بعد الرسالة
            return True
        except Exception as e:
            if not self.should_run:
                return False
            self.output.emit(f"{tr_static(self.lang, 'error')}: {str(e)}")
            return False

    def stop_process(self):
        """إيقاف العملية"""
        self.should_run = False
        if hasattr(self, 'process') and self.process:
            try:
                self.process.terminate()
                self.process.kill()
            except:
                pass

class TranslationWorker(QObject):
    """عامل لتنفيذ عمليات الترجمة في الخلفية"""
    finished = Signal()
    progress = Signal(int, int)  # إشارة لإظهار تقدم الترجمة (الحالي, الإجمالي)
    result = Signal(str)
    error = Signal(str)
    status_update = Signal(str)
    output = Signal(str)
    time_taken = Signal(float)
    def __init__(self, server_url, text, source_lang="en", target_lang="ar", lang='ar'):
        super().__init__()
        self.server_url = server_url
        self.text = text
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.lang = lang
        self.max_chunk_length = 500  # الحد الأقصى لطول كل جزء
        self.should_run = True

    def run(self):
        """تنفيذ عملية الترجمة في الخلفية"""
        try:
            if not self.should_run:
                return
            import time
            start_time = time.time()
            lines = self.text.split('\n')
            def split_line(line: str):
                if len(line) <= self.max_chunk_length:
                    return [line]
                parts = line.split()
                chunks = []
                current = ''
                for word in parts:
                    if current:
                        candidate = current + ' ' + word
                    else:
                        candidate = word
                    if len(candidate) > self.max_chunk_length:
                        if current:
                            chunks.append(current)
                        if len(word) > self.max_chunk_length:
                            for i in range(0, len(word), self.max_chunk_length):
                                chunks.append(word[i:i+self.max_chunk_length])
                            current = ''
                        else:
                            current = word
                    else:
                        current = candidate
                if current:
                    chunks.append(current)
                return chunks
            total_chunks = 0
            for line in lines:
                if line.strip():
                    chunks = split_line(line)
                    total_chunks += len(chunks)
            self.status_update.emit(f"Chunking: {total_chunks}")
            full_translation = ""
            chunk_index = 0
            for line in lines:
                if not self.should_run:
                    break
                if line.strip():  # إذا كان السطر يحتوي على نص
                    chunks = split_line(line)
                    line_translation = ""
                    for chunk in chunks:
                        if not self.should_run:
                            break
                        self.progress.emit(chunk_index + 1, total_chunks)
                        self.status_update.emit(f"{tr_static(self.lang, 'translating_in_progress')} {chunk_index+1} / {total_chunks}")
                        if hasattr(self, 'source_lang') and hasattr(self, 'target_lang'):
                            response = requests.post(
                                f'{self.server_url}/translate',
                                json={'text': chunk, 'source': self.source_lang, 'target': self.target_lang},
                                timeout=30
                            )
                        else:
                            response = requests.post(
                                f'{self.server_url}/translate',
                                json={'text': chunk, 'source': 'en', 'target': 'ar'},
                                timeout=30
                            )
                        if response.status_code == 200:
                            result = response.json()
                            translation = result.get('translation', '')
                            line_translation += translation + " "
                        else:
                            self.error.emit(f"{tr_static(self.lang, 'error')}: {response.status_code}")
                            return
                        chunk_index += 1
                    full_translation += line_translation.strip() + "\n"
                else:
                    full_translation += "\n"
            if not self.should_run:
                return
            end_time = time.time()
            response_time = end_time - start_time
            self.time_taken.emit(response_time)
            self.status_update.emit(f' {tr_static(self.lang, "translation_successful")} | {tr_static(self.lang, "response_time")}: {response_time:.2f} {tr_static(self.lang, "seconds")}')
            self.result.emit(full_translation.rstrip())
        except Exception as e:
            self.error.emit(f' {tr_static(self.lang, "translation_failed")}: {str(e)}')
        finally:
            self.finished.emit()

    def stop(self):
        """إيقاف عملية الترجمة"""
        self.should_run = False
        try:
            import requests
            requests.post(f'{self.server_url}/cancel', timeout=1)
        except:
            pass
  
class MainWindow(QMainWindow):
    request_restart = Signal()
    OPUS_BASE_NAME = "OPUS-MT"
    def tr(self, key):
        """جلب النص المترجم بناءً على اللغة الحالية"""
        return TRANSLATIONS.get(self.language, TRANSLATIONS['ar']).get(key, key)
    def __init__(self):
        super().__init__()
        self.exe_dir = get_application_path()
        self.language = 'ar'  # اللغة الافتراضية
        
        # تحميل تفضيلات اللغة مسبقاً قبل إنشاء الواجهة
        try:
            possible_paths = [
                os.path.join(self.exe_dir, 'settings.json'),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json'),
                os.path.join(os.getcwd(), 'settings.json'),
                os.path.join(os.path.expanduser('~'), 'METranslator', 'settings.json'),
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    with open(path, 'r', encoding='utf-8') as f:
                        settings = json.load(f)
                        self.language = settings.get('ui_language', 'ar')
                    break
        except Exception:
            pass

        self.setWindowTitle(self.tr('app_title'))
        self.setMinimumSize(650, 650)
        self.setWindowIcon(QIcon(os.path.join(self.exe_dir, 'icons', 'MET.ico')))
        self.previous_c2_device = "GPU"
        self.previous_onnx_device = "GPU"
        self.backend = 'c2'
        self.model_running = False
        self.running_model_type = None # نوع النموذج الذي يعمل حالياً
        self.server_url = 'http://127.0.0.1:8000'
        self.proc = None
        self.worker = None
        self.worker_thread = None
        self.worker_thread_active = False
        self.translation_worker = None
        self.translation_thread = None
        self.translation_in_progress = False
        self.translation_time = 0.0
        self.translation_widget = None
        # حالة الخادم
        self.server_fully_loaded = False
        # إعدادات تحميل النموذج
        self.download_worker = None
        self.download_thread = None
        self.download_in_progress = False
        # إعدادات تحميل نموذج madlad400
        self.download_madlad400_worker = None
        self.download_madlad400_thread = None
        self.download_madlad400_in_progress = False
        # إعدادات تحميل نموذج madlad400
        self.download_madlad400_worker = None
        self.download_madlad400_thread = None
        self.download_madlad400_in_progress = False
        # إعدادات تحميل نموذج mbartlarge50
        self.download_mbartlarge50_worker = None
        self.download_mbartlarge50_thread = None
        self.download_mbartlarge50_in_progress = False
        # إعدادات تحويل النموذج
        self.convert_c2_worker = None
        self.convert_c2_thread = None
        self.convert_c2_in_progress = False
        self.convert_onnx_worker = None
        self.convert_onnx_thread = None
        self.convert_onnx_in_progress = False
        # إعدادات تحويل نموذج MBARTLARGE50
        self.convert_mbartlarge50_c2_worker = None
        self.convert_mbartlarge50_c2_thread = None
        self.convert_mbartlarge50_c2_in_progress = False
        self.convert_mbartlarge50_onnx_worker = None
        self.convert_mbartlarge50_onnx_thread = None
        self.convert_mbartlarge50_onnx_in_progress = False
        # إعدادات إعداد البيئة
        self.setup_worker = None
        self.setup_thread = None
        self.setup_in_progress = False
        # إعدادات نافذة الإعداد
        self.setup_dialog = None
        # إعدادات ويدجت التحميل والتحويل
        self.download_widget = None
        # إعدادات التحقق من المكتبات
        self.library_verification_worker = None
        self.library_verification_thread = None
        # متغيرات للتحقق من الوجود المسبق
        self.python_installed = False
        self.venv_created = False
        self.requirements_installed = False
        # متغيرات النماذج
        self.c2_model_path = ""
        self.onnx_model_path = ""
        self.madlad400_model_path = ""
        self.c2_device = "cuda"
        self.onnx_device = "cuda"
        self.mbartlarge50_device = "cuda"
        self.madlad400_device = "cuda"
        self.theme = "dark" # الثيم الافتراضي
        self.current_font_size = 12  # حجم الخط الحالي للترجمة
        # قوائم النماذج
        self.c2_models = []
        self.onnx_models = []
        self.madlad400_models = ["madlad400"]  # نماذج متعددة اللغات
        self.mbartlarge50_c2_models = []
        self.mbartlarge50_onnx_models = []
        self.mbartlarge50_backend = 'mbartlarge50c2'  # الخلفية الافتراضية لـ MBARTLARGE50
        self.source_lang = "en"
        self.target_lang = "ar"
        # مجموعة الأزرار الراديو للنماذج
        self.backend_button_group = QButtonGroup()
        # إعداد واجهة المستخدم
        self.setup_ui()
        # تحميل قوائم النماذج
        self.load_model_lists()
        # تحميل المسارات من متغيرات البيئة
        self.load_model_paths()
        # تحميل الإعدادات تلقائياً من الملف الافتراضي
        self.load_settings_auto()
        # تهيئة مسارات النماذج بناءً على الإعدادات المحملة
        self.initialize_model_paths()
        self.lang_widget.setVisible(True)
        # تعطيل زر الترجمة في البداية
        self.translate_btn.setEnabled(False)
        # حفظ القيم الأولية كقيم سابقة
        self.previous_opus_backend = self.opus_backend_combo.currentText()
        self.previous_opus_model = self.opus_model_combo.currentText()
        self.previous_opus_device = self.opus_device_combo.currentText()
        self.previous_madlad400_model = self.madlad400_model_combo.currentText()
        self.previous_mbartlarge50_model = self.mbartlarge50_model_combo.currentText()
        self.previous_madlad400_device = self.madlad400_device_combo.currentText()
        self.previous_mbartlarge50_device = self.mbartlarge50_device_combo.currentText()
        # إضافة متغيرات للأجهزة السابقة لـ OPUS
        self.previous_c2_device = "GPU"
        self.previous_onnx_device = "GPU"
        # ربط إشارات تغيير اللغات لحفظ الإعدادات تلقائياً (الآن في شريط الأدوات)
        self.source_lang_combo.currentTextChanged.connect(self.save_settings_auto)
        self.target_lang_combo.currentTextChanged.connect(self.save_settings_auto)
        # ربط إشارات تغيير اللغات لتحديث قوائم النماذج
        self.source_lang_combo.currentTextChanged.connect(self.update_opus_models)
        self.target_lang_combo.currentTextChanged.connect(self.update_opus_models)
        # تطبيق الاتجاه الصحيح للغات في البداية
        self.change_ui_language(self.ui_lang_combo.currentIndex())
    
    def show_help_dialog(self):
        """عرض نافذة التعليمات"""
        dialog = QDialog(self)
        dialog.setWindowTitle(self.tr('help_title'))
        dialog.setMinimumSize(500, 400)
        dialog.setWindowModality(Qt.ApplicationModal)
        layout = QVBoxLayout(dialog)
        help_text = QTextBrowser()
        help_text.setReadOnly(True)
        help_text.setOpenExternalLinks(True)
        help_text.setHtml(self.tr('help_content'))
        layout.addWidget(help_text)
        close_btn = QPushButton(self.tr('close'))
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        self.apply_dark_title_bar(dialog)
        dialog.exec()

    def closeEvent(self, event):
        """إغلاق التطبيق بشكل نظيف وإيقاف جميع الخيوط"""
        # إيقاف خيط التحميل إذا كان نشطاً
        if self.download_in_progress and self.download_worker:
            self.download_worker.stop_process()
            if self.download_thread:
                self.download_thread.join()
        # إيقاف خيط تحميل madlad400 إذا كان نشطاً
        if self.download_madlad400_in_progress and self.download_madlad400_worker:
            self.download_madlad400_worker.stop_process()
            if self.download_madlad400_thread:
                self.download_madlad400_thread.join()
        # إيقاف خيط تحميل mbartlarge50 إذا كان نشطاً
        if self.download_mbartlarge50_in_progress and self.download_mbartlarge50_worker:
            self.download_mbartlarge50_worker.stop_process()
            if self.download_mbartlarge50_thread:
                self.download_mbartlarge50_thread.join()
        # إيقاف خيط تحويل MBARTLARGE50 إلى C2 إذا كان نشطاً
        if self.convert_mbartlarge50_c2_in_progress and self.convert_mbartlarge50_c2_worker:
            self.convert_mbartlarge50_c2_worker.stop_process()
            if self.convert_mbartlarge50_c2_thread:
                self.convert_mbartlarge50_c2_thread.join()
        # إيقاف خيط تحويل MBARTLARGE50 إلى ONNX إذا كان نشطاً
        if self.convert_mbartlarge50_onnx_in_progress and self.convert_mbartlarge50_onnx_worker:
            self.convert_mbartlarge50_onnx_worker.stop_process()
            if self.convert_mbartlarge50_onnx_thread:
                self.convert_mbartlarge50_onnx_thread.join()
        # إيقاف خيط الترجمة إذا كان نشطاً
        if self.translation_in_progress and self.translation_worker:
            self.translation_worker.stop()
            if self.translation_thread:
                self.translation_thread.join()
        # إيقاف خيط إعداد البيئة إذا كان نشطاً
        if self.setup_in_progress and self.setup_worker:
            self.setup_worker.stop_process()
            if self.setup_thread:
                self.setup_thread.join()
        # إيقاف خيط التحقق من المكتبات إذا كان نشطاً
        try:
            if hasattr(self, 'library_verification_thread') and self.library_verification_thread:
                self.library_verification_thread.quit()
                self.library_verification_thread.wait(3000)  # انتظر حتى 3 ثوانٍ
        except RuntimeError:
            # تجاهل الخطأ إذا كان الخيط محذوفاً بالفعل
            pass
        # إيقاف خيط الخادم إذا كان نشطاً
        try:
            if hasattr(self, 'worker_thread') and self.worker_thread:
                self.worker_thread.quit()
                self.worker_thread.wait(3000)  # انتظر حتى 3 ثوانٍ
        except RuntimeError:
            # تجاهل الخطأ إذا كان الخيط محذوفاً بالفعل
            pass
        # إيقاف خادم الترجمة إذا كان نشطاً
        if self.model_running:
            self.stop()  # استدعاء دالة الإيقاف الموجودة مسبقاً
        # تحرير الذاكرة
        try:
            import gc
            gc.collect()
        except:
            pass
        # قبول حدث الإغلاق
        event.accept()

    def apply_theme(self):
        """تطبيق السمة (داكن/فاتح)"""
        is_dark = self.theme == 'dark'
        # الألوان المشتركة
        accent_color = "#00f2ff" if is_dark else "#008c9e"
        bg_color = "#0f1016" if is_dark else "#f5f6fa"
        text_color = "#e0e6ed" if is_dark else "#2f3640"
        input_bg = "#13151d" if is_dark else "#ffffff"
        border_color = "#2b3040" if is_dark else "#dcdde1"
        btn_gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1a1c29, stop:1 #24273a)" if is_dark else "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:1 #f0f0f0)"
        btn_hover = "#2a2d42" if is_dark else "#e6e6e6"
        btn_text = "#00f2ff" if is_dark else "#008c9e"

        # متغيرات شريط الحالة (Status Bar Variables)
        sb_bg = "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364)" if is_dark else "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #dfe4ea, stop:0.5 #f1f2f6, stop:1 #ffffff)"
        sb_text_main = "#00f2ff" if is_dark else "#008c9e"
        sb_text_center = "#ffffff" if is_dark else "#2f3640"
        sb_text_right = "#7bed9f" if is_dark else "#27ae60"
        sb_border = "#00f2ff" if is_dark else "#008c9e"
        style_sheet = f"""
            /* النوافذ والخلفيات */
            QMainWindow, QWidget {{
                background-color: {bg_color};
                color: {text_color};
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }}
            /* العناوين والتسميات */
            QLabel {{
                color: {"#b0b8c3" if is_dark else "#57606f"};
                font-weight: 500;
            }}
            /* الأزرار */
            QPushButton {{
                background-color: {btn_gradient};
                border: 1px solid {"#3d4c6e" if is_dark else "#c8d6e5"};
                border-radius: 8px;
                color: {btn_text};
                padding: 8px 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {btn_hover};
                border-color: {accent_color};
            }}
            QPushButton:pressed {{
                background-color: {accent_color};
                color: {bg_color};
            }}
            QPushButton:disabled {{
                background-color: {"#161821" if is_dark else "#dfe4ea"};
                border-color: {border_color};
                color: {"#4a5060" if is_dark else "#a4b0be"};
            }}
            /* مربعات الإدخال والقوائم */
            QLineEdit, QTextEdit, QComboBox {{
                background-color: {input_bg};
                border: 1px solid {border_color};
                border-radius: 6px;
                color: {text_color};
                padding: 6px;
                selection-background-color: {accent_color};
                selection-color: {bg_color};
            }}
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {{
                border: 1px solid {accent_color};
                background-color: {"#171924" if is_dark else "#fdfdfd"};
            }}
            /* القوائم المنسدلة */
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid {accent_color};
                margin-right: 5px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {input_bg};
                border: 1px solid {border_color};
                selection-background-color: {accent_color};
                selection-color: {bg_color};
                outline: none;
                color: {text_color};
            }}
            /* المجموعات GroupBox */
            QGroupBox {{
                border: 1px solid {border_color};
                border-radius: 10px;
                margin-top: 25px;
                background-color: transparent;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 5px 15px;
                background-color: {"#1a1c29" if is_dark else "#f1f2f6"};
                color: {accent_color};
                border: 1px solid {accent_color};
                border-radius: 15px;
            }}
            /* أزرار الراديو */
            QRadioButton {{
                spacing: 10px;
                color: {text_color};
            }}
            QRadioButton::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 9px;
                border: 2px solid #555;
                background: {input_bg};
            }}
            QRadioButton::indicator:checked {{
                border-color: {accent_color};
                background-color: {accent_color};
            }}
            /* شريط التمرير */
            QScrollBar:vertical {{
                background: {bg_color};
                width: 8px;
                margin: 0;
            }}
            QScrollBar::handle:vertical {{
                background: {border_color};
                min-height: 20px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {accent_color};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
            /* شريط الحالة */
            /* شريط الحالة المستقبلي */
            /* شريط الحالة المستقبلي */
            QStatusBar {{
                background: {sb_bg};
                color: {sb_text_main};
                border-top: 1px solid {sb_border};
                min-height: 28px;
            }}
            QLabel#status_left {{
                color: {sb_text_main};
                font-weight: bold;
                padding-left: 10px;
            }}
            QLabel#status_center {{
                color: {sb_text_center};
                font-weight: bold;
            }}
            QLabel#status_right {{
                color: {sb_text_right};
                font-weight: bold;
                padding-right: 10px;
            }}
            QSizeGrip {{
                background: transparent;
            }}
            /* أشرطة التقدم */
            QProgressBar {{
                background-color: {input_bg};
                border: 1px solid {border_color};
                border-radius: 6px;
                text-align: center;
                color: {text_color};
                font-size: 11px;
                font-weight: bold;
                height: 14px;
            }}
            QProgressBar::chunk {{
                background-color: {accent_color};
                border-radius: 4px;
                margin: 2px;
            }}
            /* مربعات الاختيار */
            QCheckBox {{
                spacing: 8px;
                color: {text_color};
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 2px solid {"#555" if is_dark else "#ccc"};
                background: {input_bg};
            }}
            QCheckBox::indicator:checked {{
                border-color: {accent_color};
                background-color: {accent_color};
            }}
            QCheckBox::indicator:hover {{
                border-color: {accent_color};
            }}
            QCheckBox:disabled {{
                color: {"#4a5060" if is_dark else "#a4b0be"};
            }}
        """
        self.setStyleSheet(style_sheet)
        # تحديث الأيقونات بناءً على الثيم
        is_dark = self.theme.lower() == 'dark'
        suffix = "black" if is_dark else "light"
        # أيقونات شريط الأدوات (التي لا تتغير حالتها)
        if hasattr(self, 'run_btn'):
            self.run_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'run_server_{suffix}.png')))
        if hasattr(self, 'download_setup_btn'):
            self.download_setup_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'env_setup_{suffix}.png')))
        # أيقونات أزرار الإعدادات والتحميل (تعتمد على الحالة: إعدادات أم عودة)
        if hasattr(self, 'settings_btn'):
            if self.settings_widget.isVisible():
                self.settings_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'back_{suffix}.png')))
            else:
                self.settings_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'settings_{suffix}.png')))
        if hasattr(self, 'download_convert_btn'):
            if self.download_widget.isVisible():
                self.download_convert_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'back_{suffix}.png')))
            else:
                self.download_convert_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'download_convert_{suffix}.png')))
        # أيقونات أزرار التحويل
        if hasattr(self, 'convert_c2_btn'):
            self.convert_c2_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'convert_{suffix}.png')))
        if hasattr(self, 'convert_onnx_btn'):
            self.convert_onnx_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'convert_{suffix}.png')))
        if hasattr(self, 'convert_mbartlarge50_c2_btn'):
            self.convert_mbartlarge50_c2_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'convert_{suffix}.png')))
        if hasattr(self, 'convert_mbartlarge50_onnx_btn'):
            self.convert_mbartlarge50_onnx_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'convert_{suffix}.png')))
        # إعادة تطبيق حجم الخط المخصص بعد تطبيق السمة
        if hasattr(self, 'input_text') and hasattr(self, 'output_text') and hasattr(self, 'current_font_size'):
            # استخدام كلا الطريقتين معاً
            font = QFont("Segoe UI", self.current_font_size)
            self.input_text.setFont(font)
            self.output_text.setFont(font)
            input_style = f"""
            QTextEdit#input_text {{
                font-family: 'Segoe UI', sans-serif;
                font-size: {self.current_font_size}pt;
            }}
            """
            output_style = f"""
            QTextEdit#output_text {{
                font-family: 'Segoe UI', sans-serif;
                font-size: {self.current_font_size}pt;
            }}
            """
            self.input_text.setStyleSheet(input_style)
            self.output_text.setStyleSheet(output_style)
        self.apply_dark_title_bar()  # إعادة تطبيق شريط العنوان عند تغيير الثيم
    def apply_dark_title_bar(self, window=None):
        """تطبيق المظهر الداكن/الفاتح على شريط العنوان في ويندوز"""
        if sys.platform == 'win32':
            try:
                target_window = window if window else self
                # DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                hwnd = target_window.winId()
                attribute = DWMWA_USE_IMMERSIVE_DARK_MODE
                # إعداد القيمة بناءً على الثيم المختار
                is_dark = getattr(self, 'theme', 'dark') == 'dark'
                value = ctypes.c_int(1 if is_dark else 0)
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    int(hwnd), 
                    attribute, 
                    ctypes.byref(value), 
                    ctypes.sizeof(value)
                )
            except Exception:
                pass # Fail silently if not supported

    def show_themed_message_box(self, icon, title, text, buttons=QMessageBox.Ok, default_button=QMessageBox.Ok):
        """عرض نافذة رسائل مع تطبيق الثيم على شريط العنوان"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(icon)
        msg_box.setStandardButtons(buttons)
        msg_box.setDefaultButton(default_button)
        # تطبيق الثيم
        self.apply_dark_title_bar(msg_box)
        # تطبيق ستايل شيت النافذة الرئيسية على الرسالة لضمان تناسق الألوان
        msg_box.setStyleSheet(self.styleSheet())
        return msg_box.exec()

    def setup_ui(self):
        """إعداد واجهة المستخدم"""
        # إنشاء القطعة المركزية
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # إنشاء التخطيط الرئيسي
        main_layout = QVBoxLayout(central_widget)
        # إنشاء شريط الأدوات
        self.create_toolbar()
        main_layout.addWidget(self.toolbar_frame)
        # إنشاء إعدادات النموذج والخادم
        self.settings_widget = self.create_settings_widget()
        self.settings_widget.setVisible(False)
        main_layout.addWidget(self.settings_widget)
        # إنشاء إعدادات التحميل والتحويل
        self.download_widget = self.create_download_widget()
        self.download_widget.setVisible(False)
        main_layout.addWidget(self.download_widget)
        # إنشاء منطقة الترجمة
        self.translation_widget = self.create_translation_widget()
        self.translation_widget.setVisible(True)
        main_layout.addWidget(self.translation_widget)
        # إنشاء شريط الحالة مع ثلاثة أقسام
        self.status_bar = QStatusBar()
        self.status_bar.setSizeGripEnabled(False) # إزالة مقبض تغيير الحجم
        self.setStatusBar(self.status_bar)
        # إنشاء التسميات للأقسام المختلفة
        self.left_label = QLabel(self.tr('status_offline'))
        self.left_label.setObjectName("status_left")
        self.center_label = QLabel('')
        self.center_label.setObjectName("status_center")
        self.right_label = QLabel('')
        self.right_label.setObjectName("status_right")
        self.right_label.setAlignment(Qt.AlignRight)
        # إنشاء حاوية لعناصر شريط الحالة
        status_container = QWidget()
        status_layout = QHBoxLayout(status_container)
        status_layout.setContentsMargins(0, 0, 0, 0)
        
        # إضافة التسميات إلى تخطيط الحاوية
        status_layout.addWidget(self.left_label)
        status_layout.addStretch()
        status_layout.addWidget(self.center_label)
        status_layout.addStretch()
        status_layout.addWidget(self.right_label)
        
        # إضافة الحاوية إلى شريط الحالة
        self.status_bar.addWidget(status_container, 1)
        self.apply_theme()
        # self.apply_dark_title_bar() is called inside apply_theme now

    def create_toolbar(self):
        """إنشاء شريط الأدوات"""
        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(10, 5, 10, 5)
        # أزرار التحكم في الخادم
        self.run_btn = QPushButton()
        # سيتم تعيين الأيقونة عبر apply_theme
        self.run_btn.setIconSize(QSize(32, 32))
        self.run_btn.setToolTip(self.tr('run_server'))
        self.run_btn.clicked.connect(self.run)
        self.run_btn.setFixedSize(40, 40)
        self.stop_btn = QPushButton()
        self.stop_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', 'stop_server.png')))
        self.stop_btn.setIconSize(QSize(26, 26))
        self.stop_btn.setToolTip(self.tr('stop_server'))
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setFixedSize(40, 40)
        # زر إعداد البيئة
        self.download_setup_btn = QPushButton()
        # سيتم تعيين الأيقونة عبر apply_theme
        self.download_setup_btn.setIconSize(QSize(32, 32))
        self.download_setup_btn.setToolTip(self.tr('env_setup'))
        self.download_setup_btn.clicked.connect(self.open_setup_dialog)
        self.download_setup_btn.setFixedSize(40, 40)
        self.download_setup_btn.setEnabled(True)
        # إنشاء اختيار اللغات للنموذج متعدد اللغات
        self.lang_widget = QWidget()
        self.lang_layout = QHBoxLayout(self.lang_widget)
        # إضافة مسافة قابلة للتمدد بين اللغة المصدر والوجهة
        self.from_label = QLabel(self.tr('from'))
        self.lang_layout.addWidget(self.from_label)
        self.source_lang_combo = QComboBox()
        self.source_lang_combo.addItems(["ar", "en", "fr", "de", "es", "it", "pt", "ru", "zh", "ja", "ko"])
        self.source_lang_combo.setCurrentText("en")
        self.source_lang_combo.setMinimumWidth(80)
        self.lang_layout.addWidget(self.source_lang_combo)

        self.to_label = QLabel(self.tr('to'))
        self.lang_layout.addWidget(self.to_label)
        self.target_lang_combo = QComboBox()
        self.target_lang_combo.addItems(["ar", "en", "fr", "de", "es", "it", "pt", "ru", "zh", "ja", "ko"])
        self.target_lang_combo.setCurrentText("ar")
        self.target_lang_combo.setMinimumWidth(80)
        self.lang_layout.addWidget(self.target_lang_combo)
        # أزرار الإعدادات
        self.settings_btn = QPushButton()
        # سيتم تعيين الأيقونة عبر apply_theme
        self.settings_btn.setIconSize(QSize(32, 32))
        self.settings_btn.setToolTip(self.tr('settings'))
        self.settings_btn.clicked.connect(self.toggle_settings)
        self.settings_btn.setFixedSize(40, 40)
        # زر إعدادات التحميل والتحويل
        # زر إعدادات التحميل والتحويل
        self.download_convert_btn = QPushButton()
        # سيتم تعيين الأيقونة عبر apply_theme
        self.download_convert_btn.setIconSize(QSize(32, 32))
        self.download_convert_btn.setToolTip(self.tr('download_convert'))
        self.download_convert_btn.clicked.connect(self.toggle_download)
        self.download_convert_btn.setFixedSize(40, 40)
        # زر التعليمات
        self.help_btn = QPushButton('❓')
        self.help_btn.setToolTip(self.tr('help'))
        self.help_btn.clicked.connect(self.show_help_dialog)
        self.help_btn.setFixedSize(40, 40)
        # إضافة الأزرار إلى التخطيط
        toolbar_layout.addWidget(self.run_btn)
        toolbar_layout.addWidget(self.stop_btn)
        toolbar_layout.addWidget(self.download_setup_btn)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.lang_widget)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.settings_btn)
        toolbar_layout.addWidget(self.download_convert_btn)
        toolbar_layout.addWidget(self.help_btn)
        # إنشاء إطار لشريط الأدوات
        self.toolbar_frame = QFrame()
        self.toolbar_frame.setLineWidth(2)
        self.toolbar_frame.setLayout(toolbar_layout)
        self.toolbar_frame.setFrameShape(QFrame.StyledPanel)

    def create_settings_widget(self):
        """إنشاء ويدجت الإعدادات بتصميم عصري ومبسط"""
        settings_widget = QWidget()
        # settings_widget.setStyleSheet removed
        settings_layout = QVBoxLayout(settings_widget)
        settings_layout.setContentsMargins(10, 10, 10, 10)
        settings_layout.setSpacing(8)
        # مجموعة اختيار الثيم
        self.theme_group = QGroupBox(self.tr('appearance'))
        # 1. التخطيط الرئيسي للجروب (سيقوم بمحاذاة المحتوى في الوسط)
        main_layout = QHBoxLayout()
        main_layout.addStretch()  # مسافة مرنة من اليسار
        # 2. تخطيط داخلي يحتوي على العناصر فقط
        inner_layout = QHBoxLayout()
        self.theme_label = QLabel(self.tr('select_theme'))
        self.theme_combo = QComboBox()
        self.theme_combo.setFixedWidth(100)
        self.theme_combo.addItems(["Dark", "Light"])
        # تعيين القيمة الحالية
        self.theme_combo.setCurrentText(self.theme.capitalize())
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        self.theme_combo.currentTextChanged.connect(self.save_settings_auto)
        # إضافة العناصر للتخطيط الداخلي
        inner_layout.addWidget(self.theme_label)
        inner_layout.addWidget(self.theme_combo)
        # إضافة اختيار اللغة
        self.lang_label = QLabel(self.tr('select_lang'))
        self.ui_lang_combo = QComboBox()
        self.ui_lang_combo.setFixedWidth(100)
        self.ui_lang_combo.addItem("العربية", "ar")
        self.ui_lang_combo.addItem("English", "en")
        self.ui_lang_combo.addItem("Français", "fr")
        self.ui_lang_combo.addItem("Deutsch", "de")
        self.ui_lang_combo.addItem("Español", "es")
        self.ui_lang_combo.addItem("Italiano", "it")
        self.ui_lang_combo.addItem("Português", "pt")
        self.ui_lang_combo.addItem("Русский", "ru")
        self.ui_lang_combo.addItem("简体中文", "zh")
        self.ui_lang_combo.addItem("日本語", "ja")
        self.ui_lang_combo.addItem("한국어", "ko")
        self.ui_lang_combo.setCurrentIndex(0 if self.language == 'ar' else 1)
        self.ui_lang_combo.currentIndexChanged.connect(self.change_ui_language)
        self.ui_lang_combo.currentIndexChanged.connect(self.save_settings_auto)
        inner_layout.addSpacing(20)
        inner_layout.addWidget(self.lang_label)
        inner_layout.addWidget(self.ui_lang_combo)
        # 3. إضافة التخطيط الداخلي إلى التخطيط الرئيسي
        main_layout.addLayout(inner_layout)
        main_layout.addStretch()  # مسافة مرنة من اليمين
        self.theme_group.setLayout(main_layout)
        settings_layout.addWidget(self.theme_group)
        # مجموعة اختيار نموذج الترجمة
        self.main_model_group = QGroupBox(self.tr('select_model'))
        main_model_layout = QVBoxLayout()
        main_model_layout.setSpacing(15)
          # مجموعة اختيار النموذج
        opus_group = QGroupBox(f"{self.OPUS_BASE_NAME}")
        opus_group.setStyleSheet("""
        # Style removed
        """)
        opus_layout = QVBoxLayout()
        opus_layout.setSpacing(10)
        # خيار OPUS-MT-en-ar
        opus_option_layout = QHBoxLayout()
        src = self.source_lang_combo.currentText()
        tgt = self.target_lang_combo.currentText()
        if not src or not tgt:
            import logging
            logging.warning("Source or target language is empty; using default OPUS label.")
            opus_label = f"{self.OPUS_BASE_NAME}-UNKNOWN"
        else:
            opus_label = f"{self.OPUS_BASE_NAME}-{src}-{tgt}"
        self.opus_radio = QRadioButton(opus_label)
        self.opus_radio.setChecked(True)
        # RadioButton style removed
        self.opus_radio.setFixedWidth(160) # Fixed Width
        self.backend_button_group.addButton(self.opus_radio)
        self.opus_radio.clicked.connect(lambda: self.set_backend('opus'))
        # إضافة اختيار الخلفية لـ OPUS
        self.opus_backend_combo = QComboBox()
        self.opus_backend_combo.addItems(["CTranslate2", "ONNX"])
        self.opus_backend_combo.blockSignals(True)
        self.opus_backend_combo.setCurrentText("CTranslate2")
        self.opus_backend_combo.blockSignals(False)
        self.opus_backend_combo.currentTextChanged.connect(self.on_opus_backend_changed)
        # ComboBox style removed
        self.opus_backend_combo.setFixedWidth(130) # Fixed Width
        self.opus_model_combo = QComboBox()
        self.opus_model_combo.addItems(self.get_c2_models())
        self.opus_model_combo.blockSignals(True)
        self.opus_model_combo.blockSignals(False)
        self.opus_model_combo.currentTextChanged.connect(self.on_opus_model_changed)
        # ComboBox style removed
        self.opus_model_combo.setFixedWidth(130) # Fixed Width
        self.opus_device_combo = QComboBox()
        self.opus_device_combo.addItems(["GPU", "CPU"])
        self.opus_device_combo.blockSignals(True)
        self.opus_device_combo.setCurrentText("GPU")
        self.opus_device_combo.blockSignals(False)
        self.opus_device_combo.currentTextChanged.connect(self.update_opus_device)
        # ComboBox style removed
        self.opus_device_combo.setFixedWidth(80) # Fixed Width
        opus_option_layout.addWidget(self.opus_radio)
        # Align with other groups
        opus_colon = QLabel(":")
        opus_colon.setFixedWidth(15)
        opus_option_layout.addWidget(opus_colon)
        opus_option_layout.addStretch()
        opus_option_layout.addWidget(self.opus_backend_combo)
        opus_option_layout.addWidget(self.opus_model_combo)
        opus_option_layout.addStretch()
        self.opus_device_label = QLabel(self.tr('device'))
        self.opus_device_label.setFixedWidth(50)
        opus_option_layout.addWidget(self.opus_device_label)
        opus_option_layout.addWidget(self.opus_device_combo)
        opus_layout.addLayout(opus_option_layout)
        opus_group.setLayout(opus_layout)
        main_model_layout.addWidget(opus_group)
        # خيار متعدد اللغات
        self.multilingual_model_group = QGroupBox(self.tr('multilingual_models'))
        self.multilingual_model_group.setStyleSheet("""
        # Style removed
        """)
        model_layout = QVBoxLayout()
        model_layout.setSpacing(10)
        # مجموعة نموذج MBARTLARGE50
        mbartlarge50_option_layout = QHBoxLayout()
        self.mbartlarge50_radio = QRadioButton("MBARTLARGE50")
        # RadioButton style removed
        self.mbartlarge50_radio.setFixedWidth(160) # Fixed Width
        self.backend_button_group.addButton(self.mbartlarge50_radio)
        self.mbartlarge50_radio.clicked.connect(lambda: self.set_backend('mbartlarge50'))
        # إضافة اختيار الخلفية لـ MBARTLARGE50
        self.mbartlarge50_backend_combo = QComboBox()
        self.mbartlarge50_backend_combo.addItems(["CTranslate2", "ONNX"])
        self.mbartlarge50_backend_combo.blockSignals(True)
        self.mbartlarge50_backend_combo.setCurrentText("CTranslate2")
        self.mbartlarge50_backend_combo.blockSignals(False)
        self.mbartlarge50_backend_combo.currentTextChanged.connect(self.on_mbartlarge50_backend_changed)
        # ComboBox style removed
        self.mbartlarge50_backend_combo.setFixedWidth(130) # Fixed Width
        self.mbartlarge50_model_combo = QComboBox()
        self.mbartlarge50_model_combo.addItems(self.get_mbartlarge50_c2_models())
        self.mbartlarge50_model_combo.blockSignals(True)
        self.mbartlarge50_model_combo.blockSignals(False)
        self.mbartlarge50_model_combo.currentTextChanged.connect(self.on_mbartlarge50_model_changed)
        # ComboBox style removed
        self.mbartlarge50_model_combo.setFixedWidth(130) # Fixed Width
        self.mbartlarge50_device_combo = QComboBox()
        self.mbartlarge50_device_combo.addItems(["GPU", "CPU"])
        self.mbartlarge50_device_combo.blockSignals(True)
        self.mbartlarge50_device_combo.setCurrentText("GPU")
        self.mbartlarge50_device_combo.blockSignals(False)
        self.mbartlarge50_device_combo.currentTextChanged.connect(self.update_mbartlarge50_device)
        # ComboBox style removed
        self.mbartlarge50_device_combo.setFixedWidth(80) # Fixed Width
        mbartlarge50_option_layout.addWidget(self.mbartlarge50_radio)
        mbart_colon = QLabel(":")
        mbart_colon.setFixedWidth(15)
        mbartlarge50_option_layout.addWidget(mbart_colon)
        mbartlarge50_option_layout.addStretch()
        mbartlarge50_option_layout.addWidget(self.mbartlarge50_backend_combo)
        mbartlarge50_option_layout.addWidget(self.mbartlarge50_model_combo)
        mbartlarge50_option_layout.addStretch()
        self.mbart_device_label = QLabel(self.tr('device'))
        self.mbart_device_label.setFixedWidth(50)
        mbartlarge50_option_layout.addWidget(self.mbart_device_label)
        mbartlarge50_option_layout.addWidget(self.mbartlarge50_device_combo)
        model_layout.addLayout(mbartlarge50_option_layout)
        # نموذج MADLA400
        madlad400_layout = QHBoxLayout()
        self.madlad400_radio = QRadioButton("MADLA400")
        # RadioButton style removed
        self.madlad400_radio.setFixedWidth(160) # Fixed Width
        self.backend_button_group.addButton(self.madlad400_radio)
        self.madlad400_radio.clicked.connect(lambda: self.set_backend('madlad400'))
        self.madlad400_model_combo = QComboBox()
        self.madlad400_model_combo.addItems(self.madlad400_models)
        self.madlad400_model_combo.blockSignals(True)
        self.madlad400_model_combo.blockSignals(False)
        self.madlad400_model_combo.currentTextChanged.connect(self.on_madlad400_model_changed)
        # ComboBox style removed
        self.madlad400_model_combo.setFixedWidth(130) # Fixed Width
        self.madlad400_device_combo = QComboBox()
        self.madlad400_device_combo.addItems(["GPU", "CPU"])
        self.madlad400_device_combo.blockSignals(True)
        self.madlad400_device_combo.setCurrentText("GPU")
        self.madlad400_device_combo.blockSignals(False)
        self.madlad400_device_combo.currentTextChanged.connect(self.update_madlad400_device)
        # ComboBox style removed
        self.madlad400_device_combo.setFixedWidth(80) # Fixed Width
        madlad400_layout.addWidget(self.madlad400_radio)
        madlad_colon = QLabel(":")
        madlad_colon.setFixedWidth(15)
        madlad400_layout.addWidget(madlad_colon)
        madlad400_layout.addStretch()
        # Spacer for missing backend combo
        backend_spacer = QLabel("") 
        backend_spacer.setFixedWidth(130) # Same width as backend combo
        madlad400_layout.addWidget(backend_spacer)
        madlad400_layout.addWidget(self.madlad400_model_combo)
        madlad400_layout.addStretch()
        self.madlad_device_label = QLabel(self.tr('device'))
        self.madlad_device_label.setFixedWidth(50)
        madlad400_layout.addWidget(self.madlad_device_label)
        madlad400_layout.addWidget(self.madlad400_device_combo)
        model_layout.addLayout(madlad400_layout)
        self.multilingual_model_group.setLayout(model_layout)
        main_model_layout.addWidget(self.multilingual_model_group)
        self.main_model_group.setLayout(main_model_layout)
        settings_layout.addWidget(self.main_model_group)
        # مجموعة إعدادات الخادم
        self.server_group = QGroupBox(self.tr('server_settings'))
        self.server_group.setStyleSheet("""
        # Style removed
        """)
        server_layout = QHBoxLayout()
        server_layout.setSpacing(15)
        # 1. إضافة مسافة مرنة في البداية (للدفع نحو اليسار/الوسط)
        server_layout.addStretch()
        # حقل المضيف
        self.host_label = QLabel(f"{self.tr('host')}:")
        self.host_label.setStyleSheet("""
        # Style removed
        """)
        server_layout.addWidget(self.host_label)
        self.host = QLineEdit()
        self.host.setText("127.0.0.1")
        self.host.setStyleSheet("""
        # Style removed
        """)
        # حفظ تلقائي عند تغيير المضيف
        self.host.textChanged.connect(self.save_settings_auto)
        server_layout.addWidget(self.host)
        # حقل المنفذ
        self.port_label = QLabel(f"{self.tr('port')}:")
        self.port_label.setStyleSheet("""
        # Style removed
        """)
        server_layout.addWidget(self.port_label)
        self.port = QLineEdit()
        self.port.setText("8000")
        self.port.setStyleSheet("""
        # Style removed
        """)
        # حفظ تلقائي عند تغيير المنفذ
        self.port.textChanged.connect(self.save_settings_auto)
        server_layout.addWidget(self.port)
        # 2. إضافة مسافة مرنة في النهاية (للدفع نحو اليمين/الوسط)
        server_layout.addStretch()
        self.server_group.setLayout(server_layout)
        settings_layout.addWidget(self.server_group)
        settings_layout.addStretch()
        # إضافة مسافة في الأسفل
        return settings_widget

    def on_opus_backend_changed(self):
        """معالجة تغيير خلفية OPUS-MT-en-ar"""
        # التحقق إذا كان الخادم قيد التشغيل
        if self.show_model_device_warning('opus'):
            # استعادة الخيار السابق إذا كان الخادم قيد التشغيل
            self.opus_backend_combo.blockSignals(True)
            self.opus_backend_combo.setCurrentText(self.previous_opus_backend)
            self.opus_backend_combo.blockSignals(False)
            return
        backend_name = self.opus_backend_combo.currentText()
        self.previous_opus_backend = backend_name  # حفظ القيمة الجديدة كخيار سابق
        if backend_name == "CTranslate2":
            if self.opus_radio.isChecked():
                self.backend = 'c2'
            self.opus_model_combo.clear()
            self.opus_model_combo.addItems(self.get_c2_models())
            # استعادة الجهاز السابق لـ CTranslate2
            self.opus_device_combo.setCurrentText(self.previous_c2_device)
            # تعيين مسار النموذج
            selected_model = self.opus_model_combo.currentText()
            if selected_model:
                src = self.source_lang_combo.currentText()
                tgt = self.target_lang_combo.currentText()
                self.c2_model_path = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", "CTranslate2", f"{src}-{tgt}-CTranslate2", selected_model)
        else:  # ONNX
            if self.opus_radio.isChecked():
                self.backend = 'onnx'
            self.opus_model_combo.clear()
            self.opus_model_combo.addItems(self.get_onnx_models())
            # استعادة الجهاز السابق لـ ONNX
            self.opus_device_combo.setCurrentText(self.previous_onnx_device)
            # تعيين مسار النموذج
            selected_model = self.opus_model_combo.currentText()
            if selected_model:
                src = self.source_lang_combo.currentText()
                tgt = self.target_lang_combo.currentText()
                self.onnx_model_path = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", "ONNX", f"{src}-{tgt}-ONNX", selected_model)
        self.save_settings_auto()

    def on_opus_model_changed(self):
        """معالجة تغيير نموذج OPUS"""
        # التحقق إذا كان الخادم قيد التشغيل
        if self.show_model_device_warning('opus'):
            # استعادة الخيار السابق إذا كان الخادم قيد التشغيل
            self.opus_model_combo.blockSignals(True)
            self.opus_model_combo.setCurrentText(self.previous_opus_model)
            self.opus_model_combo.blockSignals(False)
            return
        selected_model = self.opus_model_combo.currentText()
        self.previous_opus_model = selected_model  # حفظ القيمة الجديدة كخيار سابق
        if self.backend == 'c2' and selected_model:
            src = self.source_lang_combo.currentText()
            tgt = self.target_lang_combo.currentText()
            self.c2_model_path = os.path.join(self.exe_dir, "models", self.OPUS_BASE_NAME, "CTranslate2", f"{src}-{tgt}-CTranslate2", selected_model)
        elif self.backend == 'onnx' and selected_model:
            src = self.source_lang_combo.currentText()
            tgt = self.target_lang_combo.currentText()
            self.onnx_model_path = os.path.join(self.exe_dir, "models", self.OPUS_BASE_NAME, "ONNX", f"{src}-{tgt}-ONNX", selected_model)
        self.save_settings_auto()

    def initialize_model_paths(self):
        """تهيئة مسارات النماذج بناءً على الإعدادات الحالية"""
        if hasattr(self, 'opus_radio') and self.opus_radio.isChecked():
            backend_name = self.opus_backend_combo.currentText()
            selected_model = self.opus_model_combo.currentText()
            src = self.source_lang_combo.currentText()
            tgt = self.target_lang_combo.currentText()
            if backend_name == "CTranslate2" and selected_model:
                self.c2_model_path = os.path.join(self.exe_dir, "models", self.OPUS_BASE_NAME, "CTranslate2", f"{src}-{tgt}-CTranslate2", selected_model)
                self.backend = 'c2'
            elif backend_name == "ONNX" and selected_model:
                self.onnx_model_path = os.path.join(self.exe_dir, "models", self.OPUS_BASE_NAME, "ONNX", f"{src}-{tgt}-ONNX", selected_model)
                self.backend = 'onnx'

    def update_opus_device(self):
        """تحديث جهاز OPUS"""
        # التحقق إذا كان الخادم يعمل بالفعل باستخدام الدالة المركزية
        if self.show_model_device_warning('opus'):
            return
        current_device = self.opus_device_combo.currentText()
        backend_name = self.opus_backend_combo.currentText()
        if backend_name == "CTranslate2":
            self.c2_device = "cuda" if current_device == "GPU" else "cpu"
            self.previous_c2_device = current_device
        else:
            self.onnx_device = "cuda" if current_device == "GPU" else "cpu"
            self.previous_onnx_device = current_device
        self.save_settings_auto()

    def update_opus_models(self):
        """تحديث قائمة نماذج OPUS بناءً على اللغات المحددة"""
        # التحقق إذا كان الخادم يعمل بالفعل ونستخدم نماذج OPUS
        if self.model_running and hasattr(self, 'opus_radio') and self.opus_radio.isChecked():
            self.show_themed_message_box(
                QMessageBox.Warning, self.tr('warning'),
                self.tr('server_running_warning_opus_land'),
                QMessageBox.Ok
            )
            # إعادة تعيين القيم السابقة للغة
            self.source_lang_combo.blockSignals(True)
            self.target_lang_combo.blockSignals(True)
            self.source_lang_combo.setCurrentText(self.source_lang)
            self.target_lang_combo.setCurrentText(self.target_lang)
            self.source_lang_combo.blockSignals(False)
            self.target_lang_combo.blockSignals(False)
            self.save_settings_auto()
            return
        if hasattr(self, 'opus_radio'):
            backend_name = self.opus_backend_combo.currentText()
            if backend_name == "CTranslate2":
                self.opus_model_combo.clear()
                self.opus_model_combo.addItems(self.get_c2_models())
            else:
                self.opus_model_combo.clear()
                self.opus_model_combo.addItems(self.get_onnx_models())
            # تحديث مسارات النماذج
            selected_model = self.opus_model_combo.currentText()
            src = self.source_lang_combo.currentText()
            tgt = self.target_lang_combo.currentText()
            # تحديث متغيرات اللغة الحالية دائماً
            self.source_lang = src
            self.target_lang = tgt
            if selected_model:
                if backend_name == "CTranslate2":
                    self.c2_model_path = os.path.join(self.exe_dir, "models", self.OPUS_BASE_NAME, "CTranslate2", f"{src}-{tgt}-CTranslate2", selected_model)
                else:
                    self.onnx_model_path = os.path.join(self.exe_dir, "models", self.OPUS_BASE_NAME, "ONNX", f"{src}-{tgt}-ONNX", selected_model)
            # تحديث نص زر الراديو دائماً
            if src and tgt:
                opus_label = f"{self.OPUS_BASE_NAME}-{src}-{tgt}"
                self.opus_radio.setText(opus_label)
            else:
                self.opus_radio.setText(f"{self.OPUS_BASE_NAME}-UNKNOWN")
            self.save_settings_auto()

    def create_download_widget(self):
        """إنشاء ويدجت إعدادات التحميل والتحويل"""
        download_widget = QWidget()
        download_layout = QVBoxLayout(download_widget)
        download_layout.setSpacing(15)  # زيادة المسافة بين العناصر
        # مجموعة تحميل النماذج متعددة اللغات (MADLA400 في الأعلى)
        self.multilingual_download_group = QGroupBox(self.tr('download_multilingual'))
        self.multilingual_download_group.setStyleSheet("""
        # Style removed
        """)
        multilingual_layout = QVBoxLayout()
        multilingual_layout.setSpacing(10)
        # زر تحميل نموذج madlad400 مع شريط تقدم
        self.download_madlad400_btn = QPushButton(self.tr('download_madlad400'))
        self.download_madlad400_btn.setToolTip(self.tr('download_madlad400'))
        self.download_madlad400_btn.setMinimumHeight(35)
        # إنشاء شريط تقدم داخل الزر
        self.download_madlad400_progress = QProgressBar(self.download_madlad400_btn)
        self.download_madlad400_progress.setTextVisible(False)
        self.download_madlad400_progress.setRange(0, 100)
        self.download_madlad400_progress.setValue(0)
        self.download_madlad400_progress.hide()
        self.download_madlad400_btn.clicked.connect(self.download_madlad400_model)
        multilingual_layout.addWidget(self.download_madlad400_btn)
        self.multilingual_download_group.setLayout(multilingual_layout)
        download_layout.addWidget(self.multilingual_download_group)
        # تخطيط أفقي لـ OPUS (يمين) و MBARTLARGE50 (يسار)
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(15)
        # مجموعة MBARTLARGE50 (اليسار)
        self.mbartlarge50_download_group = QGroupBox("MBARTLARGE50")
        self.mbartlarge50_download_group.setStyleSheet("""
        # Style removed
        """)
        mbartlarge50_layout = QVBoxLayout()
        mbartlarge50_layout.setSpacing(12)
        # زر تحميل نموذج MBARTLARGE50 مع شريط تقدم
        self.download_mbartlarge50_btn = QPushButton(self.tr('download_mbartlarge50'))
        self.download_mbartlarge50_btn.setToolTip(self.tr('download_mbartlarge50'))
        self.download_mbartlarge50_btn.setMinimumHeight(35)
        # إنشاء شريط تقدم داخل الزر
        self.download_mbartlarge50_progress = QProgressBar(self.download_mbartlarge50_btn)
        self.download_mbartlarge50_progress.setTextVisible(False)
        self.download_mbartlarge50_progress.setRange(0, 100)
        self.download_mbartlarge50_progress.setValue(0)
        self.download_mbartlarge50_progress.hide()
        self.download_mbartlarge50_btn.clicked.connect(self.download_mbartlarge50_model)
        mbartlarge50_layout.addWidget(self.download_mbartlarge50_btn)
        # تحويل MBARTLARGE50 إلى CTranslate2
        self.mbartlarge50_c2_group = QGroupBox(self.tr('convert_c2'))
        self.mbartlarge50_c2_group.setStyleSheet("""
        # Style removed
        """)
        mbartlarge50_c2_convert_layout = QHBoxLayout()
        mbartlarge50_c2_convert_layout.setSpacing(8)
        mbartlarge50_c2_convert_layout.addStretch()
        self.mbartlarge50_c2_convert_combo = QComboBox()
        self.mbartlarge50_c2_convert_combo.addItems(["Ct2-int8", "Ct2-int8_float16", "Ct2-float16", "Ct2-bfloat16"])
        self.mbartlarge50_c2_convert_combo.setCurrentText("Ct2-int8")
        self.mbartlarge50_c2_convert_combo.setMinimumWidth(120)
        mbartlarge50_c2_convert_layout.addWidget(self.mbartlarge50_c2_convert_combo)
        self.convert_mbartlarge50_c2_btn = QPushButton(f"         {self.tr('convert_btn')}")
        # سيتم تعيين الأيقونة عبر apply_theme
        self.convert_mbartlarge50_c2_btn.setIconSize(QSize(24, 24))
        self.convert_mbartlarge50_c2_btn.setToolTip(self.tr('convert_c2'))
        self.convert_mbartlarge50_c2_btn.setMinimumHeight(30)
        # إنشاء شريط تقدم داخل الزر
        self.convert_mbartlarge50_c2_progress = QProgressBar(self.convert_mbartlarge50_c2_btn)
        self.convert_mbartlarge50_c2_progress.setTextVisible(False)
        self.convert_mbartlarge50_c2_progress.setRange(0, 100)
        self.convert_mbartlarge50_c2_progress.setValue(0)
        self.convert_mbartlarge50_c2_progress.hide()
        self.convert_mbartlarge50_c2_btn.clicked.connect(self.convert_mbartlarge50_to_c2)
        mbartlarge50_c2_convert_layout.addWidget(self.convert_mbartlarge50_c2_btn)
        mbartlarge50_c2_convert_layout.addStretch()
        self.mbartlarge50_c2_group.setLayout(mbartlarge50_c2_convert_layout)
        mbartlarge50_layout.addWidget(self.mbartlarge50_c2_group)
        # تحويل MBARTLARGE50 إلى ONNX
        self.mbartlarge50_onnx_group = QGroupBox(self.tr('convert_onnx'))
        self.mbartlarge50_onnx_group.setStyleSheet("""
        # Style removed
        """)
        mbartlarge50_onnx_convert_layout = QHBoxLayout()
        mbartlarge50_onnx_convert_layout.setSpacing(8)
        mbartlarge50_onnx_convert_layout.addStretch()
        self.mbartlarge50_onnx_convert_combo = QComboBox()
        self.mbartlarge50_onnx_convert_combo.addItems(["Onnx", "Ox-int8", "Ox-float16"])
        self.mbartlarge50_onnx_convert_combo.setCurrentText("Onnx")
        self.mbartlarge50_onnx_convert_combo.setMinimumWidth(120)
        mbartlarge50_onnx_convert_layout.addWidget(self.mbartlarge50_onnx_convert_combo)
        self.convert_mbartlarge50_onnx_btn = QPushButton(f"         {self.tr('convert_btn')}")
        self.convert_mbartlarge50_onnx_btn.setIconSize(QSize(24, 24))
        self.convert_mbartlarge50_onnx_btn.setToolTip(self.tr('convert_onnx'))
        self.convert_mbartlarge50_onnx_btn.setMinimumHeight(30)
        # إنشاء شريط تقدم داخل الزر
        self.convert_mbartlarge50_onnx_progress = QProgressBar(self.convert_mbartlarge50_onnx_btn)
        self.convert_mbartlarge50_onnx_progress.setTextVisible(False)
        self.convert_mbartlarge50_onnx_progress.setRange(0, 100)
        self.convert_mbartlarge50_onnx_progress.setValue(0)
        self.convert_mbartlarge50_onnx_progress.hide()
        self.convert_mbartlarge50_onnx_btn.clicked.connect(self.convert_mbartlarge50_to_onnx)
        mbartlarge50_onnx_convert_layout.addWidget(self.convert_mbartlarge50_onnx_btn)
        mbartlarge50_onnx_convert_layout.addStretch()
        self.mbartlarge50_onnx_group.setLayout(mbartlarge50_onnx_convert_layout)
        mbartlarge50_layout.addWidget(self.mbartlarge50_onnx_group)
        self.mbartlarge50_download_group.setLayout(mbartlarge50_layout)
        horizontal_layout.addWidget(self.mbartlarge50_download_group)
        # مجموعة OPUS-MT (اليمين)
        self.opus_download_group = QGroupBox(self.tr('opus_mt'))
        opus_layout = QVBoxLayout()
        opus_layout.setSpacing(12)
        # اختيارات لغة المصدر والهدف لنموذج OPUS الديناميكي
        self.opus_lang_download_group = QGroupBox(self.tr('select_languages'))
        lang_select_layout = QHBoxLayout()
        lang_select_layout.setSpacing(8)
        self.download_src_lang_combo = QComboBox()
        self.download_src_lang_combo.addItems(["ar", "en", "fr", "de", "es", "it", "pt", "ru", "zh", "ja", "ko"])
        self.download_src_lang_combo.setCurrentText("en")
        self.download_src_lang_combo.setMinimumWidth(70)
        self.download_tgt_lang_combo = QComboBox()
        self.download_tgt_lang_combo.addItems(["ar", "en", "fr", "de", "es", "it", "pt", "ru", "zh", "ja", "ko"])
        self.download_tgt_lang_combo.setCurrentText("ar")
        self.download_tgt_lang_combo.setMinimumWidth(70)
        lang_select_layout.addStretch()
        self.download_from_label = QLabel(self.tr('from'))
        lang_select_layout.addWidget(self.download_from_label)
        lang_select_layout.addWidget(self.download_src_lang_combo)
        self.download_to_label = QLabel(self.tr('to'))
        lang_select_layout.addWidget(self.download_to_label)
        lang_select_layout.addWidget(self.download_tgt_lang_combo)
        lang_select_layout.addStretch()
        self.opus_lang_download_group.setLayout(lang_select_layout)
        opus_layout.addWidget(self.opus_lang_download_group)
        self.download_btn = QPushButton(self.tr('download_model'))
        self.download_btn.setToolTip(self.tr('download_opus_mt_tooltip'))
        self.download_btn.setMinimumHeight(35)
        # إنشاء شريط تقدم داخل الزر
        self.download_progress = QProgressBar(self.download_btn)
        self.download_progress.setTextVisible(False)
        self.download_progress.setRange(0, 100)
        self.download_progress.setValue(0)
        self.download_progress.hide()
        self.download_btn.clicked.connect(self.download_model)
        # تهيئة نص الزر والنص التوضيحي
        self.download_src_lang_combo.currentTextChanged.connect(lambda _: self.update_download_button_text())
        self.download_tgt_lang_combo.currentTextChanged.connect(lambda _: self.update_download_button_text())
        self.update_download_button_text()
        opus_layout.addWidget(self.download_btn)
        # مجموعة تحويل OPUS إلى CTranslate2
        self.opus_c2_group = QGroupBox(self.tr('convert_c2'))
        c2_convert_layout = QHBoxLayout()
        c2_convert_layout.setSpacing(8)
        c2_convert_layout.addStretch()
        self.c2_convert_combo = QComboBox()
        self.c2_convert_combo.addItems(["Ct2-int8", "Ct2-int8_float16", "Ct2-float16", "Ct2-bfloat16"])
        self.c2_convert_combo.setCurrentText("Ct2-int8")
        self.c2_convert_combo.setMinimumWidth(120)
        c2_convert_layout.addWidget(self.c2_convert_combo)
        self.convert_c2_btn = QPushButton(f"         {self.tr('convert_btn')}")
        # سيتم تعيين الأيقونة عبر apply_theme
        self.convert_c2_btn.setIconSize(QSize(24, 24))
        self.convert_c2_btn.setToolTip(self.tr('convert_c2_tooltip'))
        self.convert_c2_btn.setMinimumHeight(30)
        # إنشاء شريط تقدم داخل الزر
        self.convert_c2_progress = QProgressBar(self.convert_c2_btn)
        self.convert_c2_progress.setTextVisible(False)
        self.convert_c2_progress.setRange(0, 100)
        self.convert_c2_progress.setValue(0)
        self.convert_c2_progress.hide()
        self.convert_c2_btn.clicked.connect(self.convert_to_c2)
        c2_convert_layout.addWidget(self.convert_c2_btn)
        c2_convert_layout.addStretch()
        self.opus_c2_group.setLayout(c2_convert_layout)
        opus_layout.addWidget(self.opus_c2_group)
        # مجموعة تحويل OPUS إلى ONNX
        self.opus_onnx_group = QGroupBox(self.tr('convert_onnx'))
        onnx_convert_layout = QHBoxLayout()
        onnx_convert_layout.setSpacing(8)
        onnx_convert_layout.addStretch()
        self.onnx_convert_combo = QComboBox()
        self.onnx_convert_combo.addItems(["Onnx", "Ox-int8", "Ox-float16"])
        self.onnx_convert_combo.setCurrentText("Onnx")
        self.onnx_convert_combo.setMinimumWidth(120)
        onnx_convert_layout.addWidget(self.onnx_convert_combo)
        self.convert_onnx_btn = QPushButton(f"         {self.tr('convert_btn')}")
        # سيتم تعيين الأيقونة عبر apply_theme
        self.convert_onnx_btn.setIconSize(QSize(24, 24))
        self.convert_onnx_btn.setToolTip(self.tr('convert_onnx_tooltip'))
        self.convert_onnx_btn.setMinimumHeight(30)
        # إنشاء شريط تقدم داخل الزر
        self.convert_onnx_progress = QProgressBar(self.convert_onnx_btn)
        self.convert_onnx_progress.setTextVisible(False)
        self.convert_onnx_progress.setRange(0, 100)
        self.convert_onnx_progress.setValue(0)
        self.convert_onnx_progress.hide()
        self.convert_onnx_btn.clicked.connect(self.convert_to_onnx)
        onnx_convert_layout.addWidget(self.convert_onnx_btn)
        onnx_convert_layout.addStretch()
        self.opus_onnx_group.setLayout(onnx_convert_layout)
        opus_layout.addWidget(self.opus_onnx_group)
        self.opus_download_group.setLayout(opus_layout)
        horizontal_layout.addWidget(self.opus_download_group)
        download_layout.addLayout(horizontal_layout)
        download_layout.addStretch()  # إضافة مسافة في النهاية
        return download_widget

    def update_download_button_text(self):
        """تحديث نص زر التحميل بناءً على لغات المصدر والهدف المحددة"""
        try:
            src = self.download_src_lang_combo.currentText()
            tgt = self.download_tgt_lang_combo.currentText()
            model_id = f"opus-mt-tc-big-{src}-{tgt}"
            self.download_btn.setText(f"⬇️ {self.tr('download_model_specific')} {model_id}")
            self.download_btn.setToolTip(f"{self.tr('download_model_tooltip')} {model_id}")
        except Exception:
            self.download_btn.setText(f"⬇️ {self.tr('download_model')}")
            self.download_btn.setToolTip(self.tr('download_model_tooltip'))

    def create_translation_widget(self):
        """إنشاء ويدجت الترجمة"""
        translation_widget = QWidget(self)
        translation_layout = QVBoxLayout(translation_widget)
        # مجموعة الترجمة
        self.translation_group = QGroupBox(self.tr('translate_text_group'))
        translation_group_layout = QVBoxLayout()
        # منطقة إدخال النص
        self.input_label = QLabel(self.tr('source_text'))
        translation_group_layout.addWidget(self.input_label)
        self.input_text = QTextEdit()
        self.input_text.setObjectName("input_text")  # تعيين اسم الكائن للاستخدام في stylesheet
        self.input_text.setAcceptRichText(False)
        self.input_text.setMinimumHeight(100)
        translation_group_layout.addWidget(self.input_text)
        # أزرار الترجمة
        buttons_layout = QHBoxLayout()
        self.translate_btn = QPushButton(self.tr('translate_btn'))
        buttons_layout.addStretch()
        self.translate_btn.clicked.connect(self.translate_text)
        self.translate_btn.setFixedSize(200, 35)
        buttons_layout.addWidget(self.translate_btn)
        self.clear_btn = QPushButton(self.tr('clear_btn'))
        self.clear_btn.clicked.connect(self.clear_text)
        self.clear_btn.setFixedSize(200, 35)
        buttons_layout.addWidget(self.clear_btn)
        translation_group_layout.addLayout(buttons_layout)
        # أداة تغيير حجم النص
        font_size_layout = QHBoxLayout()
        self.font_size_label = QLabel(self.tr('font_size'))
        font_size_layout.addStretch()
        font_size_layout.addWidget(self.font_size_label)
        self.font_size_slider = QSlider(Qt.Horizontal)
        self.font_size_slider.setMinimum(8)
        self.font_size_slider.setMaximum(32)
        self.font_size_slider.setValue(12)
        self.font_size_slider.setFixedWidth(100)
        # استخدام lambda للتأكد من تمرير القيمة بشكل صحيح
        self.font_size_slider.valueChanged.connect(lambda value: self.change_font_size(value))
        font_size_layout.addWidget(self.font_size_slider)
        self.font_size_value = QLabel("12")
        font_size_layout.addWidget(self.font_size_value)
        buttons_layout.addLayout(font_size_layout)
        # منطقة الناتج
        self.output_label = QLabel(self.tr('translation_label'))
        translation_group_layout.addWidget(self.output_label)
        self.output_text = QTextEdit()
        self.output_text.setObjectName("output_text")  # تعيين اسم الكائن للاستخدام في stylesheet
        self.output_text.setReadOnly(True)
        self.output_text.setMinimumHeight(100)
        # سيبقى التطبيق بنظام LTR دائماً
        self.output_text.setLayoutDirection(Qt.LeftToRight)
        translation_group_layout.addWidget(self.output_text)
        self.translation_group.setLayout(translation_group_layout)
        translation_layout.addWidget(self.translation_group)
        return translation_widget

    def change_font_size(self, size):
        """تغيير حجم الخط في مربعات النص"""
        self.current_font_size = size  # حفظ حجم الخط الحالي
        self.font_size_value.setText(str(size))
        font = QFont("Segoe UI", size)
        self.input_text.setFont(font)
        self.output_text.setFont(font)
        input_style = f"""
        QTextEdit#input_text {{
            font-family: 'Segoe UI', sans-serif;
            font-size: {size}pt;
        }}
        """
        output_style = f"""
        QTextEdit#output_text {{
            font-family: 'Segoe UI', sans-serif;
            font-size: {size}pt;
        }}
        """
        self.input_text.setStyleSheet(input_style)
        self.output_text.setStyleSheet(output_style)

    def set_backend(self, backend):
        """تعيين نوع النموذج المستخدم"""
        # التحقق إذا كان الخادم يعمل بالفعل
        if self.model_running:
            # إظهار رسالة تحذير بسيطة بدون خيارات
            self.show_themed_message_box(
                QMessageBox.Warning, self.tr('warning'),
                self.tr('server_running_warning'),
                QMessageBox.Ok
            )
            if self.running_model_type == 'opus':
                self.opus_radio.blockSignals(True)
                self.opus_radio.setChecked(True)
                self.opus_radio.blockSignals(False)
            elif self.running_model_type == 'madlad400':
                self.madlad400_radio.blockSignals(True)
                self.madlad400_radio.setChecked(True)
                self.madlad400_radio.blockSignals(False)
            elif self.running_model_type == 'mbartlarge50':
                self.mbartlarge50_radio.blockSignals(True)
                self.mbartlarge50_radio.setChecked(True)
                self.mbartlarge50_radio.blockSignals(False)
            return
        else:
            if backend == 'opus':
                try:
                    backend_name = self.opus_backend_combo.currentText()
                except Exception:
                    backend_name = "CTranslate2"
                if backend_name == "CTranslate2":
                    self.backend = 'c2'
                else:
                    self.backend = 'onnx'
            else:
                self.backend = backend
            # إظهار/إخفاء اختيار اللغات حسب نوع النموذج (الآن في شريط الأدوات)
            self.lang_widget.setVisible(self.backend in ['madlad400', 'mbartlarge50', 'c2', 'onnx'])
            # حفظ الإعدادات تلقائياً بعد تغيير النموذج
            self.save_settings_auto()

    def show_model_device_warning(self, related_model=None):
        """إظهار نافذة تحذير عند تغيير نوع النموذج أو الجهاز عندما يكون الخادم شغال"""
        if self.model_running:
            # التحقق مما إذا كان التغيير يخص نوع نموذج مختلف عن الذي يعمل
            current_running_type = self.running_model_type
            
            # إذا تم تقديم related_model وكان مختلفاً عما يعمل حالياً، لا تظهر تحذيراً
            if related_model and current_running_type and related_model != current_running_type:
                return False

            self.show_themed_message_box(
                QMessageBox.Warning, self.tr('Warning'),
                self.tr('server_running_warning'),
                QMessageBox.Ok
            )
            # إعادة تعيين القيمة السابقة
            self.restore_previous_selection()
            return True  # يشير إلى أن التغيير تم منعه
        return False  # يشير إلى أن التغيير مسموح

    def on_madlad400_model_changed(self, model_name):
        """معالجة تغيير نموذج  """
        if not self.show_model_device_warning('madlad400'):
            self.previous_madlad400_model = model_name
            self.save_settings_auto()

    def on_c2_model_changed(self, model_name):
        """معالجة تغيير نموذج C2"""
        if not self.show_model_device_warning('opus'):
            self.previous_c2_model = model_name
            self.save_settings_auto()

    def on_mbartlarge50_model_changed(self, model_name):
        """معالجة تغيير نموذج MBARTLARGE50"""
        if not self.show_model_device_warning('mbartlarge50'):
            self.previous_mbartlarge50_model = model_name
            self.save_settings_auto()
    def on_mbartlarge50_backend_changed(self, backend_name):
        """معالجة تغيير خلفية MBARTLARGE50"""
        if not self.show_model_device_warning('mbartlarge50'):
            if backend_name == "CTranslate2":
                self.mbartlarge50_backend = 'mbartlarge50c2'
                self.mbartlarge50_model_combo.clear()
                self.mbartlarge50_model_combo.addItems(self.get_mbartlarge50_c2_models())
            else:  # ONNX
                self.mbartlarge50_backend = 'mbartlarge50onnx'
                self.mbartlarge50_model_combo.clear()
                self.mbartlarge50_model_combo.addItems(self.get_mbartlarge50_onnx_models())
            self.save_settings_auto()

    def on_onnx_model_changed(self, model_name):
        """معالجة تغيير نموذج ONNX"""
        if not self.show_model_device_warning('opus'):
            self.previous_onnx_model = model_name
            self.save_settings_auto()

    def restore_previous_selection(self):
        """إعادة تعيين الاختيارات السابقة"""
        # إعادة تعيين القيم السابقة
        self.opus_model_combo.blockSignals(True)
        self.madlad400_model_combo.blockSignals(True)
        self.mbartlarge50_model_combo.blockSignals(True)
        self.opus_device_combo.blockSignals(True)
        self.madlad400_device_combo.blockSignals(True)
        self.mbartlarge50_device_combo.blockSignals(True)
        self.opus_model_combo.setCurrentText(self.previous_opus_model)
        self.madlad400_model_combo.setCurrentText(self.previous_madlad400_model)
        self.mbartlarge50_model_combo.setCurrentText(self.previous_mbartlarge50_model)       
        self.opus_device_combo.setCurrentText(self.previous_opus_device)
        self.madlad400_device_combo.setCurrentText(self.previous_madlad400_device)
        self.mbartlarge50_device_combo.setCurrentText(self.previous_mbartlarge50_device)
        self.opus_model_combo.blockSignals(False)
        self.madlad400_model_combo.blockSignals(False)
        self.mbartlarge50_model_combo.blockSignals(False)
        self.opus_device_combo.blockSignals(False)
        self.madlad400_device_combo.blockSignals(False)
        self.mbartlarge50_device_combo.blockSignals(False)
    def toggle_settings(self):
        """عرض/إخفاء الإعدادات"""
        is_dark = self.theme.lower() == 'dark'
        suffix = "black" if is_dark else "light"
        if not self.settings_widget.isVisible():
            self.settings_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'back_{suffix}.png')))
            self.settings_btn.setText('')
            self.download_convert_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'download_convert_{suffix}.png')))
            self.download_convert_btn.setText('')
            self.download_convert_btn.setToolTip(self.tr('download_convert'))
            self.settings_btn.setToolTip(self.tr('back'))
            self.download_widget.setVisible(False)
            self.translation_widget.setVisible(False)
            self.settings_widget.setVisible(True)
        else:
            self.settings_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'settings_{suffix}.png')))
            self.settings_btn.setText('')
            self.settings_btn.setToolTip(self.tr('settings'))
            self.settings_widget.setVisible(False)
            self.translation_widget.setVisible(True)

    def toggle_download(self):
        """عرض/إخفاء إعدادات التحميل والتحويل"""
        is_dark = self.theme.lower() == 'dark'
        suffix = "black" if is_dark else "light"
        if not self.download_widget.isVisible():
            self.download_convert_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'back_{suffix}.png')))
            self.download_convert_btn.setText('')
            self.settings_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'settings_{suffix}.png')))
            self.settings_btn.setText('')
            self.settings_btn.setToolTip(self.tr('settings'))
            self.download_convert_btn.setToolTip(self.tr('back'))
            self.settings_widget.setVisible(False)
            self.translation_widget.setVisible(False)
            self.download_widget.setVisible(True)
        else:
            self.download_convert_btn.setIcon(QIcon(os.path.join(self.exe_dir, 'icons', f'download_convert_{suffix}.png')))
            self.download_convert_btn.setText('')
            self.download_convert_btn.setToolTip(self.tr('download_convert'))
            self.download_widget.setVisible(False)
            self.translation_widget.setVisible(True)

    def change_ui_language(self, index):
        """تغيير لغة واجهة المستخدم ديناميكياً"""
        self.language = self.ui_lang_combo.itemData(index)
        # تحديث عنوان النافذة
        self.setWindowTitle(self.tr('app_title'))
        # شريط الحالة
        if not self.model_running:
            self.left_label.setText(self.tr('status_offline'))
        else:
            self.left_label.setText(self.tr('status_running'))
        # شريط الأدوات (Tooltips)
        self.run_btn.setToolTip(self.tr('run_server'))
        self.stop_btn.setToolTip(self.tr('stop_server'))
        self.download_setup_btn.setToolTip(self.tr('env_setup'))
        self.settings_btn.setToolTip(self.tr('settings'))
        self.download_convert_btn.setToolTip(self.tr('download_convert'))
        self.help_btn.setToolTip(self.tr('help'))
        self.to_label.setText(self.tr('to'))
        self.from_label.setText(self.tr('from'))
        # الإعدادات
        self.theme_group.setTitle(self.tr('appearance'))
        self.main_model_group.setTitle(self.tr('select_model'))
        self.multilingual_model_group.setTitle(self.tr('multilingual_models'))
        self.server_group.setTitle(self.tr('server_settings'))
        # تحديث المسميات في الإعدادات
        if hasattr(self, 'theme_label'): self.theme_label.setText(self.tr('select_theme'))
        if hasattr(self, 'lang_label'): self.lang_label.setText(self.tr('select_lang'))
        # ملاحظة: Labels تم حفظها في self.xxxx_label
        if hasattr(self, 'opus_device_label'): self.opus_device_label.setText(self.tr('device'))
        if hasattr(self, 'mbart_device_label'): self.mbart_device_label.setText(self.tr('device'))
        if hasattr(self, 'madlad_device_label'): self.madlad_device_label.setText(self.tr('device'))
        if hasattr(self, 'host_label'): self.host_label.setText(f"{self.tr('host')}:")
        if hasattr(self, 'port_label'): self.port_label.setText(f"{self.tr('port')}:")
        # التحميل والتحويل
        self.multilingual_download_group.setTitle(self.tr('download_multilingual'))
        self.mbartlarge50_download_group.setTitle("MBARTLARGE50") # No translation key needed for model names usually
        self.mbartlarge50_c2_group.setTitle(self.tr('convert_c2'))
        self.mbartlarge50_onnx_group.setTitle(self.tr('convert_onnx'))
        self.opus_download_group.setTitle(self.tr('opus_mt'))
        self.opus_lang_download_group.setTitle(self.tr('select_languages'))
        self.opus_c2_group.setTitle(self.tr('convert_c2'))
        self.opus_onnx_group.setTitle(self.tr('convert_onnx'))
        self.download_madlad400_btn.setText(self.tr('download_madlad400'))
        self.download_mbartlarge50_btn.setText(self.tr('download_mbartlarge50'))
        self.convert_mbartlarge50_c2_btn.setText(f"         {self.tr('convert_btn')}")
        self.convert_mbartlarge50_onnx_btn.setText(f"         {self.tr('convert_btn')}")
        self.download_from_label.setText(self.tr('from'))
        self.download_to_label.setText(self.tr('to'))
        self.download_btn.setText(self.tr('download_model'))
        self.convert_c2_btn.setText(f"         {self.tr('convert_btn')}")
        self.convert_onnx_btn.setText(f"         {self.tr('convert_btn')}")
        # الترجمة
        self.translation_group.setTitle(self.tr('translate_text_group'))
        self.input_label.setText(self.tr('source_text'))
        self.output_label.setText(self.tr('translation_label'))
        self.translate_btn.setText(self.tr('translate_btn'))
        self.clear_btn.setText(self.tr('clear_btn'))
        self.font_size_label.setText(self.tr('font_size'))
        pair_direction = Qt.RightToLeft if self.language == 'ar' else Qt.LeftToRight
        self.lang_widget.setLayoutDirection(pair_direction)
        if hasattr(self, 'opus_lang_download_group'):
            self.opus_lang_download_group.setLayoutDirection(pair_direction)
        pass

    def load_model_lists(self):
        """تحميل قوائم النماذج من المجلدات"""
        self.c2_models = self.get_c2_models()
        self.onnx_models = self.get_onnx_models()
        self.mbartlarge50_c2_models = self.get_mbartlarge50_c2_models()
        self.mbartlarge50_onnx_models = self.get_mbartlarge50_onnx_models()

    def get_c2_models(self):
        """الحصول على قائمة نماذج CTranslate2 المتاحة بناءً على لغة المصدر والهدف"""
        src = self.source_lang_combo.currentText()
        tgt = self.target_lang_combo.currentText()
        models_dir = os.path.join(self.exe_dir, 'models', "OPUS-MT-BIG", 'CTranslate2', f"{src}-{tgt}-CTranslate2")
        if not os.path.exists(models_dir):
            return []
        models = []
        try:
            for item in os.listdir(models_dir):
                item_path = os.path.join(models_dir, item)
                if os.path.isdir(item_path):
                    models.append(item)
        except Exception as e:
            print(f"خطأ في قراءة مجلد CTranslate2: {e}")
        return models
    def get_onnx_models(self):
        """الحصول على قائمة نماذج ONNX المتاحة بناءً على لغة المصدر والهدف"""
        src = self.source_lang_combo.currentText()
        tgt = self.target_lang_combo.currentText()
        models_dir = os.path.join(self.exe_dir, 'models', "OPUS-MT-BIG", 'ONNX', f"{src}-{tgt}-ONNX")
        if not os.path.exists(models_dir):
           return []
        models = []
        try:
            for item in os.listdir(models_dir):
                item_path = os.path.join(models_dir, item)
                if os.path.isdir(item_path):
                  models.append(item)
        except Exception as e:
           print(f"خطأ في قراءة مجلد ONNX: {e}")
        return models
    
    def get_mbartlarge50_c2_models(self):
        """الحصول على قائمة نماذج MBARTLARGE50 CTranslate2 المتاحة"""
        models_dir = os.path.join(self.exe_dir, 'models', 'multilingual', 'mbartlarge50', 'CTranslate2')
        if not os.path.exists(models_dir):
            return []
        models = []
        try:
            for item in os.listdir(models_dir):
                item_path = os.path.join(models_dir, item)
                if os.path.isdir(item_path):
                    models.append(item)
        except Exception as e:
            print(f"خطأ في قراءة مجلد MBARTLARGE50 CTranslate2: {e}")
        return models

    def get_mbartlarge50_onnx_models(self):
        """الحصول على قائمة نماذج MBARTLARGE50 ONNX المتاحة"""
        models_dir = os.path.join(self.exe_dir, 'models', 'multilingual', 'mbartlarge50', 'Onnx')
        if not os.path.exists(models_dir):
            return []
        models = []
        try:
            for item in os.listdir(models_dir):
                item_path = os.path.join(models_dir, item)
                if os.path.isdir(item_path):
                    models.append(item)
        except Exception as e:
            print(f"خطأ في قراءة مجلد MBARTLARGE50 ONNX: {e}")
        return models
    def load_model_paths(self):
        """تحميل مسارات النماذج من متغيرات البيئة"""
        c2_path = os.environ.get('C2_MODEL_PATH', '').strip()
        onnx_path = os.environ.get('ONNX_MODEL_PATH', '').strip()
        if c2_path:
            # استخراج اسم النموذج من المسار
            c2_model_name = os.path.basename(c2_path)
            if c2_model_name in self.c2_models:
                self.opus_model_combo.setCurrentText(c2_model_name)
            self.c2_model_path = c2_path
        if onnx_path:
            # استخراج اسم النموذج من المسار
            onnx_model_name = os.path.basename(onnx_path)
            if onnx_model_name in self.onnx_models:
                self.opus_model_combo.setCurrentText(onnx_model_name)
            self.onnx_model_path = onnx_path

    def load_settings_auto(self):
        """تحميل الإعدادات تلقائياً من ملف الإعدادات الافتراضي"""
        try:
            # البحث في عدة مواقع محتملة لملف الإعدادات
            possible_paths = [
                os.path.join(self.exe_dir, 'settings.json'),  # مجلد الـ exe (حيث قد تُحفظ الإعدادات)
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json'),  # نفس مجلد الملف
                os.path.join(os.getcwd(), 'settings.json'),  # مجلد العمل الحالي
                os.path.join(os.path.expanduser('~'), 'METranslator', 'settings.json'),  # مجلد المستخدم
            ]
            settings_loaded = False
            for path in possible_paths:
                if os.path.exists(path):
                    try:
                        # قراءة الإعدادات من الملف
                        with open(path, 'r', encoding='utf-8') as f:
                            settings = json.load(f)
                        # تطبيق الإعدادات
                        # استعادة اختيار اللغة أولاً حتى يتم تحميل قوائم النماذج المناسبة
                        self.language = settings.get('ui_language', 'ar')
                        self.ui_lang_combo.setCurrentIndex(0 if self.language == 'ar' else 1)
                        self.change_ui_language(self.ui_lang_combo.currentIndex())
                        source_lang = settings.get('source_lang', 'en')
                        target_lang = settings.get('target_lang', 'ar')
                        if source_lang in [self.source_lang_combo.itemText(i) for i in range(self.source_lang_combo.count())]:
                            self.source_lang_combo.setCurrentText(source_lang)
                        if target_lang in [self.target_lang_combo.itemText(i) for i in range(self.target_lang_combo.count())]:
                            self.target_lang_combo.setCurrentText(target_lang)
                        backend = settings.get('backend', 'c2')
                        self.backend = backend  # تحديث متغير backend
                        # استعادة إعدادات OPUS دائماً (حتى لو كان backend المحفوظ نموذج متعدد اللغات)
                        opus_backend = settings.get('opus_backend', 'CTranslate2')
                        opus_model_name = settings.get('opus_model', '')
                        opus_device = settings.get('opus_device', 'cuda')
                        # ضع قيمة الخلفية في الـ combo ثم حضّر قائمة النماذج بناءً على اللغات الحالية
                        try:
                            self.opus_backend_combo.setCurrentText(opus_backend)
                        except Exception:
                            pass
                        # تحديث قوائم النماذج (تعتمد على source/target الحالية)
                        self.load_model_lists()
                        # ملء قائمة النماذج مع إزالة التكرارات (الحفاظ على الترتيب)
                        try:
                            all_items = []
                            if opus_backend == "CTranslate2":
                                all_items = (self.c2_models or []) + (self.get_c2_models() or [])
                            else:
                                all_items = (self.onnx_models or []) + (self.get_onnx_models() or [])
                            seen = set()
                            unique_items = []
                            for it in all_items:
                                if it and it not in seen:
                                    seen.add(it)
                                    unique_items.append(it)
                            self.opus_model_combo.clear()
                            if unique_items:
                                self.opus_model_combo.addItems(unique_items)
                        except Exception:
                            # في حال حدوث أي خطأ، نترك الـ combo فارغاً
                            try:
                                self.opus_model_combo.clear()
                            except Exception:
                                pass
                        # تطبيق اختيار نموذج OPUS المحفوظ (أضفه مؤقتاً إن لم يكن موجوداً)
                        if opus_model_name:
                            try:
                                items = [self.opus_model_combo.itemText(i) for i in range(self.opus_model_combo.count())]
                            except Exception:
                                items = []
                            if opus_model_name in items:
                                self.opus_model_combo.setCurrentText(opus_model_name)
                            else:
                                self.opus_model_combo.addItem(opus_model_name)
                                self.opus_model_combo.setCurrentText(opus_model_name)
                        # تعيين الجهاز
                        try:
                            self.opus_device_combo.setCurrentText("GPU" if opus_device == "cuda" else "CPU")
                        except Exception:
                            pass
                        # تحميل الثيم
                        self.theme_combo.setCurrentText(settings.get('theme', 'dark'))
                        # احتفظ بالقيم السابقة للـ OPUS
                        self.previous_opus_backend = self.opus_backend_combo.currentText()
                        self.previous_opus_model = self.opus_model_combo.currentText()
                        self.previous_opus_device = self.opus_device_combo.currentText()
                        # إذا كان الـ backend المحفوظ فعلياً OPUS، فعين الراديو المناسب
                        if backend in ['c2', 'onnx']:
                            self.opus_radio.setChecked(True)
                            # تعيين backend الداخلي بناءً على اختيار OPUS الحالي
                            if opus_backend == "CTranslate2":
                                self.backend = 'c2'
                            else:
                                self.backend = 'onnx'
                        elif backend == 'madlad400':
                            self.madlad400_radio.setChecked(True)
                        elif backend == 'mbartlarge50':
                            self.mbartlarge50_radio.setChecked(True)
                        # تحديث قوائم النماذج
                        self.load_model_lists()
                        # تحديث combo boxes للنماذج الأخرى
                        madlad400_model_name = settings.get('madlad400_model_name', '')
                        if madlad400_model_name and madlad400_model_name in self.madlad400_models:
                            self.madlad400_model_combo.setCurrentText(madlad400_model_name)
                        mbartlarge50_backend = settings.get('mbartlarge50_backend', 'mbartlarge50c2')
                        self.mbartlarge50_backend = mbartlarge50_backend
                        if mbartlarge50_backend == 'mbartlarge50c2':
                            self.mbartlarge50_backend_combo.setCurrentText("CTranslate2")
                            self.mbartlarge50_model_combo.clear()
                            self.mbartlarge50_model_combo.addItems(self.get_mbartlarge50_c2_models())
                        elif mbartlarge50_backend == 'mbartlarge50onnx':
                            self.mbartlarge50_backend_combo.setCurrentText("ONNX")
                            self.mbartlarge50_model_combo.clear()
                            self.mbartlarge50_model_combo.addItems(self.get_mbartlarge50_onnx_models())
                        mbartlarge50_model_name = settings.get('mbartlarge50_model_name', '')
                        if mbartlarge50_model_name:
                            if mbartlarge50_backend == 'mbartlarge50c2' and mbartlarge50_model_name in self.mbartlarge50_c2_models:
                                self.mbartlarge50_model_combo.setCurrentText(mbartlarge50_model_name)
                            elif mbartlarge50_backend == 'mbartlarge50onnx' and mbartlarge50_model_name in self.mbartlarge50_onnx_models:
                                self.mbartlarge50_model_combo.setCurrentText(mbartlarge50_model_name)
                        # تحديث قوائم النماذج لـ OPUS بناءً على اللغات المحددة
                        self.load_model_lists()
                        # تحديث اختيار اللغات
                        source_lang = settings.get('source_lang', 'en')
                        target_lang = settings.get('target_lang', 'ar')
                        if source_lang in [self.source_lang_combo.itemText(i) for i in range(self.source_lang_combo.count())]:
                            self.source_lang_combo.setCurrentText(source_lang)
                        if target_lang in [self.target_lang_combo.itemText(i) for i in range(self.target_lang_combo.count())]:
                            self.target_lang_combo.setCurrentText(target_lang)
                        # تطبيق backend وتحديث قوائم النماذج أولاً
                        self.set_backend(self.backend)
                        self.load_model_lists()
                        # بعد تحديث قوائم النماذج: أعد تطبيق اختيار نموذج OPUS المحفوظ
                        if opus_model_name:
                            if opus_model_name in [self.opus_model_combo.itemText(i) for i in range(self.opus_model_combo.count())]:
                                self.opus_model_combo.setCurrentText(opus_model_name)
                            else:
                                # أضف الاسم مؤقتاً ليصبح مرئياً للمستخدم
                                self.opus_model_combo.addItem(opus_model_name)
                                self.opus_model_combo.setCurrentText(opus_model_name)                                
                        # تحديث تسمية OPUS بعد تحميل الإعدادات
                        if hasattr(self, 'opus_radio'):
                            src = self.source_lang_combo.currentText()
                            tgt = self.target_lang_combo.currentText()
                            if src and tgt:
                                opus_label = f"{self.OPUS_BASE_NAME}-{src}-{tgt}"
                                self.opus_radio.setText(opus_label)
                            else:
                                self.opus_radio.setText(f"{self.OPUS_BASE_NAME}-UNKNOWN")
                        # تحميل باقي الإعدادات
                        self.host.setText(settings.get('host', '127.0.0.1'))
                        self.port.setText(settings.get('port', '8000'))
                        # تحميل الثيم
                        self.theme = settings.get('theme', 'dark').lower()
                        # تحديث الأجهزة
                        self.madlad400_device = settings.get('madlad400_device', 'cuda')
                        self.mbartlarge50_device = settings.get('mbartlarge50_device', 'cuda')
                        self.madlad400_device_combo.setCurrentText("GPU" if self.madlad400_device == "cuda" else "CPU")
                        self.mbartlarge50_device_combo.setCurrentText("GPU" if self.mbartlarge50_device == "cuda" else "CPU")
                        # تحديث متغيرات البيئة
                        if settings.get('madlad400_model_path', ''):
                            os.environ['MADLA400_MODEL_PATH'] = settings.get('madlad400_model_path', '')
                        if settings.get('mbartlarge50_model_path', ''):
                            os.environ['MBARTLARGE50_MODEL_PATH'] = settings.get('mbartlarge50_model_path', '')
                        self.left_label.setText(self.tr('settings_loaded_auto'))
                        settings_loaded = True
                        break
                    except Exception as e:
                        print(f"خطأ في تحميل الإعدادات من {path}: {str(e)}")
                        continue
            if not settings_loaded:
                self.left_label.setText(self.tr('settings_file_not_found'))
                self.theme = 'dark'
        except Exception as e:
            # لا نعرض رسالة خطأ هنا لأن الملف قد لا يكون موجوداً في المرة الأولى
            pass
        # تطبيق الثيم في النهاية
        self.apply_theme()
     
    def update_c2_device(self, device):
        """تحديث جهاز C2"""
        if not self.show_model_device_warning('opus'):
            self.c2_device = "cuda" if device == "GPU" else "cpu"
            self.save_settings_auto()
            self.previous_c2_device = device

    def update_onnx_device(self, device):
        """تحديث جهاز ONNX"""
        if not self.show_model_device_warning('opus'):
            self.onnx_device = "cuda" if device == "GPU" else "cpu"
            self.save_settings_auto()
            self.previous_onnx_device = device

    def update_madlad400_device(self, device):
        """تحديث جهازMADLA400"""
        if not self.show_model_device_warning('madlad400'):
            self.madlad400_device = "cuda" if device == "GPU" else "cpu"
            self.save_settings_auto()
            self.previous_madlad400_device = device

    def update_mbartlarge50_device(self):
        """تحديث جهاز نموذج MBARTLARGE50"""
        # التحقق إذا كان الخادم يعمل بالفعل باستخدام الدالة المركزية
        if self.show_model_device_warning('mbartlarge50'):
            return
        current_device = self.mbartlarge50_device_combo.currentText()
        self.mbartlarge50_device = "cuda" if current_device == "GPU" else "cpu"
        self.previous_mbartlarge50_device = current_device
        self.save_settings_auto()

    def change_theme(self, new_theme):
        """معالجة تغيير الثيم فوراً"""
        self.theme = new_theme.lower()
        self.apply_theme()
        self.save_settings_auto()

    def run(self):
        """تشغيل الخادم مباشرة باستخدام الاستيراد"""
        if self.worker_thread and self.worker_thread.isRunning():
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('server_already_running'))
            return
        # التحقق من المكتبات في خيط منفصل مع مؤشر تقدم
        if self.backend == 'c2':
            device = self.c2_device
        elif self.backend == 'onnx':
            device = self.onnx_device
        elif self.backend == 'mbartlarge50':
            device = self.mbartlarge50_device
        else:  # madlad400
            device = self.madlad400_device
        # إنشاء عامل التحقق من المكتبات
        self.library_verification_worker = LibraryVerificationWorker(self.exe_dir, self.backend, device, self.language)
        self.library_verification_thread = QThread()
        self.library_verification_worker.moveToThread(self.library_verification_thread)
        # ربط الإشارات
        self.library_verification_thread.started.connect(self.library_verification_worker.run)
        self.library_verification_worker.finished.connect(self.library_verification_thread.quit)
        self.library_verification_worker.finished.connect(self.library_verification_worker.deleteLater)
        self.library_verification_thread.finished.connect(self.library_verification_thread.deleteLater)
        self.library_verification_worker.output.connect(self.update_status)
        self.library_verification_worker.success.connect(self.on_library_verification_complete)
        # بدء الخيط
        self.library_verification_thread.start()
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.library_verification_timer = QTimer()
        self.library_verification_timer.timeout.connect(self.process_events)
        self.library_verification_timer.start(100)  # كل 100 ميلي ثانية

    def on_library_verification_complete(self, success):
        """معالجة انتهاء التحقق من البيئة والمكتبات"""
        # إيقاف المؤقت
        if hasattr(self, 'library_verification_timer'):
            self.library_verification_timer.stop()
        if not success:
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('error_verifying_libraries'))
            return
        # إذا نجح التحقق، استمر في تشغيل الخادم
        self._start_server_after_verification()
   
    def _start_server_after_verification(self):
        """تشغيل الخادم بعد التحقق من المكتبات"""
        model = None
        # اختيار مسار النموذج بناءً على النموذج المحدد
        if hasattr(self, 'opus_radio') and self.opus_radio.isChecked():
            selected_model = self.opus_model_combo.currentText()
            if selected_model:
                src = self.source_lang_combo.currentText()
                tgt = self.target_lang_combo.currentText()
                if self.backend == 'c2':
                    model = os.path.join(self.exe_dir, 'models', "OPUS-MT-BIG", 'CTranslate2', f"{src}-{tgt}-CTranslate2", selected_model)
                elif self.backend == 'onnx':  # onnx
                    model = os.path.join(self.exe_dir, 'models', "OPUS-MT-BIG", 'ONNX', f"{src}-{tgt}-ONNX", selected_model)
            else:
                model = os.environ.get('OPUS_MODEL_PATH', '').strip()
                if not model:
                    self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('model_path_required'))
                    return
        elif self.backend == 'madlad400':
            model_dir = os.path.join(self.exe_dir, 'models', 'multilingual', 'madlad400')
            if os.path.exists(os.path.join(model_dir, "model.bin")):
                model = model_dir
            else:
                self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('model_must_be_downloaded'))
                return
        elif self.backend == 'mbartlarge50':
            selected_model = self.mbartlarge50_model_combo.currentText()
            backend_for_server = None
            if selected_model:
                if self.mbartlarge50_backend == 'mbartlarge50c2':
                    model = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50", "CTranslate2", selected_model)
                    backend_for_server = 'mbartlarge50c2'
                else:  # onnx
                    model = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50", "Onnx", selected_model)
                    backend_for_server = 'mbartlarge50onnx'
                    if "CTranslate2" in model:
                        model = model.replace("CTranslate2", "Onnx")
            else:
                model = os.environ.get('MBARTLARGE50_MODEL_PATH', '').strip()
                if not model:
                    self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('model_path_required'))
                    return
                backend_for_server = self.mbartlarge50_backend if self.mbartlarge50_backend in ("mbartlarge50c2", "mbartlarge50onnx") else self.mbartlarge50_backend
        else:
            model = None
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('model_path_required'))
            return
        # تحديث شريط الحالة بعد التحقق من وجود النموذج
        self.left_label.setText(self.tr('server_starting'))
        host = _sanitize(self.host.text()) or '127.0.0.1'
        port = _sanitize(self.port.text()) or '8000'
        self.server_url = f'http://{host}:{port}'
        # تسجيل المعلومات
        self.left_label.setText(f"{self.tr('model_msg')}: {self.backend.upper()}")
        self.left_label.setText(f"{self.tr('host_msg')}: {host}")
        self.left_label.setText(f"{self.tr('port_msg')}: {port}")
        # التأكد من إيقاف أي خيط قديم قبل إنشاء خيط جديد
        if hasattr(self, 'worker_thread') and self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait(3000)  # انتظر حتى 3 ثوانٍ
            if self.worker_thread.isRunning():
                self.worker_thread.terminate()
                self.worker_thread.wait(1000)  # انتظر ثانية واحدة بعد الإنهاء القسري
        effective_backend = locals().get('backend_for_server', self.backend)
        if effective_backend == 'c2':
            device = self.c2_device
        elif effective_backend == 'onnx':
            device = self.onnx_device
        elif effective_backend.startswith('mbartlarge50') or self.backend == 'mbartlarge50':
            device = self.mbartlarge50_device
        else:  # madlad400
            device = self.madlad400_device
        # مرر الخلفية الفعلية إلى العامل بدل تغيير الحالة العامة للتطبيق
        self.worker = ServerWorkerDirect(effective_backend, model, host, port, device, lang=self.language)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        # ربط الإشارات
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.cleanup)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker.output.connect(self.update_status)
        self.worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.worker_thread.start()
        self.model_running = True
        
        # تعيين نوع النموذج الذي يعمل
        if self.backend in ['c2', 'onnx']:
            self.running_model_type = 'opus'
        elif self.backend == 'madlad400':
            self.running_model_type = 'madlad400'
        elif self.backend == 'mbartlarge50':
            self.running_model_type = 'mbartlarge50'
            
        self.worker_thread_active = True
        self.left_label.setText(self.tr('server_starting'))
        # تحديث التسمية الوسطى بمعلومات النموذج
        if self.backend == 'c2':
            device = self.c2_device
            self.center_label.setText(f"{self.tr('opus_mt_c2')} ({device})")
        elif self.backend == 'onnx':
            device = self.onnx_device
            self.center_label.setText(f"{self.tr('opus_mt_onnx')} ({device})")
        elif self.backend == 'madlad400':
            device = self.madlad400_device
            self.center_label.setText(f"{self.tr('madlad400_model')} ({device})")
        elif self.backend == 'mbartlarge50':
            device = self.mbartlarge50_device
            self.center_label.setText(f"{self.tr('mbartlarge50_model')} ({device})")      # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.process_events)
        self.progress_timer.start(100)  # كل 100 ميلي ثانية
        # تعطيل زر إيقاف الخادم وأزرار التحميل والتحويل عند بدء تشغيل الخادم
        self.download_btn.setEnabled(False)
        self.download_madlad400_btn.setEnabled(False)
        self.download_mbartlarge50_btn.setEnabled(False)
        self.convert_c2_btn.setEnabled(False)
        self.convert_onnx_btn.setEnabled(False)
        self.convert_mbartlarge50_c2_btn.setEnabled(False)
        self.convert_mbartlarge50_onnx_btn.setEnabled(False)

    def update_status(self, message):
        """تحديث شريط الحالة"""
        # قائمة الرسائل التي يجب تجاهلها
        ignore_list = [
            "pkg_resources is deprecated",
            "import pkg_resources",
            "is_causal = is_causal.item()",
            "FutureWarning: functools.partial",
            "self._normalized_config =",
            "TracerWarning",
            "inverted_mask =",
            "is_causal =",
            "Passing a tuple of `past_key_values` is deprecated",
            "if sequence_length != 1:",
            "if self.keys is None",
            "Moving the following attributes in the config to the generation config: {'max_length': 200, 'early_stopping': True, 'num_beams': 5}. You are seeing this warning because you've set generation parameters in the model config, as opposed to in the generation config",
            "Could not find any ONNX files with standard file name decoder_model_merged.onnx, files found: [WindowsPath('decoder_model.onnx'), WindowsPath('decoder_with_past_model.onnx'), WindowsPath('encoder_model.onnx')]. Please make sure to pass a `file_name` and/or `subfolder` argument to `from_pretrained` when loading an ONNX file with non-standard file names.",
            "failed to read a buffer of size 262144000 at position 237",
            "incomplete metadata, file not fully covered",
            "The model weights have been automatically converted to use the int8_float32 compute type instead.",
            "Skip loading CUDA and cuDNN DLLs since torch is imported.",
        ]
        
        for ignore_msg in ignore_list:
            if ignore_msg in message:
                return
        #print(f"{self.tr('DEBUG')}: {message}")
        self.left_label.setText(f"{self.tr('status')}: {message}")
        # التحقق إذا كانت الرسالة تشير إلى تحميل النموذج بنجاح
        if "loaded successfully" in message or "تم تحميل النموذج بنجاح" in message:
            self.left_label.setText(self.tr('server_started_successfully'))
            self.server_fully_loaded = True
            # تفعيل زر الترجمة عند تحميل النموذج بنجاح
            self.translate_btn.setEnabled(True)
            # إعادة تفعيل زر إيقاف الخادم عند تحميل النموذج بنجاح
            self.stop_btn.setEnabled(True)
            # أزرار التحميل والتحويل تبقى معطلة حتى إيقاف الخادم
            # إيقاف مؤقتات التقدم عند اكتمال التحميل
            if hasattr(self, 'progress_timer'):
                self.progress_timer.stop()
            if hasattr(self, 'download_timer'):
                self.download_timer.stop()
            if hasattr(self, 'convert_c2_timer'):
                self.convert_c2_timer.stop()
            if hasattr(self, 'convert_onnx_timer'):
                self.convert_onnx_timer.stop()

    def update_progress(self, value):
        """تحديث شريط التقدم"""
        self.center_label.setText(f"{self.tr('loading')}... {value}%")

    def process_events(self):
        """ضخ الأحداث بشكل دوري لمنع تجمد الواجهة"""
        QApplication.processEvents()

    def stop(self):
        """إيقاف الخادم وتحرير الذاكرة"""
        if self.worker_thread_active:
            try:
                # تعطيل الأزرار مؤقتاً
                self.run_btn.setEnabled(False)
                self.stop_btn.setEnabled(False)
                # مسح التسمية الوسطى
                self.center_label.setText('')
                # إرسال طلب إيقاف للخادم إذا كان العامل لا يزال نشطاً
                if hasattr(self, 'worker') and self.worker:
                    try:
                        import requests
                        requests.post(f"{self.server_url}/shutdown", timeout=1)
                    except:
                        pass
                # إنهاء الخيط بأمان
                if hasattr(self, 'worker_thread') and self.worker_thread:
                    # إرسال إشارة إيقاف للعامل
                    if hasattr(self, 'worker') and self.worker:
                        try:
                            # إذا كان لدى العامل دالة stop_process، استدعها
                            if hasattr(self.worker, 'stop_process'):
                                self.worker.stop_process()
                        except Exception as e:
                            pass
                    # فصل إشارة الحذف التلقائي لمنع حذف الكائن أثناء الانتظار
                    try:
                        self.worker_thread.finished.disconnect(self.worker_thread.deleteLater)
                    except Exception:
                        pass
                    # إنهاء الخيط
                    self.worker_thread.quit()
                    # انتظار أطول للتأكد من انتهاء الخيط مع معالجة الأحداث
                    wait_time = 0
                    max_wait = 5000  # 5 ثواني
                    while not self.worker_thread.isFinished() and wait_time < max_wait:
                        QApplication.processEvents()  # معالجة الأحداث لمنع التجمد
                        time.sleep(0.01)  # انتظار قصير
                        wait_time += 10
                    if not self.worker_thread.isFinished():
                        self.left_label.setText(self.tr('warning_thread_timeout'))
                        # إذا لم ينتهِ الخيط، محاولة إنهائه بالقوة
                        self.worker_thread.terminate()
                        wait_time = 0
                        while not self.worker_thread.isFinished() and wait_time < 2000:
                            QApplication.processEvents()  # معالجة الأحداث
                            time.sleep(0.01)
                            wait_time += 10
                        if not self.worker_thread.isFinished():
                            self.left_label.setText(self.tr('warning_thread_termination_failed'))
                    # الحذف اليدوي الآمن بعد انتهاء كل شيء
                    self.worker_thread.deleteLater()
                # تحرير الذاكرة بشكل صريح
                import gc
                gc.collect()  # تشغيل جامع القمامة
                # إعادة تعيين المتغيرات الكبيرة
                if hasattr(self, 'worker'):
                    self.worker = None
                if hasattr(self, 'worker_thread'):
                    self.worker_thread = None
                # تحرير الذاكرة مرة أخرى
                gc.collect()  # تشغيل جامع القمامة مرة أخرى
                self.model_running = False
                self.running_model_type = None
                self.worker_thread_active = False
                self.server_fully_loaded = False
                self.translate_btn.setEnabled(False)
                self.left_label.setText(self.tr('server_stopped_successfully'))
                # مسح زمن الاستجابة عند إيقاف الخادم
                self.right_label.setText('')
                self.translation_time = 0.0
                # إعادة تفعيل أزرار التحميل والتحويل عند إيقاف الخادم
                self.download_btn.setEnabled(True)
                self.download_madlad400_btn.setEnabled(True)
                self.download_mbartlarge50_btn.setEnabled(True)
                self.convert_c2_btn.setEnabled(True)
                self.convert_onnx_btn.setEnabled(True)
                self.convert_mbartlarge50_c2_btn.setEnabled(True)
                self.convert_mbartlarge50_onnx_btn.setEnabled(True)
                self.convert_mbartlarge50_c2_btn.setEnabled(True)
                self.convert_mbartlarge50_onnx_btn.setEnabled(True)
            except Exception as e:
                # التعامل مع الأخطاء
                self.left_label.setText(f"{self.tr('error_stopping_server')}: {str(e)}")
                self.model_running = False
                self.worker_thread_active = False
                # محاولة تحرير الذاكرة حتى في حالة وجود خطأ
                try:
                    import gc
                    gc.collect()
                except:
                    pass
            finally:
                # إعادة تفعيل الأزرار
                self.run_btn.setEnabled(True)
                self.stop_btn.setEnabled(True)
                # إيقاف جميع مؤقتات التقدم
                if hasattr(self, 'progress_timer'):
                    self.progress_timer.stop()
                if hasattr(self, 'download_timer'):
                    self.download_timer.stop()
                if hasattr(self, 'download_mbartlarge50_timer'):
                    self.download_mbartlarge50_timer.stop()
                if hasattr(self, 'convert_c2_timer'):
                    self.convert_c2_timer.stop()
                if hasattr(self, 'convert_onnx_timer'):
                    self.convert_onnx_timer.stop()
                if hasattr(self, 'convert_mbartlarge50_c2_timer'):
                    self.convert_mbartlarge50_c2_timer.stop()
                if hasattr(self, 'convert_mbartlarge50_onnx_timer'):
                    self.convert_mbartlarge50_onnx_timer.stop()
                if hasattr(self, 'library_verification_timer'):
                    self.library_verification_timer.stop()
                if hasattr(self, 'library_verification_timer'):
                    self.library_verification_timer.stop()
        else:
            self.left_label.setText(self.tr('server_not_active'))
        # إعادة تعيين المراجع لتجنب الوصول إلى كائنات محذوفة
        if hasattr(self, 'worker_thread'):
            self.worker_thread = None
        if hasattr(self, 'worker'):
            self.worker = None

    def save_settings_auto(self):
        """حفظ الإعدادات تلقائياً في ملف الإعدادات الافتراضي"""
        try:
            # البحث في عدة مواقع محتملة لملف الإعدادات
            possible_paths = [
                os.path.join(self.exe_dir, 'settings.json'),  # مجلد الـ exe
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json'),  # نفس مجلد الملف
                os.path.join(os.getcwd(), 'settings.json'),  # مجلد العمل الحالي
                os.path.join(os.path.expanduser('~'), 'METranslator', 'settings.json'),  # مجلد المستخدم
            ]
            # تحديد المسار الذي سيتم حفظ الإعدادات فيه
            save_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    save_path = path
                    break
            # إذا لم يتم العثور على ملف موجود، استخدم المسار الأول
            if not save_path:
                save_path = possible_paths[0]
                # تأكد من وجود المجلد
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
            # الحصول على القيم الحالية من الواجهة
            opus_backend = self.opus_backend_combo.currentText()
            opus_model_name = self.opus_model_combo.currentText()
            opus_device = "cuda" if self.opus_device_combo.currentText() == "GPU" else "cpu"
            mbartlarge50_model_name = self.mbartlarge50_model_combo.currentText()
            # بناء المسارات الكاملة بناءً على اللغات المحددة
            src = self.source_lang_combo.currentText()
            tgt = self.target_lang_combo.currentText()
            if opus_backend == "CTranslate2":
                opus_path = os.path.join(self.exe_dir, 'models', "OPUS-MT-BIG", 'CTranslate2', f"{src}-{tgt}-CTranslate2", opus_model_name) if opus_model_name else ""
            else:  # ONNX
                opus_path = os.path.join(self.exe_dir, 'models', "OPUS-MT-BIG", 'ONNX', f"{src}-{tgt}-ONNX", opus_model_name) if opus_model_name else ""
            if self.mbartlarge50_backend == "mbartlarge50c2":
                mbartlarge50_path = os.path.join(self.exe_dir, 'models', 'multilingual', 'mbartlarge50', 'CTranslate2', mbartlarge50_model_name) if mbartlarge50_model_name else ""
            else:  # mbartlarge50onnx
                mbartlarge50_path = os.path.join(self.exe_dir, 'models', 'multilingual', 'mbartlarge50', 'Onnx', mbartlarge50_model_name) if mbartlarge50_model_name else ""
            madlad400_path = os.path.join(self.exe_dir, 'models', 'multilingual', 'madlad400')
            # الحفاظ على القيم الحالية أو استخدام القيم الجديدة
            settings = {
                'backend': self.backend,
                'opus_backend': opus_backend,
                'opus_model': opus_model_name,
                'opus_device': opus_device,
                'opus_model_path': opus_path,
                'madlad400_model_name': self.madlad400_model_combo.currentText(),
                'mbartlarge50_model_name': self.mbartlarge50_model_combo.currentText(),
                'mbartlarge50_backend': self.mbartlarge50_backend,
                'madlad400_model_path': madlad400_path,
                'mbartlarge50_model_path': mbartlarge50_path,
                'madlad400_device': self.madlad400_device,
                'mbartlarge50_device': self.mbartlarge50_device,
                'host': self.host.text(),
                'port': self.port.text(),
                'source_lang': self.source_lang_combo.currentText(),
                'target_lang': self.target_lang_combo.currentText(),
                'theme': self.theme_combo.currentText(),
                'ui_language': self.language
            }
            # حفظ الإعدادات في الملف المحدد
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
            self.left_label.setText(self.tr('settings_saved_auto'))
        except Exception as e:
            self.left_label.setText(f"{self.tr('settings_save_failed')}: {str(e)}")

    def translate_text(self):
        """ترجمة النص من الإنجليزية إلى العربية"""
        if not self.model_running:
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('server_not_active_translation_warning'))
            return
        if not self.server_fully_loaded:
            self.show_themed_message_box(QMessageBox.Information, self.tr('wait'), self.tr('server_loading_wait_warning'))
            return
        # التحقق من وجود عملية ترجمة قيد التشغيل بالفعل
        if self.translation_in_progress:
            reply = self.show_themed_message_box(QMessageBox.Question, self.tr('alert'),
                self.tr('translation_in_progress_cancel_new'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                self.cancel_translation()
            else:
                return
        text = self.input_text.toPlainText().strip()
        if not text:
            self.show_themed_message_box(QMessageBox.Warning, self.tr('warning'), self.tr('enter_text_to_translate'))
            return
        try:
            # مسح النص الحالي
            self.output_text.clear()
            # تعطيل زر الترجمة مؤقتاً
            self.translate_btn.setEnabled(False)
            self.translate_btn.setText(self.tr("translating_in_progress"))
            # مسح زمن الاستجابة من الترجمة السابقة
            self.right_label.setText('')
            # إنشاء عامل الترجمة وخيط منفصل
            if self.backend == 'madlad400':
                # للنموذجMADLA400، إرسال اللغات المحددة
                source_lang = self.source_lang_combo.currentText()
                target_lang = self.target_lang_combo.currentText()
                self.translation_worker = TranslationWorker(self.server_url, text, source_lang, target_lang, lang=self.language)
            elif self.backend == 'mbartlarge50' or self.backend == 'mbartlarge50onnx' or self.backend == 'mbartlarge50c2':
                # للنموذج MBARTLARGE50، إرسال اللغات المحددة
                source_lang = self.source_lang_combo.currentText()
                target_lang = self.target_lang_combo.currentText()
                self.translation_worker = TranslationWorker(self.server_url, text, source_lang, target_lang, lang=self.language)
            else:
                # للنماذج الأخرى، استخدام الإعدادات الافتراضية
                self.translation_worker = TranslationWorker(self.server_url, text, lang=self.language)
            self.translation_thread = threading.Thread(target=self.translation_worker.run)
            # ربط الإشارات
            self.translation_worker.result.connect(self.display_translation_result)
            self.translation_worker.error.connect(self.handle_translation_error)
            self.translation_worker.progress.connect(self.update_translation_progress)
            self.translation_worker.status_update.connect(self.update_status)
            self.translation_worker.time_taken.connect(self.update_translation_time)
            # بدء الخيط
            self.translation_thread.start()
            self.translation_in_progress = True
            self.left_label.setText(self.tr('translation_started_background'))
        except Exception as e:
            # إعادة تفعيل زر الترجمة في حالة وجود خطأ
            self.translate_btn.setEnabled(True)
            self.translate_btn.setText(self.tr("translate_btn"))
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), f"{self.tr('failed_to_start_translation')}: {str(e)}")
    
    def on_translation_error(self, message):
        self.translation_in_progress = False
        self.left_label.setText(f"{self.tr('translation_error')}: {message}")
        self.center_label.setText('')
    
    def cancel_translation(self):
        """إلغاء عملية الترجمة الحالية"""
        if self.translation_in_progress and self.translation_worker:
            self.translation_worker.stop()
            self.left_label.setText(self.tr('cancelling_translation'))
            self.right_label.setText('')  # مسح زمن الاستجابة
            # انتظار انتهاء الخيط
            if self.translation_thread:
                self.translation_thread.join()
            # إعادة تعيين الحالة
            self.translation_in_progress = False
            self.translation_worker = None
            self.translation_thread = None
            # إعادة تفعيل زر الترجمة
            self.translate_btn.setEnabled(True)
            self.translate_btn.setText(self.tr("translate_btn"))
            self.left_label.setText(self.tr('translation_cancelled'))
    
    def display_translation_result(self, translation):
        """عرض نتيجة الترجمة"""
        self.display_mixed_text(translation)
        self.left_label.setText(self.tr('translation_successful'))
        # إعادة تفعيل زر الترجمة
        self.translate_btn.setEnabled(True)
        self.translate_btn.setText(self.tr("translate_btn"))
        # إعادة تعيين الحالة
        self.translation_in_progress = False
        self.translation_worker = None
        self.translation_thread = None
    
    def handle_translation_error(self, error_message):
        """معالجة أخطاء الترجمة"""
        self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), error_message)
        # إعادة تفعيل زر الترجمة
        self.translate_btn.setEnabled(True)
        self.translate_btn.setText(self.tr("translate_btn"))
        # إعادة تعيين الحالة
        self.translation_in_progress = False
        self.translation_worker = None
        self.translation_thread = None
        self.right_label.setText('')  # مسح زمن الاستجابة في حالة الخطأ
    
    def update_translation_progress(self, current, total):
        """تحديث شريط التقدم للترجمة"""
        progress_percent = int((current / total) * 100)
        self.left_label.setText(f"{self.tr('translating_progress')} {current}/{total} ({progress_percent}%)")

    def update_translation_time(self, time):
        """تحديث زمن الترجمة"""
        self.translation_time = time
        self.right_label.setText(f"{self.tr('response_time')}: {time:.2f} {self.tr('seconds')}")

    def display_mixed_text(self, text):
        """عرض النص المختلط بين العربية والإنجليزية"""
        # مسح النص الحالي
        self.output_text.clear()
        # ضبط اتجاه النص من اليمين إلى اليسار (للغة العربية)
        self.output_text.setLayoutDirection(Qt.RightToLeft)
        # تطبيق حجم الخط المخصص على الويدجت بالكامل
        font = QFont('Segoe UI', self.current_font_size)
        self.output_text.setFont(font)
        # أيضاً تطبيق stylesheet للتأكد
        output_style = f"""
        QTextEdit#output_text {{
            font-family: 'Segoe UI', sans-serif;
            font-size: {self.current_font_size}pt;
        }}
        """
        self.output_text.setStyleSheet(output_style)
        # إدراج النص ببساطة
        self.output_text.setPlainText(text)

    def clear_text(self):
        """مسح النصوص"""
        # إلغاء أي عملية ترجمة جارية
        if self.translation_in_progress:
            reply = self.show_themed_message_box(QMessageBox.Question, self.tr('alert'),
                self.tr('translation_in_progress_cancel'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                self.cancel_translation()
            else:
                return
        self.input_text.clear()
        self.output_text.clear()
        self.left_label.setText(self.tr('text_fields_cleared'))

    def download_model(self):
        """تحميل النموذج opus-mt-tc-big-en-ar مباشرة باستخدام الاستيراد"""
        if self.download_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('download_in_progress_warning'))
            return
        src = self.download_src_lang_combo.currentText() if hasattr(self, 'download_src_lang_combo') else 'en'
        tgt = self.download_tgt_lang_combo.currentText() if hasattr(self, 'download_tgt_lang_combo') else 'ar'
        model_id = f"Helsinki-NLP/opus-mt-tc-big-{src}-{tgt}"
        # تأكيد التحميل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            self.tr('confirm_download_msg'),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحميل مؤقتاً
        self.download_btn.setEnabled(False)
        self.download_btn.setText(self.tr("downloading_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(self.tr("downloading_in_progress"))
        self.download_progress.setGeometry(5, self.download_btn.height() - 10, self.download_btn.width() - 10, 5)
        self.download_progress.show()
        self.download_progress.setValue(0)
        # إنشاء عامل التحميل وخيط منفصل
        self.download_worker = ModelDownloadWorker(self.exe_dir, model_id, lang=self.language)
        self.download_thread = QThread()
        self.download_worker.moveToThread(self.download_thread)
        # ربط الإشارات
        self.download_thread.started.connect(self.download_worker.run)
        self.download_worker.progress.connect(self.download_progress.setValue)
        self.download_worker.finished.connect(self.download_thread.quit)
        self.download_worker.finished.connect(self.download_worker.deleteLater)
        self.download_thread.finished.connect(self.download_thread.deleteLater)
        self.download_worker.finished.connect(lambda: self.download_progress.hide())
        self.download_worker.output.connect(self.update_status)
        self.download_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.download_thread.start()
        self.download_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.download_timer = QTimer()
        self.download_timer.timeout.connect(self.process_events)
        self.download_timer.start(100)  # كل 100 ميلي ثانية
        self.download_worker.finished.connect(self.download_finished)

    def download_madlad400_model(self):
        """تحميل نموذج madlad400 متعدد اللغات"""
        if self.download_madlad400_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('download_in_progress_warning'))
            return
        # تم إزالة التحقق المباشر من المكتبات لتجنب قفل الملفات
        # تأكيد التحميل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            self.tr('download_madlad400_confirm'),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحميل مؤقتاً
        self.download_madlad400_btn.setEnabled(False)
        self.download_madlad400_btn.setText(self.tr("downloading_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(self.tr('downloading_madlad400_model'))
        # عرض شريط التقدم
        self.download_madlad400_progress.setGeometry(5, self.download_madlad400_btn.height() - 10, self.download_madlad400_btn.width() - 10, 5)
        self.download_madlad400_progress.show()
        self.download_madlad400_progress.setValue(0)
        # إنشاء عامل التحميل وخيط منفصل
        self.download_madlad400_worker = Madlad400DownloadWorker(self.exe_dir, lang=self.language)
        self.download_madlad400_thread = QThread()
        self.download_madlad400_worker.moveToThread(self.download_madlad400_thread)
        # ربط الإشارات
        self.download_madlad400_thread.started.connect(self.download_madlad400_worker.run)
        self.download_madlad400_worker.progress.connect(self.download_madlad400_progress.setValue)
        self.download_madlad400_worker.finished.connect(self.download_madlad400_thread.quit)
        self.download_madlad400_worker.finished.connect(self.download_madlad400_worker.deleteLater)
        self.download_madlad400_thread.finished.connect(self.download_madlad400_thread.deleteLater)
        self.download_madlad400_worker.finished.connect(lambda: self.download_madlad400_progress.hide())
        self.download_madlad400_worker.output.connect(self.update_status)
        self.download_madlad400_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.download_madlad400_thread.start()
        self.download_madlad400_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.download_madlad400_timer = QTimer()
        self.download_madlad400_timer.timeout.connect(self.process_events)
        self.download_madlad400_timer.start(100)  # كل 100 ميلي ثانية
        self.download_madlad400_worker.finished.connect(self.download_madlad400_finished)

    def download_madlad400_finished(self):
        """معالجة انتهاء عملية تحميل madlad400"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.download_madlad400_btn.setEnabled(True)
        self.download_madlad400_in_progress = False
        self.left_label.setText(self.tr('download_finished_msg'))
        self.download_madlad400_btn.setText(self.tr('download_madlad400'))
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('download_madlad400_success'))
        # إيقاف المؤقت
        if hasattr(self, 'download_madlad400_timer'):
            self.download_madlad400_timer.stop()

    def download_mbartlarge50_model(self):
        """تحميل نموذج mbartlarge50 متعدد اللغات"""
        if self.download_mbartlarge50_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('download_in_progress_warning'))
            return
        # تأكيد التحميل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            self.tr('download_mbartlarge50_confirm'),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحميل مؤقتاً
        self.download_mbartlarge50_btn.setEnabled(False)
        self.download_mbartlarge50_btn.setText(self.tr("downloading_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(self.tr('downloading_mbartlarge50_model'))
        # عرض شريط التقدم
        self.download_mbartlarge50_progress.setGeometry(5, self.download_mbartlarge50_btn.height() - 10, self.download_mbartlarge50_btn.width() - 10, 5)
        self.download_mbartlarge50_progress.show()
        self.download_mbartlarge50_progress.setValue(0)
        # إنشاء عامل التحميل وخيط منفصل
        self.download_mbartlarge50_worker = MBARTLARGE50DownloadWorker(self.exe_dir, lang=self.language)
        self.download_mbartlarge50_thread = QThread()
        self.download_mbartlarge50_worker.moveToThread(self.download_mbartlarge50_thread)
        # ربط الإشارات
        self.download_mbartlarge50_thread.started.connect(self.download_mbartlarge50_worker.run)
        self.download_mbartlarge50_worker.progress.connect(self.download_mbartlarge50_progress.setValue)
        self.download_mbartlarge50_worker.finished.connect(self.download_mbartlarge50_thread.quit)
        self.download_mbartlarge50_worker.finished.connect(self.download_mbartlarge50_worker.deleteLater)
        self.download_mbartlarge50_thread.finished.connect(self.download_mbartlarge50_thread.deleteLater)
        self.download_mbartlarge50_worker.finished.connect(lambda: self.download_mbartlarge50_progress.hide())
        self.download_mbartlarge50_worker.output.connect(self.update_status)
        self.download_mbartlarge50_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.download_mbartlarge50_thread.start()
        self.download_mbartlarge50_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.download_mbartlarge50_timer = QTimer()
        self.download_mbartlarge50_timer.timeout.connect(self.process_events)
        self.download_mbartlarge50_timer.start(100)  # كل 100 ميلي ثانية
        self.download_mbartlarge50_worker.finished.connect(self.download_mbartlarge50_finished)

    def download_mbartlarge50_finished(self):
        """معالجة انتهاء عملية تحميل mbartlarge50"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.download_mbartlarge50_btn.setEnabled(True)
        self.download_mbartlarge50_in_progress = False
        self.left_label.setText(self.tr('download_finished_msg'))
        self.download_mbartlarge50_btn.setText(self.tr('download_mbartlarge50'))
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('download_mbartlarge50_success'))
        # إيقاف المؤقت
        if hasattr(self, 'download_mbartlarge50_timer'):
            self.download_mbartlarge50_timer.stop()

    def download_finished(self):
        """معالجة انتهاء عملية التحويل إلى C2"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.download_btn.setEnabled(True)
        # إعادة تعيين نص الزر حسب الاختيارات الحالية
        try:
            self.update_download_button_text()
        except Exception:
            self.download_btn.setText(self.tr("download_opus_model"))
        self.download_in_progress = False
        self.left_label.setText(self.tr('download_finished_msg'))
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('download_success_msg'))
        self.load_model_lists()
        # إيقاف المؤقت
        if hasattr(self, 'download_timer'):
            self.download_timer.stop()

    def convert_to_c2(self):
        """تحويل النموذج إلى صيغة CTranslate2 المحددة مباشرة باستخدام الاستيراد"""
        if self.convert_c2_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('conversion_in_progress_warning'))
            return
        # تحديد نموذج المصدر بناءً على اختيارات التحميل (أو الافتراض en->ar)
        src = self.download_src_lang_combo.currentText() if hasattr(self, 'download_src_lang_combo') else 'en'
        tgt = self.download_tgt_lang_combo.currentText() if hasattr(self, 'download_tgt_lang_combo') else 'ar'
        model_folder = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", f"opus-mt-tc-big-{src}-{tgt}")
        if not os.path.exists(model_folder):
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), f"{self.tr('original_model_not_found')}: {os.path.basename(model_folder)}. {self.tr('download_model_first')}")
            return
        # الحصول على نوع التحويل المحدد
        conversion_type = self.c2_convert_combo.currentText()
        pass
        # تأكيد التحويل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            f"{self.tr('convert_model_to_format_confirm')} {conversion_type}؟ {self.tr('may_take_time')}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحويل مؤقتاً
        self.convert_c2_btn.setEnabled(False)
        self.convert_c2_btn.setText(self.tr("converting_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(f"{self.tr('converting_model_to')} {conversion_type}...")
        self.convert_c2_progress.setGeometry(5, self.convert_c2_btn.height() - 10, self.convert_c2_btn.width() - 10, 5)
        self.convert_c2_progress.show()
        self.convert_c2_progress.setValue(0)
        # إنشاء عامل التحويل وخيط منفصل
        self.convert_c2_worker = ConvertToOPUSC2Worker(self.exe_dir, conversion_type, model_folder, lang=self.language)
        self.convert_c2_thread = QThread()
        self.convert_c2_worker.moveToThread(self.convert_c2_thread)
        # ربط الإشارات
        self.convert_c2_thread.started.connect(self.convert_c2_worker.run)
        self.convert_c2_worker.progress.connect(self.convert_c2_progress.setValue)
        self.convert_c2_worker.finished.connect(self.convert_c2_thread.quit)
        self.convert_c2_worker.finished.connect(self.convert_c2_worker.deleteLater)
        self.convert_c2_thread.finished.connect(self.convert_c2_thread.deleteLater)
        self.convert_c2_worker.finished.connect(lambda: self.convert_c2_progress.hide())
        self.convert_c2_worker.output.connect(self.update_status)
        self.convert_c2_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.convert_c2_thread.start()
        self.convert_c2_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.convert_c2_timer = QTimer()
        self.convert_c2_timer.timeout.connect(self.process_events)
        self.convert_c2_timer.start(100)  # كل 100 ميلي ثانية
        # ربط إشارة انتهاء التحويل لإعادة تفعيل الزر
        self.convert_c2_worker.finished.connect(self.on_convert_c2_finished)

    def on_convert_c2_finished(self):
        """معالجة انتهاء عملية التحويل إلى C2"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.convert_c2_btn.setEnabled(True)
        self.convert_c2_in_progress = False
        self.left_label.setText(self.tr('conversion_finished_msg'))
        self.convert_c2_btn.setText(f"         {self.tr('convert_btn')}")
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('conversion_c2_success'))
        # إيقاف المؤقت
        if hasattr(self, 'convert_c2_timer'):
            self.convert_c2_timer.stop()
        # إعادة تحميل قوائم النماذج وتحديث القوائم المنسدلة
        self.load_model_lists()
        if self.backend == 'c2':
            self.opus_model_combo.clear()
            self.opus_model_combo.addItems(self.c2_models)
        else:  # ONNX
            self.opus_model_combo.clear()
            self.opus_model_combo.addItems(self.onnx_models)

    def convert_to_onnx(self):
        """تحويل النموذج إلى صيغة ONNX المحددة مباشرة باستخدام الاستيراد"""
        if self.convert_onnx_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('conversion_in_progress_warning'))
            return
        # تحديد نموذج المصدر بناءً على اختيارات التحميل (أو الافتراض en->ar)
        src = self.download_src_lang_combo.currentText() if hasattr(self, 'download_src_lang_combo') else 'en'
        tgt = self.download_tgt_lang_combo.currentText() if hasattr(self, 'download_tgt_lang_combo') else 'ar'
        model_folder = os.path.join(self.exe_dir, "models", "OPUS-MT-BIG", f"opus-mt-tc-big-{src}-{tgt}")
        if not os.path.exists(model_folder):
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), f"{self.tr('original_model_not_found')}: {os.path.basename(model_folder)}. {self.tr('download_model_first')}")
            return
        # الحصول على نوع التحويل المحدد
        conversion_type = self.onnx_convert_combo.currentText()
        pass
        # تأكيد التحويل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            f"{self.tr('convert_model_to_format_confirm')} {conversion_type}؟ {self.tr('may_take_time')}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحويل مؤقتاً
        self.convert_onnx_btn.setEnabled(False)
        self.convert_onnx_btn.setText(self.tr("converting_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(f"{self.tr('converting_model_to')} {conversion_type}...")
        # عرض شريط التقدم
        self.convert_onnx_progress.setGeometry(5, self.convert_onnx_btn.height() - 10, self.convert_onnx_btn.width() - 10, 5)
        self.convert_onnx_progress.show()
        self.convert_onnx_progress.setValue(0)
        # إنشاء عامل التحويل وخيط منفصل
        self.convert_onnx_worker = ConvertToONNXWorker(self.exe_dir, conversion_type, model_folder, lang=self.language)
        self.convert_onnx_thread = QThread()
        self.convert_onnx_worker.moveToThread(self.convert_onnx_thread)
        # ربط الإشارات
        self.convert_onnx_thread.started.connect(self.convert_onnx_worker.run)
        self.convert_onnx_worker.progress.connect(self.convert_onnx_progress.setValue)
        self.convert_onnx_worker.finished.connect(self.convert_onnx_thread.quit)
        self.convert_onnx_worker.finished.connect(self.convert_onnx_worker.deleteLater)
        self.convert_onnx_thread.finished.connect(self.convert_onnx_thread.deleteLater)
        self.convert_onnx_worker.finished.connect(lambda: self.convert_onnx_progress.hide())
        self.convert_onnx_worker.output.connect(self.update_status)
        self.convert_onnx_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.convert_onnx_thread.start()
        self.convert_onnx_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.convert_onnx_timer = QTimer()
        self.convert_onnx_timer.timeout.connect(self.process_events)
        self.convert_onnx_timer.start(100)  # كل 100 ميلي ثانية
        # ربط إشارة انتهاء التحويل لإعادة تفعيل الزر
        self.convert_onnx_worker.finished.connect(self.on_convert_onnx_finished)

    def on_convert_onnx_finished(self):
        """معالجة انتهاء عملية التحويل إلى ONNX"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.convert_onnx_btn.setEnabled(True)
        self.convert_onnx_in_progress = False
        self.left_label.setText(self.tr('conversion_finished_msg'))
        self.convert_onnx_btn.setText(f"         {self.tr('convert_btn')}")
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('conversion_onnx_success'))
        # إيقاف المؤقت
        if hasattr(self, 'convert_onnx_timer'):
            self.convert_onnx_timer.stop()
        # إعادة تحميل قوائم النماذج وتحديث القوائم المنسدلة
        self.load_model_lists()
        if self.backend == 'onnx':
            self.opus_model_combo.clear()
            self.opus_model_combo.addItems(self.onnx_models)
        else:  # C2
            self.opus_model_combo.clear()
            self.opus_model_combo.addItems(self.c2_models)

    def convert_mbartlarge50_to_c2(self):
        """تحويل نموذج MBARTLARGE50 إلى صيغة CTranslate2 المحددة مباشرة باستخدام الاستيراد"""
        if self.convert_mbartlarge50_c2_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('conversion_in_progress_warning'))
            return
        # التحقق من وجود النموذج الأصلي
        model_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50")
        if not os.path.exists(model_path):
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('mbartlarge50_original_model_not_found'))
            return
        # الحصول على نوع التحويل المحدد
        conversion_type = self.mbartlarge50_c2_convert_combo.currentText()
        pass
        # تأكيد التحويل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            f"{self.tr('convert_mbartlarge50_to_format_confirm')} {conversion_type}؟ {self.tr('may_take_time')}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحويل مؤقتاً
        self.convert_mbartlarge50_c2_btn.setEnabled(False)
        self.convert_mbartlarge50_c2_btn.setText(self.tr("converting_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(f"{self.tr('converting_mbartlarge50_to')} {conversion_type}...")
        self.convert_mbartlarge50_c2_progress.setGeometry(5, self.convert_mbartlarge50_c2_btn.height() - 10, self.convert_mbartlarge50_c2_btn.width() - 10, 5)
        self.convert_mbartlarge50_c2_progress.show()
        self.convert_mbartlarge50_c2_progress.setValue(0)
        # إنشاء عامل التحويل وخيط منفصل
        self.convert_mbartlarge50_c2_worker = ConvertToMBARTLARGE50C2Worker(self.exe_dir, conversion_type, lang=self.language)
        self.convert_mbartlarge50_c2_thread = QThread()
        self.convert_mbartlarge50_c2_worker.moveToThread(self.convert_mbartlarge50_c2_thread)
        # ربط الإشارات
        self.convert_mbartlarge50_c2_thread.started.connect(self.convert_mbartlarge50_c2_worker.run)
        self.convert_mbartlarge50_c2_worker.progress.connect(self.convert_mbartlarge50_c2_progress.setValue)
        self.convert_mbartlarge50_c2_worker.finished.connect(self.convert_mbartlarge50_c2_thread.quit)
        self.convert_mbartlarge50_c2_worker.finished.connect(self.convert_mbartlarge50_c2_worker.deleteLater)
        self.convert_mbartlarge50_c2_thread.finished.connect(self.convert_mbartlarge50_c2_thread.deleteLater)
        self.convert_mbartlarge50_c2_worker.finished.connect(lambda: self.convert_mbartlarge50_c2_progress.hide())
        self.convert_mbartlarge50_c2_worker.output.connect(self.update_status)
        self.convert_mbartlarge50_c2_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.convert_mbartlarge50_c2_thread.start()
        self.convert_mbartlarge50_c2_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.convert_mbartlarge50_c2_timer = QTimer()
        self.convert_mbartlarge50_c2_timer.timeout.connect(self.process_events)
        self.convert_mbartlarge50_c2_timer.start(100)  # كل 100 ميلي ثانية
        # ربط إشارة انتهاء التحويل لإعادة تفعيل الزر
        self.convert_mbartlarge50_c2_worker.finished.connect(self.on_convert_mbartlarge50_c2_finished)

    def on_convert_mbartlarge50_c2_finished(self):
        """معالجة انتهاء عملية التحويل MBARTLARGE50 إلى C2"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.convert_mbartlarge50_c2_btn.setEnabled(True)
        self.convert_mbartlarge50_c2_in_progress = False
        self.left_label.setText(self.tr('conversion_finished_msg'))
        self.convert_mbartlarge50_c2_btn.setText(f"         {self.tr('convert_btn')}")
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('conversion_mbartlarge50_c2_success'))
        # إيقاف المؤقت
        if hasattr(self, 'convert_mbartlarge50_c2_timer'):
            self.convert_mbartlarge50_c2_timer.stop()
        # إعادة تحميل قوائم النماذج وتحديث القوائم المنسدلة
        self.load_model_lists()
        self.mbartlarge50_model_combo.clear()
        self.mbartlarge50_model_combo.addItems(self.mbartlarge50_c2_models)

    def convert_mbartlarge50_to_onnx(self):
        """تحويل نموذج MBARTLARGE50 إلى صيغة ONNX المحددة مباشرة باستخدام الاستيراد"""
        if self.convert_mbartlarge50_onnx_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('conversion_in_progress_warning'))
            return
        # التحقق من وجود النموذج الأصلي
        model_path = os.path.join(self.exe_dir, "models", "multilingual", "mbartlarge50")
        if not os.path.exists(model_path):
            self.show_themed_message_box(QMessageBox.Critical, self.tr('error'), self.tr('mbartlarge50_original_model_not_found'))
            return
        # الحصول على نوع التحويل المحدد
        conversion_type = self.mbartlarge50_onnx_convert_combo.currentText()
        pass
        # تأكيد التحويل
        reply = self.show_themed_message_box(QMessageBox.Question, self.tr('confirm'),
            f"{self.tr('convert_mbartlarge50_to_format_confirm')} {conversion_type}؟ {self.tr('may_take_time')}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر التحويل مؤقتاً
        self.convert_mbartlarge50_onnx_btn.setEnabled(False)
        self.convert_mbartlarge50_onnx_btn.setText(self.tr("converting_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(f"{self.tr('converting_mbartlarge50_to')} {conversion_type}...")
        # عرض شريط التقدم
        self.convert_mbartlarge50_onnx_progress.setGeometry(5, self.convert_mbartlarge50_onnx_btn.height() - 10, self.convert_mbartlarge50_onnx_btn.width() - 10, 5)
        self.convert_mbartlarge50_onnx_progress.show()
        self.convert_mbartlarge50_onnx_progress.setValue(0)
        # إنشاء عامل التحويل وخيط منفصل
        self.convert_mbartlarge50_onnx_worker = ConvertToMBARTLARGE50ONNXWorker(self.exe_dir, conversion_type, lang=self.language)
        self.convert_mbartlarge50_onnx_thread = QThread()
        self.convert_mbartlarge50_onnx_worker.moveToThread(self.convert_mbartlarge50_onnx_thread)
        # ربط الإشارات
        self.convert_mbartlarge50_onnx_thread.started.connect(self.convert_mbartlarge50_onnx_worker.run)
        self.convert_mbartlarge50_onnx_worker.progress.connect(self.convert_mbartlarge50_onnx_progress.setValue)
        self.convert_mbartlarge50_onnx_worker.finished.connect(self.convert_mbartlarge50_onnx_thread.quit)
        self.convert_mbartlarge50_onnx_worker.finished.connect(self.convert_mbartlarge50_onnx_worker.deleteLater)
        self.convert_mbartlarge50_onnx_thread.finished.connect(self.convert_mbartlarge50_onnx_thread.deleteLater)
        self.convert_mbartlarge50_onnx_worker.finished.connect(lambda: self.convert_mbartlarge50_onnx_progress.hide())
        self.convert_mbartlarge50_onnx_worker.output.connect(self.update_status)
        self.convert_mbartlarge50_onnx_worker.progress.connect(self.update_progress)
        # بدء الخيط
        self.convert_mbartlarge50_onnx_thread.start()
        self.convert_mbartlarge50_onnx_in_progress = True
        # إضافة مؤقت لضخ الأحداث بشكل دوري
        self.convert_mbartlarge50_onnx_timer = QTimer()
        self.convert_mbartlarge50_onnx_timer.timeout.connect(self.process_events)
        self.convert_mbartlarge50_onnx_timer.start(100)  # كل 100 ميلي ثانية
        # ربط إشارة انتهاء التحويل لإعادة تفعيل الزر
        self.convert_mbartlarge50_onnx_worker.finished.connect(self.on_convert_mbartlarge50_onnx_finished)

    def on_convert_mbartlarge50_onnx_finished(self):
        """معالجة انتهاء عملية التحويل MBARTLARGE50 إلى ONNX"""
        # إعادة تفعيل الزر في الخيط الرئيسي
        self.convert_mbartlarge50_onnx_btn.setEnabled(True)
        self.convert_mbartlarge50_onnx_in_progress = False
        self.left_label.setText(self.tr('conversion_finished_msg'))
        self.convert_mbartlarge50_onnx_btn.setText(f"         {self.tr('convert_btn')}")
        self.show_themed_message_box(QMessageBox.Information, self.tr('success'), self.tr('conversion_mbartlarge50_onnx_success'))
        # إيقاف المؤقت
        if hasattr(self, 'convert_mbartlarge50_onnx_timer'):
            self.convert_mbartlarge50_onnx_timer.stop()
        # إعادة تحميل قوائم النماذج وتحديث القوائم المنسدلة
        self.load_model_lists()
        self.mbartlarge50_model_combo.clear()
        self.mbartlarge50_model_combo.addItems(self.mbartlarge50_onnx_models)

    def open_setup_dialog(self):
        """فتح نافذة إعداد البيئة"""
        if self.setup_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('setup_in_progress_warning'))
            return
        # التحقق من الوجود المسبق للمكونات
        self._check_existing_components()
        # إنشاء نافذة الحوار
        self.setup_dialog = QDialog(self)
        self.setup_dialog.setWindowTitle(self.tr('environment_setup_title'))
        self.setup_dialog.setModal(True)
        self.setup_dialog.setFixedSize(450, 450)
        # تخطيط النافذة
        layout = QVBoxLayout(self.setup_dialog)
        # عنوان
        title_label = QLabel(self.tr('portable_environment_setup_title'))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title_label)
        # مجموعة اختيار نوع المتطلبات
        requirements_group = QGroupBox(self.tr("requirements_type_group"))
        requirements_layout = QVBoxLayout()
        self.cpu_radio = QRadioButton(self.tr("cpu_requirements"))
        self.cpu_radio.setChecked(True)
        self.gpu_radio = QRadioButton(self.tr("gpu_requirements"))
        requirements_layout.addWidget(self.cpu_radio)
        requirements_layout.addWidget(self.gpu_radio)
        requirements_group.setLayout(requirements_layout)
        layout.addWidget(requirements_group)
        # خيارات الإعداد
        options_group = QGroupBox(self.tr("setup_options_group"))
        options_layout = QVBoxLayout()
        self.install_python_checkbox = QCheckBox(self.tr("install_python_local"))
        self.install_python_checkbox.setChecked(not self.python_installed)
        self.install_python_checkbox.setEnabled(not self.python_installed)
        if self.python_installed:
            self.install_python_checkbox.setText(self.tr("install_python_local_installed"))
        self.install_python_checkbox.setToolTip(self.tr("install_python_local_tooltip"))
        self.create_venv_checkbox = QCheckBox(self.tr("create_virtual_environment"))
        self.create_venv_checkbox.setChecked(not self.venv_created)
        self.create_venv_checkbox.setEnabled(not self.venv_created)  # دائماً متاح
        if self.venv_created:
            self.create_venv_checkbox.setText(self.tr("create_virtual_environment_created"))
        self.create_venv_checkbox.setToolTip(self.tr("create_virtual_environment_tooltip"))
        # خيار إعادة إنشاء البيئة الافتراضية
        self.recreate_venv_checkbox = QCheckBox(self.tr("recreate_virtual_environment"))
        self.recreate_venv_checkbox.setChecked(False)
        self.recreate_venv_checkbox.setEnabled(self.venv_created)
        self.recreate_venv_checkbox.setToolTip(self.tr("recreate_virtual_environment_tooltip"))
        self.recreate_venv_checkbox.setVisible(self.venv_created)
        self.install_requirements_checkbox = QCheckBox(self.tr("install_requirements"))
        self.install_requirements_checkbox.setChecked(True)  # دائماً متاح للإعادة التثبيت
        self.install_requirements_checkbox.setToolTip(self.tr("install_requirements_tooltip"))
        options_layout.addWidget(self.install_python_checkbox)
        options_layout.addWidget(self.create_venv_checkbox)
        if self.venv_created:
            options_layout.addWidget(self.recreate_venv_checkbox)
        options_layout.addWidget(self.install_requirements_checkbox)
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        # منطقة الإخراج
        self.setup_output_text = QTextEdit()
        self.setup_output_text.setReadOnly(True)
        self.setup_output_text.setMaximumHeight(120)
        layout.addWidget(self.setup_output_text)
        # شريط التقدم
        self.setup_progress_bar = QProgressBar()
        self.setup_progress_bar.setRange(0, 100)
        self.setup_progress_bar.setValue(0)
        self.setup_progress_bar.setTextVisible(True)
        self.setup_progress_bar.setFormat("%p%")
        # تمت إزالة الـ hardcoded style ليستخدم الستايل العام من apply_theme
        layout.addWidget(self.setup_progress_bar)
        # أزرار التحكم
        buttons_layout = QHBoxLayout()
        self.start_setup_btn = QPushButton(self.tr("start_setup_btn"))
        self.start_setup_btn.clicked.connect(self.start_setup)
        buttons_layout.addWidget(self.start_setup_btn)
        cancel_btn = QPushButton(self.tr("cancel_btn"))
        cancel_btn.clicked.connect(self.cancel_setup)
        buttons_layout.addWidget(cancel_btn)
        layout.addLayout(buttons_layout)
        # عرض النافذة
        self.apply_dark_title_bar(self.setup_dialog)
        self.setup_dialog.exec()

    def start_setup(self):
        """بدء عملية إعداد البيئة"""
        if self.setup_in_progress:
            self.show_themed_message_box(QMessageBox.Information, self.tr('info'), self.tr('setup_in_progress_warning'))
            return
        # جمع الخيارات المحددة
        requirements_type = 'gpu' if self.gpu_radio.isChecked() else 'cpu'
        install_python = self.install_python_checkbox.isChecked()
        create_venv = self.create_venv_checkbox.isChecked()
        recreate_venv = self.recreate_venv_checkbox.isChecked() if hasattr(self, 'recreate_venv_checkbox') else False
        install_reqs = self.install_requirements_checkbox.isChecked()
        # التحقق من صحة الخيارات
        if not (install_python or create_venv or install_reqs):
            self.show_themed_message_box(QMessageBox.Warning, self.tr('warning'), self.tr('select_at_least_one_option'))
            return
        # التحقق من المتطلبات المتبادلة
        if create_venv and not (install_python or self.python_installed):
            self.show_themed_message_box(QMessageBox.Warning, self.tr('warning'), self.tr('cannot_create_venv_without_python'))
            return
        if install_reqs and not (create_venv or self.venv_created):
            self.show_themed_message_box(QMessageBox.Warning, self.tr('warning'), self.tr('cannot_install_reqs_without_venv'))
            return
        # تأكيد البدء بناءً على الخيار المحدد
        if recreate_venv:
            confirm_msg = self.tr('confirm_recreate_venv')
        else:
            confirm_msg = self.tr('confirm_start_setup')

        reply = self.show_themed_message_box(
            QMessageBox.Question, self.tr('confirm'),
            confirm_msg,
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )
        if reply != QMessageBox.Yes:
            return
        # تعطيل زر البدء
        self.start_setup_btn.setEnabled(False)
        self.start_setup_btn.setText(self.tr("setting_up_in_progress"))
        # تحديث شريط الحالة
        self.left_label.setText(self.tr('setting_up_environment'))
        # تشغيل العملية باستخدام QThread و Worker (النمط الصحيح)
        # إنشاء عامل الإعداد
        self.setup_worker = SetupWorker(
            requirements_type, install_python, create_venv, recreate_venv, install_reqs, self.exe_dir, self.language
        )
        self.setup_thread = QThread()
        self.setup_worker.moveToThread(self.setup_thread)
        # ربط الإشارات
        self.setup_thread.started.connect(self.setup_worker.run)
        self.setup_worker.output.connect(self.update_setup_output)
        self.setup_worker.progress.connect(self.update_setup_progress)
        self.setup_worker.finished.connect(self.setup_thread.quit)
        self.setup_worker.finished.connect(self.setup_worker.deleteLater)
        self.setup_thread.finished.connect(self.setup_thread.deleteLater)
        self.setup_thread.finished.connect(self.on_setup_finished)
        # ربط إشارة التنظيف
        self.setup_worker.request_cleanup.connect(self.kill_all_subprocesses)
        # بدء الخيط
        self.setup_thread.start()
        self.setup_in_progress = True
        # إعداد مؤقت لتحديث الواجهة (لضمان الاستجابة)
        self.setup_timer = QTimer()
        self.setup_timer.timeout.connect(self._ensure_ui_responsive)
        self.setup_timer.start(100)

    def cancel_setup(self):
        """إلغاء عملية إعداد البيئة"""
        if self.setup_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('confirm'),
                self.tr('confirm_cancel_setup'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                if self.setup_worker:
                    self.setup_worker.stop_process()
                self.setup_in_progress = False
                if hasattr(self, 'setup_dialog') and self.setup_dialog:
                    self.setup_dialog.reject()
        else:
            if hasattr(self, 'setup_dialog') and self.setup_dialog:
                self.setup_dialog.reject()

    def update_setup_output(self, message):
        """تحديث إخراج نافذة الإعداد"""
        if hasattr(self, 'setup_output_text') and self.setup_output_text:
            self.setup_output_text.append(message)
        # أيضاً تحديث شريط الحالة الرئيسي
        self.left_label.setText(message)
    
    def update_setup_progress(self, value):
        """تحديث شريط التقدم في نافذة الإعداد"""
        if hasattr(self, 'setup_progress_bar') and self.setup_progress_bar:
            self.setup_progress_bar.setValue(value)
            # التأكد من تحديث الواجهة فوراً
            QApplication.processEvents()
    
    def _ensure_ui_responsive(self):
        """ضمان استجابة الواجهة أثناء عملية الإعداد"""
        QApplication.processEvents()

    def on_setup_finished(self):
        """معالجة انتهاء عملية الإعداد"""
        self.setup_in_progress = False
        self.left_label.setText(self.tr('environment_setup_finished'))
        # إيقاف مؤقت تحديث الواجهة
        if hasattr(self, 'setup_timer') and self.setup_timer:
            self.setup_timer.stop()
        # إعادة تفعيل زر البدء إذا كانت النافذة لا تزال مفتوحة
        if hasattr(self, 'start_setup_btn') and self.start_setup_btn:
            self.start_setup_btn.setEnabled(True)
            self.start_setup_btn.setText(self.tr("start_setup_btn"))
        # إعادة تفعيل زر الإعداد في الشريط الرئيسي
        self.download_setup_btn.setEnabled(True)
        # إعادة التحقق من المكونات المثبتة
        self._check_existing_components()

    def _check_existing_components(self):
        """التحقق من وجود المكونات المثبتة مسبقاً"""
        import os
        # التحقق من بايثون
        python_exe = os.path.join(self.exe_dir, 'python_runtime', 'python.exe')
        self.python_installed = os.path.exists(python_exe)
        # التحقق من البيئة الافتراضية
        venv_dir = os.path.join(self.exe_dir, 'venv')
        self.venv_created = os.path.exists(venv_dir)
        # التحقق من المتطلبات (بشكل أساسي)
        pip_exe = os.path.join(self.exe_dir, 'venv', 'Scripts', 'pip.exe')
        self.requirements_installed = os.path.exists(pip_exe)

    def closeEvent(self, event):
        """معالجة حدث إغلاق النافذة وتحرير الذاكرة"""
        # إلغاء أي عملية تحميل جارية
        if self.download_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('download_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                self.download_worker.stop_process()
                self.download_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية تحميل madlad400 جارية
        if self.download_madlad400_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('download_madlad400_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                self.download_madlad400_worker.stop_process()
                self.download_madlad400_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية تحويل إلى C2 جارية
        if self.convert_c2_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('convert_c2_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                if self.convert_c2_worker:
                    self.convert_c2_worker.stop_process()
                self.convert_c2_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية تحويل إلى ONNX جارية
        if self.convert_onnx_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('convert_onnx_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                if self.convert_onnx_worker:
                    self.convert_onnx_worker.stop_process()
                self.convert_onnx_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية تحويل MBARTLARGE50 إلى C2 جارية
        if self.convert_mbartlarge50_c2_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('convert_mbart_c2_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                if self.convert_mbartlarge50_c2_worker:
                    self.convert_mbartlarge50_c2_worker.stop_process()
                self.convert_mbartlarge50_c2_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية تحويل MBARTLARGE50 إلى ONNX جارية
        if self.convert_mbartlarge50_onnx_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('convert_mbart_onnx_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                if self.convert_mbartlarge50_onnx_worker:
                    self.convert_mbartlarge50_onnx_worker.stop_process()
                self.convert_mbartlarge50_onnx_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية إعداد البيئة جارية
        if self.setup_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('setup_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                self.setup_worker.stop_process()
                self.setup_in_progress = False
            else:
                event.ignore()
                return
        # إلغاء أي عملية تحقق من المكتبات جارية
        try:
            if hasattr(self, 'library_verification_thread') and self.library_verification_thread and self.library_verification_thread.isRunning():
                reply = self.show_themed_message_box(
                    QMessageBox.Question, self.tr('alert'),
                    self.tr('verification_in_progress_exit_warning'),
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
                )
                if reply == QMessageBox.Yes:
                    self.library_verification_thread.quit()
                    self.library_verification_thread.wait()
                else:
                    event.ignore()
                    return
        except RuntimeError:
            pass
        # إلغاء أي عملية ترجمة جارية
        if self.translation_in_progress:
            reply = self.show_themed_message_box(
                QMessageBox.Question, self.tr('alert'),
                self.tr('translation_in_progress_exit_warning'),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
                self.cancel_translation()
            else:
                event.ignore()
                return
        if self.worker_thread_active:
            # إيقاف الخادم بشكل غير متزامن
            self.stop()
            event.accept()
        event.accept()

    def kill_all_subprocesses(self):
        """إنهاء جميع العمليات الفرعية قسرياً"""
        print("DEBUG: Killing all subprocesses for cleanup...")
        # 1. إيقاف الخادم
        if hasattr(self, 'server_fully_loaded') and self.server_fully_loaded:
             # محاولة إغلاق نظيف أولاً via HTTP
            try:
                import requests
                requests.post(f"{self.server_url}/shutdown", timeout=1)
            except: pass
        # 2. إيقاف وإلغاء جميع العمال
        workers_to_stop = [
            'worker', # ServerWorkerDirect
            'download_worker',
            'download_madlad400_worker',
            'download_mbartlarge50_worker',
            'convert_c2_worker',
            'convert_onnx_worker',
            'convert_mbartlarge50_c2_worker',
            'convert_mbartlarge50_onnx_worker',
            'translation_worker',
            'library_verification_worker'
        ]
        for worker_name in workers_to_stop:
            if hasattr(self, worker_name):
                worker = getattr(self, worker_name)
                if worker:
                    if hasattr(worker, 'stop_process'):
                        try: worker.stop_process()
                        except: pass
                    elif hasattr(worker, 'stop'):
                        try: worker.stop()
                        except: pass
                    # إذا كان للعمال عملية process مباشرة (مثل الفئات القديمة)
                    if hasattr(worker, 'process') and worker.process:
                        try:
                            worker.process.terminate()
                            import time
                            time.sleep(0.1)
                            if worker.process.poll() is None:
                                worker.process.kill()
                        except: pass
        # 3. تنظيف Threads
        # لا ننتظر الـ threads هنا لأننا نريد الإسراع، فقط نطلب منها التوقف
        threads_to_stop = [
            'worker_thread',
            'download_thread',
            'download_madlad400_thread',
            'download_mbartlarge50_thread',
            'convert_c2_thread',
            'convert_onnx_thread',
            'convert_mbartlarge50_c2_thread',
            'convert_mbartlarge50_onnx_thread',
            'translation_thread',
            'library_verification_thread'
        ]
        for thread_name in threads_to_stop:
            if hasattr(self, thread_name):
                thread = getattr(self, thread_name)
                if thread and thread.isRunning():
                    thread.quit()
        # 4. تنظيف sys.path من مسارات venv التي قد تكون أضيفت
        try:
            exe_dir = get_application_path()
            venv_base = os.path.join(exe_dir, 'venv').lower()
            # إنشاء قائمة جديدة خالية من مسارات venv
            clean_path = [p for p in sys.path if venv_base not in os.path.abspath(p).lower()]
            sys.path[:] = clean_path
            print("DEBUG: sys.path cleaned")
        except Exception as e:
            print(f"DEBUG: Error cleaning sys.path: {e}")
        # 5. Force garbage collection
        import gc
        gc.collect()

if __name__ == '__main__':
    myappid = 'mettranslator.7.0'  # استخدم سلسلة فريدة لتطبيقك
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(get_application_path(), 'icons', 'MET.ico')))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
