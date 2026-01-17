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

# Add the application directory to sys.path
app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)
import threading
import time
import subprocess
try:
    from PySide6.QtCore import QObject, Signal
except ImportError:
    class QObject: pass
    def Signal(*args): return None
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
from translations import TRANSLATIONS

def tr_static(lang, key):
    """دالة ترجمة ثابتة لاستخدامها داخل كلاس ServerWorkerDirect"""
    try:
        return TRANSLATIONS.get(lang, TRANSLATIONS['ar']).get(key, key)
    except:
        return key

def get_application_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def is_port_in_use(host, port):
    import socket
    try:
        port = int(port)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            return result == 0
    except Exception as e:
        return False

class ServerWorkerDirect(QObject):
    finished = Signal()
    output = Signal(str)
    progress = Signal(int)
    
    def __init__(self, backend, model_path, host, port, device, lang='ar'):
        super().__init__()
        self.backend = backend
        self.model_path = model_path
        self.host = host
        self.port = port
        self.device = device
        self.lang = lang
        self.should_run = True
        self.process = None

    def stop_process(self):
        self.should_run = False
        try:
            import requests
            requests.post(f"http://{self.host}:{self.port}/shutdown", timeout=1)
        except:
            pass
        if self.process:
            try:
                self.process.terminate()
                try:
                    self.process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    self.process.kill()
            except:
                pass
            self.process = None

    def cleanup(self):
        self.stop_process()

    def run(self):
        try:
            # انتظار حتى يصبح المنفذ متاحاً
            while is_port_in_use(self.host, self.port):
                self.output.emit(f"Port {self.port} is busy, waiting...")
                for _ in range(10):
                    if not self.should_run: return
                    time.sleep(0.1)
            exe_dir = get_application_path()
            python_exe = os.path.join(exe_dir, 'venv', 'Scripts', 'python.exe')
            if not os.path.exists(python_exe):
                python_exe = sys.executable
            script_path = os.path.abspath(__file__)
            cmd = [
                python_exe,
                "-u",
                script_path,
                '--backend', self.backend,
                '--model_path', self.model_path,
                '--host', str(self.host),
                '--port', str(self.port),
                '--device', self.device
            ]
            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "utf-8"
            self.output.emit(tr_static(self.lang, 'server_starting'))
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, 
                env=env,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
                bufsize=0
            )
            def drain_stderr():
                try:
                    for line in iter(self.process.stderr.readline, b''):
                        pass
                except:
                    pass
            threading.Thread(target=drain_stderr, daemon=True).start()
            for line_bytes in iter(self.process.stdout.readline, b''):
                if not self.should_run:
                    break
                line = line_bytes.decode('utf-8', errors='replace').strip()
                if line:
                    self.output.emit(line)
            if self.process:
                self.process.wait()
                if self.process.returncode != 0 and self.should_run:
                    self.output.emit(f"Server stopped unexpectedly (Code {self.process.returncode})")
        except Exception as e:
            self.output.emit(f"{tr_static(self.lang, 'status_error')}: {str(e)}")
            import traceback
            self.output.emit(str(traceback.format_exc()))
        finally:
            self.finished.emit()

def run_server_standalone(backend, model_path, host, port, device):
    pass
    if backend == 'c2':
        run_c2_server(model_path, host, port, device)
    elif backend == 'onnx':
        run_onnx_server(model_path, host, port, device)
    elif backend == 'madlad400':
        run_madlad400_server(model_path, host, port, device)
    elif backend == 'mbartlarge50c2':
        run_mbartlarge50c2_server(model_path, host, port, device)
    elif backend == 'mbartlarge50onnx':
         run_mbartlarge50onnx_server(model_path, host, port, device)
    else:
        print(f"Error: Unknown backend {backend}")

def run_c2_server(model_path, host, port, device_name):
    os.environ['C2_MODEL_PATH'] = model_path
    os.environ['C2_DEVICE'] = device_name
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    import ctranslate2
    from transformers import AutoTokenizer
    model_device = "cuda" if device_name.lower() == "cuda" else "cpu"
    if not model_path:
        print("Error: Model path not specified")
        return
    try:
        translator = ctranslate2.Translator(model_path, device=model_device)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        print(f"CTranslate2 models loaded successfully!:({model_device.upper()})")
    except Exception as e:
        print(f"Error loading model: {e}")
        return
    app = FastAPI(title="English-Arabic Translation API (CTranslate2)")
    class TranslationRequest(BaseModel):
        text: str
    class TranslationResponse(BaseModel):
        translation: str
        response_time: float
    def translate_text(input_text: str):
        import time
        start_time = time.time()
        source_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(input_text))
        results = translator.translate_batch([source_tokens], max_decoding_length=500)
        target_tokens = results[0].hypotheses[0]
        translated_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(target_tokens))
        end_time = time.time()
        response_time = round(end_time - start_time, 3)
        return translated_text, response_time

    @app.post("/translate", response_model=TranslationResponse)
    async def translate(request: TranslationRequest):
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="The text is empty")
        try:
            translated_text, response_time = translate_text(request.text)
            return {"translation": translated_text, "response_time": response_time}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

    @app.post("/shutdown")
    async def shutdown():
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)
        return {"message": "Shutting down"}
    import uvicorn
    uvicorn.run(app, host=host, port=int(port), log_level="warning")

def run_onnx_server(model_path, host, port, device_name):
    import onnxruntime as ort
    import uvicorn
    import argparse
    import time
    import numpy as np
    from fastapi import FastAPI, HTTPException
    from contextlib import asynccontextmanager
    from pydantic import BaseModel
    from transformers import AutoTokenizer
    os.environ['ONNX_MODEL_PATH'] = model_path
    os.environ['ONNX_DEVICE'] = device_name
    MODEL_PATH = os.environ.get("ONNX_MODEL_PATH")
    ONNX_DEVICE = os.environ.get("ONNX_DEVICE", "cuda").lower()
    provider = "CPUExecutionProvider"
    if ONNX_DEVICE == "cuda":
        ort.preload_dlls()
    tokenizer = None
    model = None
    actual_provider = "Unknown"
    encoder_sess = None
    decoder_sess = None
    decoder_with_past_sess = None
    @asynccontextmanager
    async def lifespan(app: FastAPI):
       global tokenizer, encoder_sess, decoder_sess, decoder_with_past_sess, actual_provider
       if not os.path.exists(MODEL_PATH):
          raise FileNotFoundError(f"MODEL folder was not found in the path: {MODEL_PATH}")
       tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
       if ONNX_DEVICE == "cuda":
          providers = ["CUDAExecutionProvider"]
       else:
          providers = ["CPUExecutionProvider"]
       so = ort.SessionOptions()
       so.log_severity_level = 3
       so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
       if ONNX_DEVICE == "cuda":
          so.add_session_config_entry('session.disable_prepacking', '1')
       encoder_sess = ort.InferenceSession(os.path.join(MODEL_PATH, "encoder_model.onnx"), providers=providers, sess_options=so)
       decoder_sess = ort.InferenceSession(os.path.join(MODEL_PATH, "decoder_model.onnx"), providers=providers, sess_options=so)
       decoder_with_past_sess = ort.InferenceSession(os.path.join(MODEL_PATH, "decoder_with_past_model.onnx"), providers=providers, sess_options=so)
       actual_provider = encoder_sess.get_providers()[0]
       print(f"ONNX models loaded successfully!:{actual_provider} ({ONNX_DEVICE.upper()})")
       yield
    app = FastAPI(title="ONNX Translation API", lifespan=lifespan)

    class TranslationRequest(BaseModel):
        text: str
        source: str = "en"
        target: str = "ar"
    class TranslationResponse(BaseModel):
        translation: str
        response_time: float
    def translate_text(text, source: str = "en", target: str = "ar", max_length=100):
                    global tokenizer, encoder_sess, decoder_sess, decoder_with_past_sess
                    inputs = tokenizer(text, return_tensors="np")
                    input_ids = inputs["input_ids"]
                    attention_mask = inputs["attention_mask"]
                    encoder_outputs = encoder_sess.run(None, {
                        "input_ids": input_ids,
                        "attention_mask": attention_mask
                    })
                    encoder_hidden_states = encoder_outputs[0]
                    start_token_id = tokenizer.bos_token_id
                    if start_token_id is None:
                        start_token_id = tokenizer.cls_token_id
                    if start_token_id is None:
                        try:
                            start_token_id = tokenizer.convert_tokens_to_ids("<s>")
                        except:
                            try:
                                start_token_id = tokenizer.convert_tokens_to_ids("[CLS]")
                            except:
                                start_token_id = 0
                    decoder_input_ids = np.array([[start_token_id]], dtype=np.int64)
                    for _ in range(max_length):
                        outputs = decoder_sess.run(None, {
                            "input_ids": decoder_input_ids,
                            "encoder_hidden_states": encoder_hidden_states,
                            "encoder_attention_mask": attention_mask
                        })
                        logits = outputs[0][:, -1, :]
                        next_token_id = np.argmax(logits, axis=-1).item()
                        if next_token_id == tokenizer.eos_token_id:
                            break
                        decoder_input_ids = np.concatenate(
                            [decoder_input_ids, np.array([[next_token_id]], dtype=np.int64)],
                            axis=-1
                        )
                    decoded_text = tokenizer.decode(decoder_input_ids[0], skip_special_tokens=True)
                    cleaned_text = decoded_text.replace("``", "").replace("''", "").strip()
                    return cleaned_text if cleaned_text else "تعذر الترجمة"

    @app.post("/translate", response_model=TranslationResponse)
    async def translate(request: TranslationRequest):
        import time
        start = time.time()
        try:
            res = translate_text(request.text)
            return {"translation": res, "response_time": round(time.time() - start, 3)}
        except Exception as e:
            print(f"Translation error: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/shutdown")
    async def shutdown():
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)
        return {"message": "Shutting down"}
    uvicorn.run(app, host=host, port=int(port), log_level="warning")

def run_madlad400_server(model_path, host, port, device_name):
    model_device = "cuda" if device_name.lower() == "cuda" else "cpu"
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    import ctranslate2
    from transformers import AutoTokenizer
    import re
    if not model_path: return
    if os.path.isfile(model_path):
        model_path = os.path.dirname(model_path)
    translator = ctranslate2.Translator(model_path, device=model_device)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    print(f"MADLAD400 models loaded successfully!:({model_device.upper()})")
    app = FastAPI(title="MADLAD400 API")
    class TranslationRequest(BaseModel):
        text: str
        source: str = "en"
        target: str = "ar"
    def translate_text(text, source="en", target="ar"):
        import time
        start_time = time.time()
        full_translation = ""
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        for sentence in sentences:
            if not sentence.strip(): continue
            match = re.search(r'([.!?]+)$', sentence)
            original_punctuation = match.group(1) if match else ""
            core_sentence = sentence[:-len(original_punctuation)].strip() if original_punctuation else sentence.strip()
            if not core_sentence: continue
            target_lang_tag = f"<2{target}>"
            input_ids = tokenizer.encode(target_lang_tag + core_sentence)
            source_tokens = tokenizer.convert_ids_to_tokens(input_ids)
            results = translator.translate_batch([source_tokens], max_decoding_length=500)
            target_tokens = results[0].hypotheses[0]
            translated_ids = tokenizer.convert_tokens_to_ids(target_tokens)
            translated_text = tokenizer.decode(translated_ids)
            if translated_text.startswith(target_lang_tag):
                translated_text = translated_text[len(target_lang_tag):].strip()
            if translated_text.endswith(('.', '!', '?', '؟', '،', '؛')):
                sentence_to_correct = translated_text
            else:
                sentence_to_correct = translated_text + original_punctuation
            if target == 'ar':
                sentence_to_correct = sentence_to_correct.replace('?', '؟')
            full_translation += sentence_to_correct + " "
        return full_translation.strip(), round(time.time() - start_time, 3)

    @app.post("/translate")
    async def translate(request: TranslationRequest):
        t, r = translate_text(request.text, request.source, request.target)
        return {"translation": t, "response_time": r}

    @app.post("/shutdown")
    async def shutdown():
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)
        return {"message": "Shutting down"}
    import uvicorn
    uvicorn.run(app, host=host, port=int(port), log_level="warning")

def run_mbartlarge50c2_server(model_path, host, port, device_name):
    model_device = "cuda" if device_name.lower() == "cuda" else "cpu"
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    import ctranslate2
    from transformers import MBart50TokenizerFast
    translator = ctranslate2.Translator(model_path, device=model_device)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_path)
    print(f"MBARTLARGE50 C2 models loaded successfully! ({model_device.upper()})")
    app = FastAPI(title="MBART50 C2 API")
    LANG_CODE_MAP = {
        "ar": "ar_AR", "en": "en_XX", "fr": "fr_XX", "de": "de_DE",
        "ru": "ru_RU", "zh": "zh_CN", "es": "es_XX", "it": "it_IT",
        "pt": "pt_XX", "ja": "ja_XX", "hi": "hi_IN"
    }
    class TranslationRequest(BaseModel):
        text: str
        source: str = "en"
        target: str = "ar"
    def translate_text(text, source_lang, target_lang):
        import time
        start = time.time()
        src = LANG_CODE_MAP.get(source_lang, "en_XX")
        tgt = LANG_CODE_MAP.get(target_lang, "ar_AR")
        tokenizer.src_lang = src
        input_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
        results = translator.translate_batch([input_tokens], target_prefix=[[tgt]])
        output_tokens = results[0].hypotheses[0]
        if output_tokens and output_tokens[0] == tgt:
             output_tokens = output_tokens[1:]
        trans = tokenizer.decode(tokenizer.convert_tokens_to_ids(output_tokens))
        return trans, round(time.time() - start, 3)

    @app.post("/translate")
    async def translate(request: TranslationRequest):
        t, r = translate_text(request.text, request.source, request.target)
        return {"translation": t, "response_time": r}

    @app.post("/shutdown")
    async def shutdown():
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)
        return {"message": "Shutting down"}
    import uvicorn
    uvicorn.run(app, host=host, port=int(port), log_level="warning")

def run_mbartlarge50onnx_server(model_path, host, port, device_name):
    import numpy as np
    import onnxruntime as ort
    from optimum.onnxruntime import ORTModelForSeq2SeqLM
    from transformers import MBart50TokenizerFast
    from fastapi import FastAPI, HTTPException, Request, Query
    from contextlib import asynccontextmanager
    from pydantic import BaseModel
    import uvicorn
    available_providers = ort.get_available_providers()
    provider = "CPUExecutionProvider"
    if device_name.lower() == "cuda":
        if "CUDAExecutionProvider" in available_providers:
            provider = "CUDAExecutionProvider"
            print(f"Using CUDA provider. Available: {available_providers}")
        else:
            print("CUDA requested but not found in ONNX Runtime available providers. Falling back to CPU.")
    tokenizer = None
    model = None
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        nonlocal tokenizer, model
        tokenizer = MBart50TokenizerFast.from_pretrained(model_path)
        model = ORTModelForSeq2SeqLM.from_pretrained(model_path, provider=provider)
        print("MBART50 ONNX models loaded successfully!")
        yield
    app = FastAPI(title="MBART50 ONNX API", lifespan=lifespan)
    LANG_CODE_MAP = {
        "ar": "ar_AR", "en": "en_XX", "fr": "fr_XX", "de": "de_DE",
        "ru": "ru_RU", "zh": "zh_CN", "es": "es_XX", "it": "it_IT",
         "pt": "pt_XX", "ja": "ja_XX", "hi": "hi_IN"
    }
    class TranslationRequest(BaseModel):
        text: str
        source: str = "en"
        target: str = "ar"
    def perform_translation(text: str, source: str, target: str):
        try:
            src = LANG_CODE_MAP.get(source, "en_XX")
            tgt = LANG_CODE_MAP.get(target, "ar_AR")
            if src not in tokenizer.lang_code_to_id:
                raise ValueError(f"Source language code '{src}' not found in tokenizer.")
            if tgt not in tokenizer.lang_code_to_id:
                raise ValueError(f"Target language code '{tgt}' not found in tokenizer.")
            tokenizer.src_lang = src
            inputs = tokenizer(text, return_tensors="pt")
            inputs = {k: v.to("cpu") for k, v in inputs.items()}
            model.use_io_binding = False
            generated_ids = model.generate(
                **inputs, 
                max_length=512, 
                forced_bos_token_id=tokenizer.lang_code_to_id[tgt]
            )
            return tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        except Exception as e:
            print(f"\n!!! Error inside perform_translation: {e} !!!")
            import traceback
            traceback.print_exc()
            raise e

    @app.post("/translate")
    async def translate_post(request: TranslationRequest):
        import traceback
        try:
            if not request.text or not request.text.strip():
                return {"translation": "", "response_time": 0.0}
            start_time = time.time()
            trans = perform_translation(request.text, request.source, request.target)
            return {"translation": trans, "response_time": round(time.time() - start_time, 3)}
        except Exception as e:
            print("\n\n!!! CRITICAL ERROR IN POST REQUEST !!!")
            print(str(e))
            traceback.print_exc()
            print("!!! END OF ERROR !!!\n\n")
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/translate")
    async def translate_get(text: str = Query(...), source: str = "en", target: str = "ar"):
        import traceback
        try:
            if not text or not text.strip():
                return {"translation": "", "response_time": 0.0}
            start_time = time.time()
            trans = perform_translation(text, source, target)
            return {"translation": trans, "response_time": round(time.time() - start_time, 3)}
        except Exception as e:
            print("\n\n!!! CRITICAL ERROR IN GET REQUEST !!!")
            print(str(e))
            traceback.print_exc()
            print("!!! END OF ERROR !!!\n\n")
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/shutdown")
    async def shutdown():
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)
        return {"message": "Shutting down"}
    uvicorn.run(app, host=host, port=int(port), log_level="warning")

if __name__ == "__main__":
    import argparse
    import traceback
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--backend", required=True)
        parser.add_argument("--model_path", required=True)
        parser.add_argument("--host", default="127.0.0.1")
        parser.add_argument("--port", default="7870")
        parser.add_argument("--device", default="cpu")
        args = parser.parse_args()
        run_server_standalone(args.backend, args.model_path, args.host, args.port, args.device)
    except Exception:
        print(traceback.format_exc())
        sys.exit(1)