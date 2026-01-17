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

import sys
import os

# Add the application directory to sys.path
app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

import argparse
import json
import shutil
import codecs
import time
try:
    from translations import TRANSLATIONS
except ImportError:
    TRANSLATIONS = {}

def tr_static(lang, key):
    try:
        return TRANSLATIONS.get(lang, TRANSLATIONS.get('ar', {})).get(key, key)
    except:
        return key
task_lang = 'ar'

def print_json(data):
    print(json.dumps(data, ensure_ascii=False))
    sys.stdout.flush()

def print_message(msg):
    print_json({"type": "message", "content": msg})

def print_progress(value):
    print_json({"type": "progress", "value": value})

def verify_libraries(device):
    try:
        if device == "cuda":
            try:
                import torch
                if not torch.cuda.is_available():
                    print_message(tr_static(task_lang, 'error_cuda_not_available'))
                    print_json({"type": "result", "success": False})
                    return
            except ImportError:
                print_message(tr_static(task_lang, 'error_pytorch_not_installed'))
                print_json({"type": "result", "success": False})
                return
        elif device == "cpu":
            try:
                import ctranslate2
                from transformers import AutoTokenizer
            except ImportError as e:
                print_message(f"{tr_static(task_lang, 'error_missing_lib_c2')} {e}")
                print_json({"type": "result", "success": False})
                return
        print_message(tr_static(task_lang, 'libraries_verified_success'))
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_verifying_libraries')} {str(e)}")
        print_json({"type": "result", "success": False})

def convert_opus_c2(src_model, dst_model, quantization):
    try:
        from ctranslate2.converters import TransformersConverter
        print_message(f"{tr_static(task_lang, 'starting_conversion_to')} {quantization}")
        print_progress(10)
        os.makedirs(dst_model, exist_ok=True)
        converter = TransformersConverter(src_model)
        print_progress(30)
        print_message(tr_static(task_lang, 'converting_model'))
        try:
            converter.convert(dst_model, quantization=quantization, force=True)
            print_progress(80)
        except Exception as e:
            print_message(f"{tr_static(task_lang, 'conversion_quant_failed_retry')} {e}")
            converter.convert(dst_model, force=True)
            print_progress(80)
            print_message(tr_static(task_lang, 'conversion_success_no_quant'))
        print_message(tr_static(task_lang, 'copying_extra_files'))
        files_to_copy = ["source.spm", "target.spm", "special_tokens_map.json", "vocab.json", "tokenizer_config.json"]
        for file in files_to_copy:
            src = os.path.join(src_model, file)
            dst = os.path.join(dst_model, file)
            if os.path.exists(src):
                shutil.copy(src, dst)
        print_progress(100)
        print_message(tr_static(task_lang, 'model_converted_success'))
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_conversion')} {str(e)}")
        print_json({"type": "result", "success": False})

def convert_mbart_c2(src_model, dst_model, quantization):
    try:
        from ctranslate2.converters import TransformersConverter
        import transformers
        if not os.path.isdir(src_model):
            print_message(tr_static(task_lang, 'error_src_model_not_found'))
            print_json({"type": "result", "success": False})
            return
        print_progress(10)
        if os.path.exists(dst_model):
            print_message(tr_static(task_lang, 'deleting_old_folder'))
            shutil.rmtree(dst_model)
        print_message(f"{tr_static(task_lang, 'starting_mbart_conversion_to')} {quantization}")
        print_progress(30)
        converter = TransformersConverter(src_model)
        converter.convert(dst_model, quantization=quantization, force=True)
        print_progress(70)
        print_message(tr_static(task_lang, 'saving_tokenizer_files'))
        tokenizer = transformers.MBart50TokenizerFast.from_pretrained(src_model)
        tokenizer.save_pretrained(dst_model)
        print_progress(90)
        print_progress(100)
        print_message(tr_static(task_lang, 'conversion_success'))
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_conversion')} {str(e)}")
        import traceback
        print_message(traceback.format_exc())
        print_json({"type": "result", "success": False})

def convert_mbart_onnx(src_model, dst_model, quantization):
    try:
        from optimum.onnxruntime import ORTModelForSeq2SeqLM, ORTQuantizer
        from optimum.onnxruntime.configuration import AutoQuantizationConfig
        from transformers import AutoTokenizer
        import torch
        if os.path.exists(dst_model):
            print_message(tr_static(task_lang, 'deleting_old_folder'))
            shutil.rmtree(dst_model)
        os.makedirs(dst_model, exist_ok=True)
        print_progress(10)
        print_message(tr_static(task_lang, 'exporting_onnx_wait'))
        print_message(tr_static(task_lang, 'warning_ram_requirement'))
        print_progress(30)
        model = ORTModelForSeq2SeqLM.from_pretrained(
            src_model, 
            export=True,
            use_cache=True
        )
        print_message(tr_static(task_lang, 'onnx_export_success_loading_tokenizer'))
        tokenizer = AutoTokenizer.from_pretrained(src_model)
        if quantization:
            temp_onnx_dir = os.path.join(os.path.dirname(dst_model), "temp_raw_onnx")
            if os.path.exists(temp_onnx_dir):
                shutil.rmtree(temp_onnx_dir)
            os.makedirs(temp_onnx_dir, exist_ok=True)
            print_message(tr_static(task_lang, 'saving_raw_model_temp'))
            model.save_pretrained(temp_onnx_dir)
            tokenizer.save_pretrained(temp_onnx_dir) # حفظ التوكنيزر في المجلد المؤقت أيضاً
            print_progress(60)
            print_message(f"{tr_static(task_lang, 'quantizing_model')} {quantization}")
            print_progress(70)
            qconfig = AutoQuantizationConfig.avx2(is_static=False, per_channel=False)
            onnx_files = [f for f in os.listdir(temp_onnx_dir) if f.endswith('.onnx')]
            for onnx_file in onnx_files:
                print_message(f"{tr_static(task_lang, 'quantizing_part')} {onnx_file}...")
                quantizer = ORTQuantizer.from_pretrained(temp_onnx_dir, file_name=onnx_file)
                quantizer.quantize(save_dir=dst_model, quantization_config=qconfig)
            tokenizer.save_pretrained(dst_model)
            print_message(tr_static(task_lang, 'cleaning_temp_files'))
            shutil.rmtree(temp_onnx_dir)
            print_progress(90)
        else:
            print_message(tr_static(task_lang, 'saving_model_files'))
            model.save_pretrained(dst_model)
            tokenizer.save_pretrained(dst_model)
            print_progress(90)
        print_progress(100)
        print_message(tr_static(task_lang, 'conversion_success'))
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_conversion')} {str(e)}")
        import traceback
        print_message(traceback.format_exc())
        print_json({"type": "result", "success": False})

def convert_opus_onnx(src_model, dst_model, quantization):
    try:
        from optimum.onnxruntime import ORTModelForSeq2SeqLM, ORTQuantizer
        from optimum.onnxruntime.configuration import AutoQuantizationConfig
        from transformers import AutoTokenizer
        import glob
        os.makedirs(dst_model, exist_ok=True)
        print_progress(10)
        print_message(tr_static(task_lang, 'copying_extra_files'))
        files = ["config.json", "generation_config.json", "source.spm", "special_tokens_map.json", "target.spm", "tokenizer_config.json", "vocab.json"]
        for f in files:
            src = os.path.join(src_model, f)
            dst = os.path.join(dst_model, f)
            if os.path.exists(src):
                shutil.copy(src, dst)
        print_progress(20)
        print_message(tr_static(task_lang, 'exporting_onnx_wait'))
        model = ORTModelForSeq2SeqLM.from_pretrained(src_model, export=True)
        tokenizer = AutoTokenizer.from_pretrained(src_model)
        model.save_pretrained(dst_model)
        tokenizer.save_pretrained(dst_model)
        print_progress(70)
        if quantization:
            print_message(f"{tr_static(task_lang, 'quantizing_model')} {quantization}")
            print_progress(80)
            qconfig = AutoQuantizationConfig.avx2(is_static=False, per_channel=False)
            onnx_files = glob.glob(os.path.join(dst_model, "*_model.onnx"))
            if not onnx_files:
                print_message(tr_static(task_lang, 'warning_no_onnx_files'))
            for file_path in onnx_files:
                file_name = os.path.basename(file_path)
                print_message(f"{tr_static(task_lang, 'quantizing')} {file_name}...")
                temp_dir = os.path.join(dst_model, f"temp_quant_{file_name}")
                if os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir)
                os.makedirs(temp_dir, exist_ok=True)
                try:
                    quantizer = ORTQuantizer.from_pretrained(dst_model, file_name=file_name)
                    quantizer.quantize(save_dir=temp_dir, quantization_config=qconfig)
                    quantized_files = glob.glob(os.path.join(temp_dir, "*.onnx"))
                    if not quantized_files:
                         raise Exception(f"{tr_static(task_lang, 'error_quant_failed_no_file')} {file_name}")
                    quantized = quantized_files[0]
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    shutil.move(quantized, file_path)
                except Exception as q_error:
                    print_message(f"{tr_static(task_lang, 'error_during_quant')} {file_name}: {str(q_error)}")
                    raise q_error
                finally:
                    if os.path.exists(temp_dir):
                        shutil.rmtree(temp_dir)
            print_progress(90)
        print_progress(100)
        print_message(tr_static(task_lang, 'conversion_success'))
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_conversion')} {str(e)}")
        print_json({"type": "result", "success": False})

def check_for_corrupted_files(path):
    if not os.path.isdir(path):
        return False, f"{tr_static(task_lang, 'error_folder_not_found')} {path}"
    corrupted = []
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path) and os.path.getsize(full_path) == 0:
            corrupted.append(f)
    if corrupted:
        return False, f"{tr_static(task_lang, 'error_download_corrupted')} {', '.join(corrupted)}"
    return True, ""

def verify_download(model_path):
    """التحقق من تحميل نموذج OPUS"""
    try:
        if not model_path:
            print_message(tr_static(task_lang, 'error_model_path_not_specified'))
            print_json({"type": "result", "success": False})
            print_progress(10)
            return
        print_message(tr_static(task_lang, 'verifying_model_at'))
        print_progress(30)
        ok, err = check_for_corrupted_files(model_path)
        if not ok:
            print_message(err)
            print_json({"type": "result", "success": False})
            return
        from transformers import MarianMTModel, MarianTokenizer
        print_message(tr_static(task_lang, 'loading_model_local'))
        print_progress(40)
        try:
            print_message(tr_static(task_lang, 'loading_tokenizer'))
            print_progress(50)
            tokenizer = MarianTokenizer.from_pretrained(model_path)
            print_message(tr_static(task_lang, 'tokenizer_loaded_success'))
            print_progress(60)
        except Exception as te:
            print_message(f"{tr_static(task_lang, 'error_loading_tokenizer')} {str(te)}")
            raise te
        try:
            print_message(tr_static(task_lang, 'loading_model'))  
            print_progress(70)
            model = MarianMTModel.from_pretrained(model_path)
            print_message(tr_static(task_lang, 'model_loaded_success'))
            print_progress(80)
        except Exception as me:
            print_message(f"{tr_static(task_lang, 'error_loading_model')} {str(me)}")
            raise me
        print_message(tr_static(task_lang, 'model_integrity_verified'))
        print_progress(100)
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_verifying_model')} {str(e)}")
        import traceback
        print_message(traceback.format_exc())
        print_json({"type": "result", "success": False})

def verify_mbartlarge50_download(model_path):
    """التحقق من تحميل نموذج MBARTLARGE50"""
    try:
        if not model_path:
            print_message(tr_static(task_lang, 'error_model_path_not_specified'))
            print_json({"type": "result", "success": False})
            return
        print_message(tr_static(task_lang, 'verifying_mbart_at'))
        print_progress(30)
        ok, err = check_for_corrupted_files(model_path)
        if not ok:
            print_message(err)
            print_json({"type": "result", "success": False})
            return
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        print_progress(40)
        print_message(tr_static(task_lang, 'loading_mbart_local'))
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            print_progress(60)
            print_message(tr_static(task_lang, 'tokenizer_loaded_success'))
        except Exception as te:
            print_message(f"{tr_static(task_lang, 'error_loading_tokenizer')} {str(te)}")
            raise te
        try:
            model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
            print_progress(80)
            print_message(tr_static(task_lang, 'model_loaded_success'))
        except Exception as me:
            print_message(f"{tr_static(task_lang, 'error_loading_model')} {str(me)}")
            raise me
        print_message(tr_static(task_lang, 'model_integrity_verified'))
        print_progress(100)
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_verifying_mbart')} {str(e)}")
        import traceback
        print_message(traceback.format_exc())
        print_json({"type": "result", "success": False})

def verify_madlad400_download(model_path, model_device):
    """التحقق من تحميل نموذج MADLAD400"""
    try:
        if not model_path:
            print_message(tr_static(task_lang, 'error_model_path_not_specified'))
            print_json({"type": "result", "success": False})
            return
        print_progress(10)    
        print_message(tr_static(task_lang, 'verifying_madlad_at'))
        print_progress(30)
        ok, err = check_for_corrupted_files(model_path)
        if not ok:
            print_message(err)
            print_json({"type": "result", "success": False})
            return
        import ctranslate2
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        print_progress(40)
        print_message(tr_static(task_lang, 'loading_madlad_local'))
        try:
            device = model_device if model_device else "cpu"
            print_message(f"{tr_static(task_lang, 'testing_model_on_device')} {device}")
            print_progress(60)
            translator = ctranslate2.Translator(model_path, device=device)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            print_message(tr_static(task_lang, 'translator_tokenizer_loaded_success'))
            print_progress(80)
        except Exception as te:
            print_message(f"{tr_static(task_lang, 'error_loading_components')} {str(te)}")
            raise te
        print_message(tr_static(task_lang, 'model_integrity_verified'))
        print_progress(100)
        print_json({"type": "result", "success": True})
    except Exception as e:
        print_message(f"{tr_static(task_lang, 'error_verifying_madlad')} {str(e)}")
        import traceback
        print_message(traceback.format_exc())
        print_json({"type": "result", "success": False})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("task", choices=["verify", "convert_opus_c2", "convert_mbart_c2", "convert_mbart_onnx", "convert_opus_onnx", "verify_download", "verify_mbartlarge50_download", "verify_madlad400_download"])
    parser.add_argument("--src", help="Source model path")
    parser.add_argument("--dst", help="Destination model path")
    parser.add_argument("--quantization", help="Quantization type (int8, float16, etc.)")
    parser.add_argument("--device", help="Device (cpu/cuda)")
    parser.add_argument("--lang", default="ar", help="Language for output")
    args = parser.parse_args()
    task_lang = args.lang
    if args.task == "verify":
        verify_libraries(args.device)
    elif args.task == "convert_opus_c2":
        convert_opus_c2(args.src, args.dst, args.quantization)
    elif args.task == "convert_mbart_c2":
        convert_mbart_c2(args.src, args.dst, args.quantization)
    elif args.task == "convert_mbart_onnx":
        convert_mbart_onnx(args.src, args.dst, args.quantization)
    elif args.task == "convert_opus_onnx":
        convert_opus_onnx(args.src, args.dst, args.quantization)
    elif args.task == "verify_download":
        verify_download(args.src)
    elif args.task == "verify_mbartlarge50_download":
        verify_mbartlarge50_download(args.src)
    elif args.task == "verify_madlad400_download":
        verify_madlad400_download(args.src, args.device)
