# -*- coding: utf-8 -*-
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
TRANSLATIONS = {
    'ar': {
        'app_title': 'METranslator',
        'status_offline': 'الحالة: غير متصل',
        'status_loading': 'الحالة: جاري التحميل...',
        'status_running': 'الحالة: يعمل',
        'status_error': 'الحالة: خطأ',
        'run_server': 'تشغيل الخادم',
        'stop_server': 'إيقاف الخادم',
        'env_setup': 'إعداد البيئة',
        'settings': 'الإعدادات',
        'download_convert': 'إعدادات التحميل والتحويل',
        'help': 'تعليمات',
        'to': 'إلى:',
        'from': 'من:',
        'appearance': 'المظهر',
        'select_theme': 'اختر الثيم:',
        'select_model': 'اختيار نموذج الترجمة',
        'multilingual_models': 'النماذج متعددة اللغات',
        'device': 'الجهاز:',
        'server_settings': 'إعدادات الخادم',
        'host': 'المضيف',
        'port': 'المنفذ',
        'translate_text_group': 'ترجمة النص',
        'source_text': 'النص المصدر:',
        'translation_label': 'الترجمة:',
        'translate_btn': 'ترجمة',
        'clear_btn': 'مسح',
        'font_size': 'حجم الخط:',
        'close': 'إغلاق',
        'warning': 'تحذير',
        'server_running_warning': 'الخادم يعمل بالفعل. يجب إيقاف الخادم قبل تغيير النموذج أو الجهاز.',
        'server_running_warning_opus_land': 'الخادم يعمل بالفعل. يجب إيقاف الخادم قبل تغيير اللغة لنماذج OPUS.',
        'stop_server_first': 'يجب إيقاف الخادم أولاً.',
        'back': 'العودة',
        'download_multilingual': 'تحميل النماذج متعددة اللغات',
        'download_madlad400': '⬇️ تحميل نموذج MADLAD400 متعدد اللغات',
        'download_mbartlarge50': '⬇️ تحميل نموذج MBARTLARGE50',
        'convert_c2': 'تحويل إلى CTranslate2',
        'convert_onnx': 'تحويل إلى ONNX',
        'convert_btn': 'تحويل',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'اختيار اللغات',
        'download_model': '⬇️ تحميل النموذج',
        'output_direction': 'rtl',
        'lang_label': 'اللغة:',
        'select_lang': 'اختر لغة الواجهة:',
        'help_title': 'تعليمات استخدام METranslator',
        'confirm': 'تأكيد',
        'loading': 'تحميل',
        'info': 'معلومات',
        'error': 'خطأ',
        'success': 'نجاح',
        'wait': 'يرجى الانتظار',
        'alert': 'تنبيه',
        'server_already_running': 'الخادم يعمل بالفعل.',
        'download_failed': 'فشل التحميل',
        'model_path_required': 'مسار النموذج مطلوب.',
        'model_must_be_downloaded': 'يجب تحميل النموذج أولاً.',
        'server_starting': 'جاري تشغيل الخادم...',
        'model_msg': 'النموذج',
        'host_msg': 'المضيف',
        'port_msg': 'المنفذ',
        'confirm_download_msg': 'هل أنت متأكد من رغبتك في تحميل النموذج؟',
        'converting_in_progress': 'جاري تحويل النموذج...',
        'converting_model_to': 'جاري تحويل النموذج إلى',
        'confirm_conversion_msg': 'هل تريد حقاً بدء عملية التحويل؟',
        'download_in_progress_warning': 'هناك عملية تحميل جارية بالفعل.',
        'conversion_in_progress_warning': 'هناك عملية تحويل جارية بالفعل.',
        'setup_in_progress_warning': 'هناك عملية إعداد جارية بالفعل.',
        'original_model_not_found': 'النموذج الأصلي غير موجود',
        'download_model_first': 'يرجى تحميل النموذج أولاً.',
        'conversion_c2_success': 'تم تحويل النموذج إلى CTranslate2 بنجاح.',
        'conversion_onnx_success': 'تم تحويل النموذج إلى ONNX بنجاح.',
        'download_madlad400_success': 'تم تحميل نموذج MADLAD400 بنجاح.',
        'download_mbartlarge50_success': 'تم تحميل نموذج MBARTLARGE50 بنجاح.',
        'download_success_msg': 'تم تحميل النموذج بنجاح.',
        'server_not_active_translation_warning': 'الخادم غير نشط. يرجى تشغيل الخادم أولاً.',
        'server_loading_wait_warning': 'الخادم لا يزال في مرحلة التحميل. يرجى الانتظار.',
        'enter_text_to_translate': 'يرجى إدخال نص للترجمة.',
        'failed_to_start_translation': 'فشل في بدء الترجمة',
        'select_at_least_one_option': 'يرجى اختيار خيار واحد على الأقل.',
        'cannot_create_venv_without_python': 'لا يمكن إنشاء بيئة افتراضية بدون تثبيت بايثون.',
        'cannot_install_reqs_without_venv': 'لا يمكن تثبيت المكتبات بدون وجود بيئة افتراضية.',
        'environment_setup_title': 'إعداد البيئة',
        'portable_environment_setup_title': 'إعداد البيئة الافتراضية المحمولة',
        'requirements_type_group': 'نوع المتطلبات',
        'cpu_requirements': 'متطلبات CPU',
        'gpu_requirements': 'متطلبات GPU (NVIDIA CUDA)',
        'setup_options_group': 'خيارات الإعداد',
        'install_python_local': 'تثبيت بايثون محلياً',
        'install_python_local_installed': 'تثبيت بايثون محلياً (مثبت بالفعل)',
        'install_python_local_tooltip': 'سيتم تحميل وتثبيت نسخة محمولة من بايثون داخل مجلد البرنامج',
        'create_virtual_environment': 'إنشاء البيئة الافتراضية',
        'create_virtual_environment_created': 'إنشاء البيئة الافتراضية (موجودة بالفعل)',
        'create_virtual_environment_tooltip': 'إنشاء بيئة معزولة لتثبيت المكتبات',
        'recreate_virtual_environment': 'حذف وإعادة إنشاء البيئة الافتراضية',
        'recreate_virtual_environment_tooltip': 'سيتم حذف البيئة الموجودة وإعادة إنشائها من الصفر (مفيد عند تغيير نوع الجهاز)',
        'install_requirements': 'تثبيت المكتبات اللازمة',
        'install_requirements_tooltip': 'تثبيت مكتبات الترجمة والذكاء الاصطناعي الضرورية',
        'start_setup_btn': 'بدء',
        'cancel_btn': 'إلغاء',
        'confirm_recreate_venv': 'سيتم حذف البيئة الافتراضية الحالية وإعادة إنشائها. هل تريد الاستمرار؟',
        'confirm_start_setup': 'هل تريد بدء عملية الإعداد؟',
        'confirm_cancel_setup': 'هل أنت متأكد من رغبتك في إلغاء عملية الإعداد؟',
        'venv_virtualenv_not_found': 'نظام venv غير متوفر، جاري المحاولة باستخدام virtualenv...',
        'setting_up_in_progress': 'جاري الإعداد...',
        'setting_up_environment': 'جاري إعداد البيئة...',
        'environment_setup_finished': 'انتهت عملية إعداد البيئة.',
        'download_in_progress_exit_warning': 'هناك عملية تحميل النموذج قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'download_madlad400_in_progress_exit_warning': 'هناك عملية تحميل نموذج madlad400 قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'convert_c2_in_progress_exit_warning': 'هناك عملية تحويل النموذج إلى C2 قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'convert_onnx_in_progress_exit_warning': 'هناك عملية تحويل النموذج إلى ONNX قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'convert_mbart_c2_in_progress_exit_warning': 'هناك عملية تحويل نموذج MBARTLARGE50 إلى C2 قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'convert_mbart_onnx_in_progress_exit_warning': 'هناك عملية تحويل نموذج MBARTLARGE50 إلى ONNX قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'verification_in_progress_exit_warning': 'هناك عملية تحقق من المكتبات قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'translation_in_progress_exit_warning': 'هناك عملية ترجمة قيد التشغيل. هل تريد إلغاؤها قبل الخروج؟',
        'server_not_active': 'الخادم غير متصل',
        'convert_mbartlarge50_to_format_confirm': 'هل تريد تحويل نموذج MBARTLARGE50 إلى',
        'may_take_time': 'هذا قد يستغرق وقتاً',
        'convert_model_to_format_confirm': 'هل تريد تحويل النموذج إلى',
        'server_started_successfully': 'تم تشغيل الخادم بنجاح',
        'server_stopped_successfully': 'تم إيقاف الخادم بنجاح',
        'settings_save_failed': 'فشل في حفظ الإعدادات',
        'settings_saved_auto': 'تم حفظ الإعدادات تلقائياً',
        'settings_loaded_auto': 'تم تحميل الإعدادات تلقائياً',
        'settings_file_not_found': 'ملف الإعدادات غير موجود، تم استخدام القيم الافتراضية',
        'status': 'الحالة',
        'translating_in_progress': 'جاري الترجمة...',
        'translating_progress': 'تقدم الترجمة',
        'text_fields_cleared': 'تم مسح حقول النص',
        'translation_successful': 'تمت الترجمة بنجاح',
        'seconds': 'ثانية',
        'translation_error': 'خطأ في الترجمة',
        'translation_cancelled': 'تم إلغاء الترجمة',
        'translation_started_background': 'بدأت الترجمة في الخلفية',
        'translation_in_progress_cancel': 'هناك عملية ترجمة جارية. هل تريد إلغاؤها؟',
        'translation_in_progress_cancel_new': 'هناك عملية ترجمة جارية. هل تريد إلغاؤها لبدء ترجمة جديدة؟',
        'downloading_in_progress': 'جاري التحميل...',
        'downloading_madlad400_model': 'جاري تحميل نموذج MADLAD400...',
        'downloading_mbartlarge50_model': 'جاري تحميل نموذج MBARTLARGE50...',
        'downloading_model_msg': 'جاري تحميل النموذج',
        'conversion_finished_msg': 'انتهت عملية التحويل',
        'conversion_mbartlarge50_c2_success': 'تم تحويل MBARTLARGE50 إلى CTranslate2 بنجاح',
        'conversion_mbartlarge50_onnx_success': 'تم تحويل MBARTLARGE50 إلى ONNX بنجاح',
        'mbartlarge50_original_model_not_found': 'النموذج الأصلي لـ MBARTLARGE50 غير موجود',
        'setting_up_progress': 'تقدم الإعداد',
        'warning_thread_termination_failed': 'تحذير: فشل إنهاء بعض الخيوط',
        'warning_thread_timeout': 'تحذير: انتهت مهلة انتظار الخيوط',
        'python_local_exists': 'بايثون محلي موجود بالفعل',
        'downloading_python_installer': 'جاري تحميل مثبت بايثون...',
        'installing_python': 'جاري تثبيت بايثون...',
        'python_install_success': 'تم تثبيت بايثون محلي بنجاح',
        'python_install_failed': 'فشل في تثبيت بايثون',
        'fatal_error_venv_active': 'خطأ قاتل: لا يمكن حذف البيئة لأن البرنامج يعمل من خلالها!',
        'venv_exists': 'البيئة الافتراضية موجودة بالفعل',
        'venv_created_success': 'تم إنشاء البيئة الافتراضية بنجاح',
        'venv_creation_failed': 'فشل في إنشاء البيئة الافتراضية',
        'requirements_file_not_found': 'ملف المتطلبات غير موجود',
        'installing_requirements_from': 'تثبيت المتطلبات من',
        'download_madlad400_confirm': 'هل تريد تحميل نموذج MADLAD400؟',
        'download_mbartlarge50_confirm': 'هل تريد تحميل نموذج MBARTLARGE50؟',
        'download_model_specific': 'تحميل',
        'download_model_tooltip': 'تحميل النموذج من الإنترنت:',
        'error_cuda_not_available': 'خطأ: CUDA غير متوفر على النظام',
        'error_pytorch_not_installed': 'خطأ: PyTorch غير مثبت',
        'error_missing_lib_c2': 'مكتبة مطلوبة مفقودة لـ CTranslate2:',
        'libraries_verified_success': 'تم التحقق من المكتبات بنجاح',
        'error_verifying_libraries': 'خطأ في التحقق من المكتبات:',
        'error_deleting_venv': 'خطأ في حذف البيئة الافتراضية:',
        'starting_conversion_to': 'بدء تحويل النموذج الى:',
        'converting_model': 'جاري تحويل النموذج...',
        'conversion_quant_failed_retry': 'فشل التحويل مع تكميم، جاري المحاولة بدونه:',
        'conversion_success_no_quant': 'تم التحويل بنجاح بدون تكميم',
        'copying_extra_files': 'جاري نسخ الملفات الإضافية...',
        'model_converted_success': 'تم تحويل النموذج بنجاح',
        'error_conversion': 'خطأ في التحويل:',
        'download_finished_msg': 'تم تحميل النموذج بنجاح',
        'error_src_model_not_found': 'خطأ: مجلد النموذج المصدر غير موجود',
        'deleting_old_folder': 'جاري حذف المجلد القديم',
        'starting_mbart_conversion_to': 'بدء تحويل نموذج mbartlarge50 إلى:',
        'saving_tokenizer_files': 'جاري حفظ ملفات الـ Tokenizer...',
        'conversion_success': 'تم التحويل بنجاح',
        'exporting_onnx_wait': 'جاري تصدير النموذج إلى ONNX (قد يستغرق هذا وقتاً طويلاً للنماذج الكبيرة)',
        'warning_ram_requirement': 'تنبيه: ستحتاج إلى ذاكرة عشوائية (RAM) كافية (على الأقل 16 جيجابايت).',
        'onnx_export_success_loading_tokenizer': 'تم تصدير النموذج بنجاح، جاري تحميل الـ Tokenizer...',
        'saving_raw_model_temp': 'جاري حفظ النموذج الخام في مجلد مؤقت...',
        'quantizing_model': 'جاري تكميم النموذج:',
        'quantizing_part': 'جاري تكميم الجزء:',
        'cleaning_temp_files': 'جاري تنظيف الملفات المؤقتة...',
        'saving_model_files': 'جاري حفظ ملفات النموذج...',
        'warning_no_onnx_files': 'تنبيه: لم يتم العثور على ملفات ONNX',
        'quantizing': 'تكميم',
        'error_quant_failed_no_file': 'فشل التكميم: لم يتم إنشاء ملف .onnx في المجلد المؤقت لـ',
        'error_during_quant': 'خطأ أثناء تكميم',
        'error_folder_not_found': 'المجلد غير موجود:',
        'error_download_corrupted': 'فشل التحميل: تم العثور على ملفات فارغة:',
        'error_model_path_not_specified': 'خطأ: مسار النموذج غير محدد',
        'verifying_model_at': 'جاري التحقق من النموذج في المسار:',
        'loading_model_local': 'جاري التحميل النهائي للنموذج من الملفات المحلية...',
        'loading_tokenizer': 'جاري تحميل Tokenizer',
        'tokenizer_loaded_success': 'تم تحميل Tokenizer بنجاح',
        'error_loading_tokenizer': 'خطأ في تحميل Tokenizer:',
        'loading_model': 'جاري تحميل Model',
        'model_loaded_success': 'تم تحميل Model بنجاح',
        'error_loading_model': 'خطأ في تحميل Model:',
        'model_integrity_verified': 'تم التحقق من سلامة النموذج بنجاح',
        'error_verifying_model': 'خطأ في التحقق من النموذج:',
        'verifying_mbart_at': 'جاري التحقق من نموذج MBARTLARGE50 في المسار:',
        'loading_mbart_local': 'جاري التحميل النهائي لنموذج MBARTLARGE50 من الملفات المحلية...',
        'error_verifying_mbart': 'خطأ في التحقق من نموذج MBARTLARGE50:',
        'verifying_madlad_at': 'جاري التحقق من نموذج MADLAD400 في المسار:',
        'loading_madlad_local': 'جاري التحميل النهائي لنموذج MADLAD400 من الملفات المحلية...',
        'testing_model_on_device': 'جاري اختبار تحميل النموذج على جهاز:',
        'translator_tokenizer_loaded_success': 'تم تحميل Translator و Tokenizer بنجاح',
        'error_loading_components': 'خطأ في تحميل المكونات:',
        'error_verifying_madlad': 'خطأ في التحقق من نموذج MADLAD400:',
        'download_opus_mt_tooltip': 'تحميل نموذج OPUS-MT المحدد',
        'convert_c2_tooltip': 'تحويل النموذج إلى صيغة CTranslate2 المحددة',
        'convert_onnx_tooltip': 'تحويل النموذج إلى صيغة ONNX المحددة',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2 dir="rtl">إعداد METranslator:</h2>

        <h3 dir="rtl">الخطوة 1: تثبيت المكتبات اللازمة (يتطلب إنترنت)</h3>
        <ol dir="rtl">
            <li>انتقل إلى إعداد البيئة.</li>
            <li>اختر جهازك: CPU لمن ليس لديهم كروت شاشة NVIDIA، أو GPU لمستخدمي NVIDIA الذين يرغبون في استخدام CUDA.</li>
            <li>حدد الخيارات الأخرى وانقر على بدأ.</li>
        </ol>

        <p dir="rtl"><b>ملاحظة:</b></p>
        <ul dir="rtl">
            <li>إذا كنت بحاجة إلى تغيير نوع جهازك، فحدد "حذف وإعادة إنشاء البيئة الافتراضية" لمنع تعارض المكتبات.</li>
            <li>تحميل مكتبات GPU كبير (حوالي 3 جيجابايت) وقد يستغرق بعض الوقت.</li>
        </ul>

        <h3 dir="rtl">الخطوة 2: تحميل وتحويل النماذج (يتطلب إنترنت)</h3>
        <ol dir="rtl">
            <li>انتقل إلى إعدادات التحميل والتحويل.</li>
            <li>انقر فوق تحميل النموذج (اختر من opus-mt-tc-big، أو MADLAD-400-Ct2، أو mBART-large-50).</li>
            <li>انقر فوق تحويل النموذج لجهازك (فقط لـ opus-mt-tc-big و mBART-large-50).</li>
        </ol>

        <p dir="rtl"><b>ملاحظة:</b></p>
        <ul dir="rtl">
            <li>بالنسبة لنموذج opus-mt-tc-big، يجب عليك تحديد لغتي المصدر والهدف.</li>
            <li>نموذج MADLAD-400-Ct2 محول بالفعل إلى ct2-int8_float16 ولا يحتاج إلى مزيد من التحويل.</li>
            <li>حجم نموذج opus-mt-tc-big حوالي 450 ميجابايت.</li>
            <li>حجما نموذجي MADLAD-400-Ct2 و mBART-large-50 حوالي 3 جيجابايت لكل منهما.</li>
        </ul>

        <h3 dir="rtl">الخطوة 3: التحضير للترجمة</h3>
        <ol dir="rtl">
            <li>انتقل إلى الإعدادات ⚙️.</li>
            <li>حدد النموذج.</li>
            <li>حدد المسار.</li>
            <li>اختر نوع الجهاز (CPU أو GPU).</li>
        </ol>

        <p dir="rtl">أنت الآن جاهز للترجمة واستخدام الخدمة.</p>

        <h3 dir="rtl">طريقة الاستخدام:</h3>
        <p dir="rtl">بساطة انقر فوق تشغيل الخادم ▶ كلما احتجت إلى ترجمة. </p>

        <h3 dir="rtl">نتقدم بجزيل الشكر لهذه المشاريع مفتوحة المصدر:</h3>
        <ul dir="rtl">
            <li>Hugging Face لنماذج وذكاء اصطناعي ومجموعات البيانات الخاصة بهم.
                <ul>
                    <li>استكشف عروضهم في <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>اكتشف نماذج محددة مثل <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>تحقق من MADLAD-400-Ct2 في <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>تعرف على المزيد حول mBART-large-50 في <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python للبرمجة النصية للخلفية.
                <ul>
                    <li>قم بزيارة <a href="https://www.python.org/">Python</a> لمعرفة المزيد.</li>
                </ul>
            </li>
            <li>PyTorch لإطار عمل التعلم الآلي الخاص بنا.
                <ul>
                    <li>استكشف PyTorch في <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p dir="rtl">المؤلف: مروان الحماطي البريد الإلكتروني: marwanalhamaty@gmail.com</p>
        """,
    },
    'en': {
        'app_title': 'METranslator',
        'status_offline': 'Status: Offline',
        'status_loading': 'Status: Loading...',
        'status_running': 'Status: Running',
        'status_error': 'Status: Error',
        'run_server': 'Run Server',
        'stop_server': 'Stop Server',
        'env_setup': 'Environment Setup',
        'settings': 'Settings',
        'download_convert': 'Download & Convert Settings',
        'help': 'Help',
        'to': 'To:',
        'from': 'From:',
        'appearance': 'Appearance',
        'select_theme': 'Select Theme:',
        'select_model': 'Select Translation Model',
        'multilingual_models': 'Multilingual Models',
        'device': 'Device:',
        'server_settings': 'Server Settings',
        'host': 'Host',
        'port': 'Port',
        'translate_text_group': 'Translate Text',
        'source_text': 'Source Text:',
        'translation_label': 'Translation:',
        'translate_btn': 'Translate',
        'clear_btn': 'Clear',
        'font_size': 'Font Size:',
        'close': 'Close',
        'warning': 'Warning',
        'server_running_warning': 'Server is already running. You must stop the server before changing the model or device.',
        'server_running_warning_opus_land': 'Server is already running. You must stop the server before changing the language for OPUS models.',
        'stop_server_first': 'You must stop the server first.',
        'back': 'Back',
        'download_multilingual': 'Download Multilingual Models',
        'download_madlad400': '⬇️ Download MADLAD400 Multilingual Model',
        'download_mbartlarge50': '⬇️ Download MBARTLARGE50',
        'convert_c2': 'Convert to CTranslate2',
        'convert_onnx': 'Convert to ONNX',
        'convert_btn': 'Convert',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Select Languages',
        'download_model': '⬇️ Download Model',
        'output_direction': 'ltr',
        'lang_label': 'Language:',
        'select_lang': 'Interface Language:',
        'help_title': 'METranslator Usage Instructions',
        'confirm': 'Confirm',
        'loading': 'Loading',
        'info': 'Information',
        'error': 'Error',
        'success': 'Success',
        'wait': 'Please wait',
        'alert': 'Alert',
        'server_already_running': 'Server is already running.',
        'download_failed': 'Download failed',
        'model_path_required': 'Model path is required.',
        'model_must_be_downloaded': 'Model must be downloaded first.',
        'server_starting': 'Starting server...',
        'model_msg': 'Model',
        'host_msg': 'Host',
        'port_msg': 'Port',
        'confirm_download_msg': 'Are you sure you want to download the model?',
        'converting_in_progress': 'Conversion in progress...',
        'converting_model_to': 'Converting model to',
        'confirm_conversion_msg': 'Do you really want to start the conversion process?',
        'download_in_progress_warning': 'A download is already in progress.',
        'conversion_in_progress_warning': 'A conversion is already in progress.',
        'setup_in_progress_warning': 'Setup is already in progress.',
        'original_model_not_found': 'Original model not found',
        'download_model_first': 'Please download the model first.',
        'conversion_c2_success': 'Model converted to CTranslate2 successfully.',
        'conversion_onnx_success': 'Model converted to ONNX successfully.',
        'download_madlad400_success': 'MADLAD400 model downloaded successfully.',
        'download_mbartlarge50_success': 'MBARTLARGE50 model downloaded successfully.',
        'download_success_msg': 'Model downloaded successfully.',
        'server_not_active_translation_warning': 'Server is not active. Please start the server first.',
        'server_loading_wait_warning': 'Server is still loading. Please wait.',
        'enter_text_to_translate': 'Please enter text to translate.',
        'failed_to_start_translation': 'Failed to start translation',
        'select_at_least_one_option': 'Please select at least one option.',
        'cannot_create_venv_without_python': 'Cannot create a virtual environment without Python installed.',
        'cannot_install_reqs_without_venv': 'Cannot install libraries without a virtual environment.',
        'environment_setup_title': 'Environment Setup',
        'portable_environment_setup_title': 'Portable Virtual Environment Setup',
        'requirements_type_group': 'Requirements Type',
        'cpu_requirements': 'CPU Requirements',
        'gpu_requirements': 'GPU Requirements (NVIDIA CUDA)',
        'setup_options_group': 'Setup Options',
        'install_python_local': 'Install Python locally',
        'install_python_local_installed': 'Install Python locally (Already installed)',
        'install_python_local_tooltip': 'A portable version of Python will be downloaded and installed inside the app folder',
        'create_virtual_environment': 'Create virtual environment',
        'create_virtual_environment_created': 'Create virtual environment (Already exists)',
        'create_virtual_environment_tooltip': 'Create an isolated environment to install libraries',
        'recreate_virtual_environment': 'Delete and recreate virtual environment',
        'recreate_virtual_environment_tooltip': 'The existing environment will be deleted and recreated from scratch (useful when changing device type)',
        'install_requirements': 'Install necessary libraries',
        'install_requirements_tooltip': 'Install necessary translation and AI libraries',
        'start_setup_btn': 'Start',
        'cancel_btn': 'Cancel',
        'confirm_recreate_venv': 'The current virtual environment will be deleted and recreated. Do you want to continue?',
        'confirm_start_setup': 'Do you want to start the setup process?',
        'confirm_cancel_setup': 'Are you sure you want to cancel the setup process?',
        'venv_virtualenv_not_found': 'System venv not found, trying to use virtualenv...',
        'setting_up_in_progress': 'Setting up...',
        'setting_up_environment': 'Setting up environment...',
        'environment_setup_finished': 'Environment setup finished.',
        'download_in_progress_exit_warning': 'A model download is in progress. Do you want to cancel it before exiting?',
        'download_madlad400_in_progress_exit_warning': 'A madlad400 download is in progress. Do you want to cancel it before exiting?',
        'convert_c2_in_progress_exit_warning': 'A C2 conversion is in progress. Do you want to cancel it before exiting?',
        'convert_onnx_in_progress_exit_warning': 'An ONNX conversion is in progress. Do you want to cancel it before exiting?',
        'convert_mbart_c2_in_progress_exit_warning': 'A MBART C2 conversion is in progress. Do you want to cancel it before exiting?',
        'convert_mbart_onnx_in_progress_exit_warning': 'A MBART ONNX conversion is in progress. Do you want to cancel it before exiting?',
        'verification_in_progress_exit_warning': 'A library verification is in progress. Do you want to cancel it before exiting?',
        'translation_in_progress_exit_warning': 'A translation is in progress. Do you want to cancel it before exiting?',
        'server_not_active': 'Server Offline',
        'server_started_successfully': 'Server started successfully',
        'server_stopped_successfully': 'Server stopped successfully',
        'settings_save_failed': 'Failed to save settings',
        'settings_saved_auto': 'Settings saved automatically',
        'settings_loaded_auto': 'Settings loaded automatically',
        'settings_file_not_found': 'Settings file not found, using defaults',
        'status': 'Status',
        'translating_in_progress': 'Translating...',
        'translating_progress': 'Translation Progress',
        'text_fields_cleared': 'Text fields cleared',
        'translation_successful': 'Translation successful',
        'seconds': 'seconds',
        'translation_error': 'Translation error',
        'translation_cancelled': 'Translation cancelled',
        'translation_started_background': 'Translation started in background',
        'translation_in_progress_cancel': 'A translation is in progress. Do you want to cancel it?',
        'translation_in_progress_cancel_new': 'A translation is in progress. Do you want to cancel it to start a new one?',
        'downloading_in_progress': 'Downloading...',
        'downloading_madlad400_model': 'Downloading MADLAD400 model...',
        'downloading_mbartlarge50_model': 'Downloading MBARTLARGE50 model...',
        'downloading_model_msg': 'Downloading model',
        'conversion_finished_msg': 'Conversion process finished',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 converted to CTranslate2 successfully',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 converted to ONNX successfully',
        'mbartlarge50_original_model_not_found': 'MBARTLARGE50 original model not found',
        'setting_up_progress': 'Setup Progress',
        'warning_thread_termination_failed': 'Warning: Some threads failed to terminate',
        'warning_thread_timeout': 'Warning: Thread wait timeout',
        'python_local_exists': 'Local Python already exists',
        'downloading_python_installer': 'Downloading Python installer...',
        'installing_python': 'Installing Python...',
        'python_install_success': 'Local Python installed successfully',
        'python_install_failed': 'Failed to install Python',
        'fatal_error_venv_active': 'Fatal Error: Cannot delete environment because the program is running through it!',
        'venv_exists': 'Virtual environment already exists',
        'venv_created_success': 'Virtual environment created successfully',
        'venv_creation_failed': 'Failed to create virtual environment',
        'requirements_file_not_found': 'Requirements file not found',
        'installing_requirements_from': 'Installing requirements from',
        'download_madlad400_confirm': 'Do you want to download MADLAD400 model?',
        'download_mbartlarge50_confirm': 'Do you want to download MBARTLARGE50 model?',
        'download_model_specific': 'Download',
        'download_model_tooltip': 'Download model from the internet:',
        'error_cuda_not_available': 'Error: CUDA is not available on the system',
        'error_pytorch_not_installed': 'Error: PyTorch is not installed',
        'error_missing_lib_c2': 'Required library missing for CTranslate2:',
        'libraries_verified_success': 'Libraries verified successfully',
        'error_verifying_libraries': 'Error verifying libraries:',
        'error_deleting_venv': 'Error deleting virtual environment:',
        'starting_conversion_to': 'Starting model conversion to:',
        'converting_model': 'Converting model...',
        'conversion_quant_failed_retry': 'Conversion failed with quantization, retrying without it:',
        'conversion_success_no_quant': 'Conversion successful without quantization',
        'copying_extra_files': 'Copying extra files...',
        'model_converted_success': 'Model converted successfully',
        'error_conversion': 'Conversion error:',
        'error_src_model_not_found': 'Error: Source model folder not found',
        'deleting_old_folder': 'Deleting old folder',
        'starting_mbart_conversion_to': 'Starting mbartlarge50 model conversion to:',
        'saving_tokenizer_files': 'Saving Tokenizer files...',
        'conversion_success': 'Conversion successful',
        'exporting_onnx_wait': 'Exporting model to ONNX (this may take a long time for large models)',
        'warning_ram_requirement': 'Warning: You will need sufficient RAM (at least 16GB).',
        'onnx_export_success_loading_tokenizer': 'Model exported successfully, loading Tokenizer...',
        'saving_raw_model_temp': 'Saving raw model in temporary folder...',
        'quantizing_model': 'Quantizing model:',
        'quantizing_part': 'Quantizing part:',
        'cleaning_temp_files': 'Cleaning temporary files...',
        'saving_model_files': 'Saving model files...',
        'warning_no_onnx_files': 'Warning: No ONNX files found',
        'quantizing': 'Quantizing',
        'error_quant_failed_no_file': 'Quantization failed: No .onnx file created in temp folder for',
        'error_during_quant': 'Error during quantization',
        'error_folder_not_found': 'Folder not found:',
        'error_download_corrupted': 'Download failed: Empty files found:',
        'error_model_path_not_specified': 'Error: Model path not specified',
        'verifying_model_at': 'Verifying model at path:',
        'loading_model_local': 'Final loading of model from local files...',
        'loading_tokenizer': 'Loading Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer loaded successfully',
        'error_loading_tokenizer': 'Error loading Tokenizer:',
        'loading_model': 'Loading Model',
        'model_loaded_success': 'Model loaded successfully',
        'error_loading_model': 'Error loading Model:',
        'download_finished_msg': 'Download finished',
        'model_integrity_verified': 'Model integrity verified successfully',
        'error_verifying_model': 'Error verifying model:',
        'verifying_mbart_at': 'Verifying MBARTLARGE50 model at path:',
        'loading_mbart_local': 'Final loading of MBARTLARGE50 model from local files...',
        'error_verifying_mbart': 'Error verifying MBARTLARGE50 model:',
        'verifying_madlad_at': 'Verifying MADLAD400 model at path:',
        'loading_madlad_local': 'Final loading of MADLAD400 model from local files...',
        'testing_model_on_device': 'Testing model loading on device:',
        'translator_tokenizer_loaded_success': 'Translator and Tokenizer loaded successfully',
        'error_loading_components': 'Error loading components:',
        'error_verifying_madlad': 'Error verifying MADLAD400 model:',
        'download_opus_mt_tooltip': 'Download the selected OPUS-MT model',
        'convert_c2_tooltip': 'Convert the model to the selected CTranslate2 format',
        'convert_onnx_tooltip': 'Convert the model to the selected ONNX format',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Setting Up METranslator:</h2>

        <h3>Step 1: Install Necessary Libraries (Internet Required)</h3>
        <ol>
            <li>Go to Environment Setup.</li>
            <li>Choose your device: CPU for those without NVIDIA GPUs, or GPU for NVIDIA users who want to use CUDA.</li>
            <li>Select other options and click Start.</li>
        </ol>

        <p><b>Note:</b></p>
        <ul>
            <li>If you need to change your device type, select "Delete and Recreate Virtual Environment" to prevent library conflicts.</li>
            <li>Downloading GPU libraries is substantial (approx. 3GB) and may take some time.</li>
        </ul>

        <h3>Step 2: Download and Convert Models (Internet Required)</h3>
        <ol>
            <li>Go to Download & Convert Settings.</li>
            <li>Click Download the Model (choose from opus-mt-tc-big, MADLAD-400-Ct2, or mBART-large-50).</li>
            <li>Click Convert the Model for Your Device (only for opus-mt-tc-big and mBART-large-50).</li>
        </ol>

        <p><b>Note:</b></p>
        <ul>
            <li>For the opus-mt-tc-big Model, you must specify the source and target languages.</li>
            <li>The MADLAD-400-Ct2 Model is already converted to ct2-int8_float16 and does not need further conversion.</li>
            <li>The opus-mt-tc-big Model is approximately 450MB in size.</li>
            <li>The MADLAD-400-Ct2 and mBART-large-50 Models are approximately 3GB each.</li>
        </ul>

        <h3>Step 3: Prepare for Translation</h3>
        <ol>
            <li>Go to Settings ⚙️.</li>
            <li>Select the Model.</li>
            <li>Select the path</li>
            <li>Choose the Device Type (CPU or GPU).</li>
        </ol>

        <p>You are now ready to translate and use the service.</p>

        <h3>How to Use:</h3>
        <p>Simply click Run Server ▶ whenever you need a translation.</p>

        <h3>We extend our heartfelt thanks to these open-source projects:</h3>
        <ul>
            <li>Hugging Face for their AI models and datasets.
                <ul>
                    <li>Explore their offerings at <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Discover specific models like <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Check out MADLAD-400-Ct2 at <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>Learn more about mBART-large-50 at <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python for backend scripting.
                <ul>
                    <li>Visit <a href="https://www.python.org/">Python</a> to learn more.</li>
                </ul>
            </li>
            <li>PyTorch for our machine learning framework.
                <ul>
                    <li>Explore PyTorch at <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Author: Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'fr': {
        'app_title': 'METranslator',
        'status_offline': 'Statut : Hors ligne',
        'status_loading': 'Statut : Chargement...',
        'status_running': 'Statut : En cours',
        'status_error': 'Statut : Erreur',
        'run_server': 'Démarrer le serveur',
        'stop_server': 'Arrêter le serveur',
        'env_setup': 'Configuration de l\'environnement',
        'settings': 'Paramètres',
        'download_convert': 'Téléchargement et conversion',
        'help': 'Aide',
        'to': 'Vers :',
        'from': 'De :',
        'appearance': 'Apparence',
        'select_theme': 'Sélectionner le thème :',
        'select_model': 'Sélectionner le modèle de traduction',
        'multilingual_models': 'Modèles multilingues',
        'device': 'Appareil :',
        'server_settings': 'Paramètres du serveur',
        'host': 'Hôte',
        'port': 'Port',
        'translate_text_group': 'Traduire le texte',
        'source_text': 'Texte source :',
        'translation_label': 'Traduction :',
        'translate_btn': 'Traduire',
        'clear_btn': 'Effacer',
        'font_size': 'Taille de police :',
        'close': 'Fermer',
        'warning': 'Avertissement',
        'server_running_warning': 'Le serveur est déjà en cours d\'exécution. Vous devez arrêter le serveur avant de changer le modèle ou l\'appareil.',
        'server_running_warning_opus_land': 'Le serveur est déjà en cours d\'exécution. Vous devez arrêter le serveur avant de changer la langue pour les modèles OPUS.',
        'stop_server_first': 'Vous devez arrêter le serveur d\'abord.',
        'back': 'Retour',
        'download_multilingual': 'Télécharger les modèles multilingues',
        'download_madlad400': '⬇️ Télécharger le modèle multilingue MADLAD400',
        'download_mbartlarge50': '⬇️ Télécharger MBARTLARGE50',
        'convert_c2': 'Convertir en CTranslate2',
        'convert_onnx': 'Convertir en ONNX',
        'convert_btn': 'Convertir',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Sélectionner les langues',
        'download_model': '⬇️ Télécharger le modèle',
        'output_direction': 'ltr',
        'lang_label': 'Langue :',
        'select_lang': 'Langue de l\'interface :',
        'help_title': 'Instructions d\'utilisation de METranslator',
        'confirm': 'Confirmer',
        'loading': 'Chargement',
        'info': 'Information',
        'error': 'Erreur',
        'success': 'Succès',
        'wait': 'Veuillez patienter',
        'alert': 'Alerte',
        'server_already_running': 'Le serveur est déjà en cours d\'exécution.',
        'download_failed': 'Échec du téléchargement',
        'model_path_required': 'Le chemin du modèle est requis.',
        'model_must_be_downloaded': 'Le modèle doit d\'abord être téléchargé.',
        'server_starting': 'Démarrage du serveur...',
        'model_msg': 'Modèle',
        'host_msg': 'Hôte',
        'port_msg': 'Port',
        'confirm_download_msg': 'Êtes-vous sûr de vouloir télécharger le modèle ?',
        'converting_in_progress': 'Conversion en cours...',
        'converting_model_to': 'Conversion du modèle en',
        'confirm_conversion_msg': 'Voulez-vous vraiment lancer le processus de conversion ?',
        'download_in_progress_warning': 'Un téléchargement est déjà en cours.',
        'conversion_in_progress_warning': 'Une conversion est déjà en cours.',
        'setup_in_progress_warning': 'La configuration est déjà en cours.',
        'original_model_not_found': 'Modèle original introuvable',
        'download_model_first': 'Veuillez d\'abord télécharger le modèle.',
        'conversion_c2_success': 'Modèle converti en CTranslate2 avec succès.',
        'conversion_onnx_success': 'Modèle converti en ONNX avec succès.',
        'download_madlad400_success': 'Modèle MADLAD400 téléchargé avec succès.',
        'download_mbartlarge50_success': 'Modèle MBARTLARGE50 téléchargé avec succès.',
        'download_success_msg': 'Modèle téléchargé avec succès.',
        'server_not_active_translation_warning': 'Le serveur n\'est pas actif. Veuillez d\'abord démarrer le serveur.',
        'server_loading_wait_warning': 'Le serveur est encore en cours de chargement. Veuillez patienter.',
        'enter_text_to_translate': 'Veuillez entrer du texte à traduire.',
        'failed_to_start_translation': 'Échec du démarrage de la traduction',
        'select_at_least_one_option': 'Veuillez sélectionner au moins une option.',
        'cannot_create_venv_without_python': 'Impossible de créer un environnement virtuel sans Python installé.',
        'cannot_install_reqs_without_venv': 'Impossible d\'installer les bibliothèques sans environnement virtuel.',
        'environment_setup_title': 'Configuration de l\'environnement',
        'portable_environment_setup_title': 'Configuration de l\'environnement virtuel portable',
        'requirements_type_group': 'Type de prérequis',
        'cpu_requirements': 'Prérequis CPU',
        'gpu_requirements': 'Prérequis GPU (NVIDIA CUDA)',
        'setup_options_group': 'Options de configuration',
        'install_python_local': 'Installer Python localement',
        'install_python_local_installed': 'Installer Python localement (Déjà installé)',
        'install_python_local_tooltip': 'Une version portable de Python sera téléchargée et installée dans le dossier de l\'application',
        'create_virtual_environment': 'Créer un environnement virtuel',
        'create_virtual_environment_created': 'Créer un environnement virtuel (Déjà existant)',
        'create_virtual_environment_tooltip': 'Créer un environnement isolé pour installer les bibliothèques',
        'recreate_virtual_environment': 'Supprimer et recréer l\'environnement virtuel',
        'recreate_virtual_environment_tooltip': 'L\'environnement existant sera supprimé et recréé à partir de zéro (utile lors du changement de type d\'appareil)',
        'install_requirements': 'Installer les bibliothèques nécessaires',
        'install_requirements_tooltip': 'Installer les bibliothèques nécessaires de traduction et d\'IA',
        'start_setup_btn': 'Démarrer',
        'cancel_btn': 'Annuler',
        'confirm_recreate_venv': 'L\'environnement virtuel actuel sera supprimé et recréé. Voulez-vous continuer ?',
        'confirm_start_setup': 'Voulez-vous démarrer le processus de configuration ?',
        'confirm_cancel_setup': 'Êtes-vous sûr de vouloir annuler le processus de configuration ?',
        'venv_virtualenv_not_found': 'venv du système introuvable, tentative d\'utilisation de virtualenv...',
        'setting_up_in_progress': 'Configuration en cours...',
        'setting_up_environment': 'Configuration de l\'environnement...',
        'environment_setup_finished': 'Configuration de l\'environnement terminée.',
        'download_in_progress_exit_warning': 'Un téléchargement de modèle est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'download_madlad400_in_progress_exit_warning': 'Un téléchargement madlad400 est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'convert_c2_in_progress_exit_warning': 'Une conversion C2 est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'convert_onnx_in_progress_exit_warning': 'Une conversion ONNX est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'convert_mbart_c2_in_progress_exit_warning': 'Une conversion MBART C2 est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'convert_mbart_onnx_in_progress_exit_warning': 'Une conversion MBART ONNX est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'verification_in_progress_exit_warning': 'Une vérification de bibliothèque est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'translation_in_progress_exit_warning': 'Une traduction est en cours. Voulez-vous l\'annuler avant de quitter ?',
        'server_not_active': 'Serveur hors ligne',
        'convert_mbartlarge50_to_format_confirm': 'Voulez-vous convertir le modèle MBARTLARGE50 en',
        'may_take_time': 'Cela peut prendre du temps',
        'convert_model_to_format_confirm': 'Voulez-vous convertir le modèle en',
        'server_started_successfully': 'Serveur démarré avec succès',
        'server_stopped_successfully': 'Serveur arrêté avec succès',
        'settings_save_failed': 'Échec de l\'enregistrement des paramètres',
        'settings_saved_auto': 'Paramètres enregistrés automatiquement',
        'settings_loaded_auto': 'Paramètres chargés automatiquement',
        'settings_file_not_found': 'Fichier de paramètres introuvable, utilisation des valeurs par défaut',
        'status': 'Statut',
        'translating_in_progress': 'Traduction en cours...',
        'translating_progress': 'Progression de la traduction',
        'text_fields_cleared': 'Champs de texte effacés',
        'translation_successful': 'Traduction réussie',
        'seconds': 'secondes',
        'translation_error': 'Erreur de traduction',
        'translation_cancelled': 'Traduction annulée',
        'translation_started_background': 'Traduction démarrée en arrière-plan',
        'translation_in_progress_cancel': 'Une traduction est en cours. Voulez-vous l\'annuler ?',
        'translation_in_progress_cancel_new': 'Une traduction est en cours. Voulez-vous l\'annuler pour en commencer une nouvelle ?',
        'downloading_in_progress': 'Téléchargement...',
        'downloading_madlad400_model': 'Téléchargement du modèle MADLAD400...',
        'downloading_mbartlarge50_model': 'Téléchargement du modèle MBARTLARGE50...',
        'downloading_model_msg': 'Téléchargement du modèle',
        'conversion_finished_msg': 'Processus de conversion terminé',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 converti en CTranslate2 avec succès',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 converti en ONNX avec succès',
        'mbartlarge50_original_model_not_found': 'Modèle original MBARTLARGE50 introuvable',
        'setting_up_progress': 'Progression de la configuration',
        'warning_thread_termination_failed': 'Avertissement : Certains threads n\'ont pas pu se terminer',
        'warning_thread_timeout': 'Avertissement : Délai d\'attente du thread expiré',
        'python_local_exists': 'Python local existe déjà',
        'downloading_python_installer': 'Téléchargement de l\'installateur Python...',
        'installing_python': 'Installation de Python...',
        'python_install_success': 'Python local installé avec succès',
        'python_install_failed': 'Échec de l\'installation de Python',
        'fatal_error_venv_active': 'Erreur fatale : Impossible de supprimer l\'environnement car le programme tourne dessus !',
        'venv_exists': 'L\'environnement virtuel existe déjà',
        'venv_created_success': 'Environnement virtuel créé avec succès',
        'venv_creation_failed': 'Échec de la création de l\'environnement virtuel',
        'requirements_file_not_found': 'Fichier des prérequis introuvable',
        'installing_requirements_from': 'Installation des prérequis depuis',
        'download_madlad400_confirm': 'Voulez-vous télécharger le modèle MADLAD400 ?',
        'download_mbartlarge50_confirm': 'Voulez-vous télécharger le modèle MBARTLARGE50 ?',
        'download_model_specific': 'Télécharger',
        'download_model_tooltip': 'Télécharger le modèle depuis Internet :',
        'error_cuda_not_available': 'Erreur : CUDA n\'est pas disponible sur le système',
        'error_pytorch_not_installed': 'Erreur : PyTorch n\'est pas installé',
        'error_missing_lib_c2': 'Bibliothèque requise manquante pour CTranslate2 :',
        'libraries_verified_success': 'Bibliothèques vérifiées avec succès',
        'error_verifying_libraries': 'Erreur lors de la vérification des bibliothèques :',
        'error_deleting_venv': 'Erreur lors de la suppression de l\'environnement virtuel :',
        'starting_conversion_to': 'Démarrage de la conversion du modèle vers :',
        'converting_model': 'Conversion du modèle...',
        'conversion_quant_failed_retry': 'Échec de la conversion avec quantification, nouvelle tentative sans :',
        'conversion_success_no_quant': 'Conversion réussie sans quantification',
        'copying_extra_files': 'Copie des fichiers supplémentaires...',
        'model_converted_success': 'Modèle converti avec succès',
        'error_conversion': 'Erreur de conversion :',
        'error_src_model_not_found': 'Erreur : Dossier du modèle source introuvable',
        'deleting_old_folder': 'Suppression de l\'ancien dossier',
        'starting_mbart_conversion_to': 'Démarrage de la conversion du modèle mbartlarge50 vers :',
        'saving_tokenizer_files': 'Enregistrement des fichiers Tokenizer...',
        'conversion_success': 'Conversion réussie',
        'exporting_onnx_wait': 'Exportation du modèle vers ONNX (cela peut prendre du temps pour les grands modèles)',
        'warning_ram_requirement': 'Avertissement : Vous aurez besoin de suffisamment de RAM (au moins 16 Go).',
        'onnx_export_success_loading_tokenizer': 'Modèle exporté avec succès, chargement du Tokenizer...',
        'saving_raw_model_temp': 'Enregistrement du modèle brut dans un dossier temporaire...',
        'quantizing_model': 'Quantification du modèle :',
        'quantizing_part': 'Quantification de la partie :',
        'cleaning_temp_files': 'Nettoyage des fichiers temporaires...',
        'saving_model_files': 'Enregistrement des fichiers du modèle...',
        'warning_no_onnx_files': 'Avertissement : Aucun fichier ONNX trouvé',
        'quantizing': 'Quantification',
        'error_quant_failed_no_file': 'Échec de la quantification : Aucun fichier .onnx créé dans le dossier temporaire pour',
        'error_during_quant': 'Erreur lors de la quantification',
        'error_folder_not_found': 'Dossier introuvable :',
        'error_download_corrupted': 'Échec du téléchargement : Fichiers vides trouvés :',
        'error_model_path_not_specified': 'Erreur : Chemin du modèle non spécifié',
        'verifying_model_at': 'Vérification du modèle à l\'emplacement :',
        'loading_model_local': 'Chargement final du modèle depuis les fichiers locaux...',
        'loading_tokenizer': 'Chargement du Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer chargé avec succès',
        'error_loading_tokenizer': 'Erreur lors du chargement du Tokenizer :',
        'loading_model': 'Chargement du modèle',
        'model_loaded_success': 'Modèle chargé avec succès',
        'error_loading_model': 'Erreur lors du chargement du modèle :',
        'download_finished_msg': 'Téléchargement terminé',
        'model_integrity_verified': 'Intégrité du modèle vérifiée avec succès',
        'error_verifying_model': 'Erreur lors de la vérification du modèle :',
        'verifying_mbart_at': 'Vérification du modèle MBARTLARGE50 à l\'emplacement :',
        'loading_mbart_local': 'Chargement final du modèle MBARTLARGE50 depuis les fichiers locaux...',
        'error_verifying_mbart': 'Erreur lors de la vérification du modèle MBARTLARGE50 :',
        'verifying_madlad_at': 'Vérification du modèle MADLAD400 à l\'emplacement :',
        'loading_madlad_local': 'Chargement final du modèle MADLAD400 depuis les fichiers locaux...',
        'testing_model_on_device': 'Test du chargement du modèle sur l\'appareil :',
        'translator_tokenizer_loaded_success': 'Traducteur et Tokenizer chargés avec succès',
        'error_loading_components': 'Erreur lors du chargement des composants :',
        'error_verifying_madlad': 'Erreur lors de la vérification du modèle MADLAD400 :',
        'download_opus_mt_tooltip': 'Télécharger le modèle OPUS-MT sélectionné',
        'convert_c2_tooltip': 'Convertir le modèle au format CTranslate2 sélectionné',
        'convert_onnx_tooltip': 'Convertir le modèle au format ONNX sélectionné',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Configuration de METranslator :</h2>

        <h3>Étape 1 : Installer les bibliothèques nécessaires (Internet requis)</h3>
        <ol>
            <li>Accédez à la Configuration de l'environnement.</li>
            <li>Choisissez votre appareil : CPU pour ceux qui n'ont pas de GPU NVIDIA, ou GPU pour les utilisateurs de NVIDIA qui souhaitent utiliser CUDA.</li>
            <li>Sélectionnez les autres options et cliquez sur Démarrer.</li>
        </ol>

        <p><b>Note :</b></p>
        <ul>
            <li>Si vous devez changer de type d'appareil, sélectionnez « Supprimer et recréer l'environnement virtuel » pour éviter les conflits de bibliothèques.</li>
            <li>Le téléchargement des bibliothèques GPU est conséquent (environ 3 Go) et peut prendre un certain temps.</li>
        </ul>

        <h3>Étape 2 : Télécharger et convertir les modèles (Internet requis)</h3>
        <ol>
            <li>Accédez aux Paramètres de téléchargement et de conversion.</li>
            <li>Cliquez sur Télécharger le modèle (choisissez parmi opus-mt-tc-big, MADLAD-400-Ct2 ou mBART-large-50).</li>
            <li>Cliquez sur Convertir le modèle pour votre appareil (uniquement pour opus-mt-tc-big et mBART-large-50).</li>
        </ol>

        <p><b>Note :</b></p>
        <ul>
            <li>Pour le modèle opus-mt-tc-big, vous devez spécifier les langues source et cible.</li>
            <li>Le modèle MADLAD-400-Ct2 est déjà converti en ct2-int8_float16 et ne nécessite aucune conversion supplémentaire.</li>
            <li>Le modèle opus-mt-tc-big fait environ 450 Mo.</li>
            <li>Les modèles MADLAD-400-Ct2 et mBART-large-50 font environ 3 Go chacun.</li>
        </ul>

        <h3>Étape 3 : Préparer la traduction</h3>
        <ol>
            <li>Accédez aux Paramètres ⚙️.</li>
            <li>Sélectionnez le modèle.</li>
            <li>Sélectionnez le chemin.</li>
            <li>Choisissez le type d'appareil (CPU ou GPU).</li>
        </ol>

        <p>Vous êtes maintenant prêt à traduire et à utiliser le service.</p>

        <h3>Comment utiliser :</h3>
        <p>Cliquez simplement sur Démarrer le serveur ▶ chaque fois que vous avez besoin d'une traduction.</p>

        <h3>Nous adressons nos sincères remerciements à ces projets open-source :</h3>
        <ul>
            <li>Hugging Face pour leurs modèles d'IA et leurs ensembles de données.
                <ul>
                    <li>Explorez leurs offres sur <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Découvrez des modèles spécifiques comme <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Consultez MADLAD-400-Ct2 sur <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>En savoir plus sur mBART-large-50 sur <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python pour le scripting backend.
                <ul>
                    <li>Visitez <a href="https://www.python.org/">Python</a> pour en savoir plus.</li>
                </ul>
            </li>
            <li>PyTorch pour notre framework d'apprentissage automatique.
                <ul>
                    <li>Explorez PyTorch sur <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Auteur : Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'de': {
        'app_title': 'METranslator',
        'status_offline': 'Status: Offline',
        'status_loading': 'Status: Laden...',
        'status_running': 'Status: Läuft',
        'status_error': 'Status: Fehler',
        'run_server': 'Server starten',
        'stop_server': 'Server stoppen',
        'env_setup': 'Umgebungseinrichtung',
        'settings': 'Einstellungen',
        'download_convert': 'Herunterladen & Konvertieren',
        'help': 'Hilfe',
        'to': 'An:',
        'from': 'Von:',
        'appearance': 'Erscheinungsbild',
        'select_theme': 'Design auswählen:',
        'select_model': 'Übersetzungsmodell auswählen',
        'multilingual_models': 'Mehrsprachige Modelle',
        'device': 'Gerät:',
        'server_settings': 'Servereinstellungen',
        'host': 'Host',
        'port': 'Port',
        'translate_text_group': 'Text übersetzen',
        'source_text': 'Quelltext:',
        'translation_label': 'Übersetzung:',
        'translate_btn': 'Übersetzen',
        'clear_btn': 'Löschen',
        'font_size': 'Schriftgröße:',
        'close': 'Schließen',
        'warning': 'Warnung',
        'server_running_warning': 'Server läuft bereits. Sie müssen den Server stoppen, bevor Sie das Modell oder das Gerät ändern.',
        'server_running_warning_opus_land': 'Server läuft bereits. Sie müssen den Server stoppen, bevor Sie die Sprache für OPUS-Modelle ändern.',
        'stop_server_first': 'Sie müssen zuerst den Server stoppen.',
        'back': 'Zurück',
        'download_multilingual': 'Mehrsprachige Modelle herunterladen',
        'download_madlad400': '⬇️ MADLAD400 mehrsprachiges Modell herunterladen',
        'download_mbartlarge50': '⬇️ MBARTLARGE50 herunterladen',
        'convert_c2': 'In CTranslate2 konvertieren',
        'convert_onnx': 'In ONNX konvertieren',
        'convert_btn': 'Konvertieren',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Sprachen auswählen',
        'download_model': '⬇️ Modell herunterladen',
        'output_direction': 'ltr',
        'lang_label': 'Sprache:',
        'select_lang': 'Oberflächensprache:',
        'help_title': 'METranslator Bedienungsanleitung',
        'confirm': 'Bestätigen',
        'loading': 'Laden',
        'info': 'Information',
        'error': 'Fehler',
        'success': 'Erfolg',
        'wait': 'Bitte warten',
        'alert': 'Alarm',
        'server_already_running': 'Server läuft bereits.',
        'download_failed': 'Download fehlgeschlagen',
        'model_path_required': 'Modellpfad ist erforderlich.',
        'model_must_be_downloaded': 'Modell muss zuerst heruntergeladen werden.',
        'server_starting': 'Server wird gestartet...',
        'model_msg': 'Modell',
        'host_msg': 'Host',
        'port_msg': 'Port',
        'confirm_download_msg': 'Möchten Sie das Modell wirklich herunterladen?',
        'converting_in_progress': 'Konvertierung läuft...',
        'converting_model_to': 'Konvertiere Modell nach',
        'confirm_conversion_msg': 'Wollen Sie wirklich den Konvertierungsprozess starten?',
        'download_in_progress_warning': 'Ein Download läuft bereits.',
        'conversion_in_progress_warning': 'Eine Konvertierung läuft bereits.',
        'setup_in_progress_warning': 'Einrichtung läuft bereits.',
        'original_model_not_found': 'Originalmodell nicht gefunden',
        'download_model_first': 'Bitte laden Sie zuerst das Modell herunter.',
        'conversion_c2_success': 'Modell erfolgreich in CTranslate2 konvertiert.',
        'conversion_onnx_success': 'Modell erfolgreich in ONNX konvertiert.',
        'download_madlad400_success': 'MADLAD400-Modell erfolgreich heruntergeladen.',
        'download_mbartlarge50_success': 'MBARTLARGE50-Modell erfolgreich heruntergeladen.',
        'download_success_msg': 'Modell erfolgreich heruntergeladen.',
        'server_not_active_translation_warning': 'Server ist nicht aktiv. Bitte starten Sie zuerst den Server.',
        'server_loading_wait_warning': 'Server lädt noch. Bitte warten.',
        'enter_text_to_translate': 'Bitte Text zum Übersetzen eingeben.',
        'failed_to_start_translation': 'Start der Übersetzung fehlgeschlagen',
        'select_at_least_one_option': 'Bitte wählen Sie mindestens eine Option aus.',
        'cannot_create_venv_without_python': 'Kann ohne installiertes Python keine virtuelle Umgebung erstellen.',
        'cannot_install_reqs_without_venv': 'Kann ohne virtuelle Umgebung keine Bibliotheken installieren.',
        'environment_setup_title': 'Umgebungseinrichtung',
        'portable_environment_setup_title': 'Einrichtung der portablen virtuellen Umgebung',
        'requirements_type_group': 'Anforderungstyp',
        'cpu_requirements': 'CPU-Anforderungen',
        'gpu_requirements': 'GPU-Anforderungen (NVIDIA CUDA)',
        'setup_options_group': 'Einrichtungsoptionen',
        'install_python_local': 'Python lokal installieren',
        'install_python_local_installed': 'Python lokal installieren (Bereits installiert)',
        'install_python_local_tooltip': 'Eine portable Version von Python wird im App-Ordner heruntergeladen und installiert',
        'create_virtual_environment': 'Virtuelle Umgebung erstellen',
        'create_virtual_environment_created': 'Virtuelle Umgebung erstellen (Existiert bereits)',
        'create_virtual_environment_tooltip': 'Eine isolierte Umgebung zum Installieren von Bibliotheken erstellen',
        'recreate_virtual_environment': 'Virtuelle Umgebung löschen und neu erstellen',
        'recreate_virtual_environment_tooltip': 'Die vorhandene Umgebung wird gelöscht und von Grund auf neu erstellt (nützlich beim Wechsel des Gerätetyps)',
        'install_requirements': 'Erforderliche Bibliotheken installieren',
        'install_requirements_tooltip': 'Erforderliche Übersetzungs- und KI-Bibliotheken installieren',
        'start_setup_btn': 'Starten',
        'cancel_btn': 'Abbrechen',
        'confirm_recreate_venv': 'Die aktuelle virtuelle Umgebung wird gelöscht und neu erstellt. Möchten Sie fortfahren?',
        'confirm_start_setup': 'Möchten Sie den Einrichtungsprozess starten?',
        'confirm_cancel_setup': 'Sind Sie sicher, dass Sie den Einrichtungsprozess abbrechen möchten?',
        'venv_virtualenv_not_found': 'System-venv nicht gefunden, Versuch virtualenv zu nutzen...',
        'setting_up_in_progress': 'Einrichtung läuft...',
        'setting_up_environment': 'Umgebung wird eingerichtet...',
        'environment_setup_finished': 'Umgebungseinrichtung abgeschlossen.',
        'download_in_progress_exit_warning': 'Ein Modell-Download läuft. Wollen Sie ihn vor dem Beenden abbrechen?',
        'download_madlad400_in_progress_exit_warning': 'Ein madlad400-Download läuft. Wollen Sie ihn vor dem Beenden abbrechen?',
        'convert_c2_in_progress_exit_warning': 'Eine C2-Konvertierung läuft. Wollen Sie sie vor dem Beenden abbrechen?',
        'convert_onnx_in_progress_exit_warning': 'Eine ONNX-Konvertierung läuft. Wollen Sie sie vor dem Beenden abbrechen?',
        'convert_mbart_c2_in_progress_exit_warning': 'Eine MBART C2-Konvertierung läuft. Wollen Sie sie vor dem Beenden abbrechen?',
        'convert_mbart_onnx_in_progress_exit_warning': 'Eine MBART ONNX-Konvertierung läuft. Wollen Sie sie vor dem Beenden abbrechen?',
        'verification_in_progress_exit_warning': 'Eine Bibliotheksüberprüfung läuft. Wollen Sie sie vor dem Beenden abbrechen?',
        'translation_in_progress_exit_warning': 'Eine Übersetzung läuft. Wollen Sie sie vor dem Beenden abbrechen?',
        'server_not_active': 'Server Offline',
        'convert_mbartlarge50_to_format_confirm': 'Wollen Sie das MBARTLARGE50-Modell konvertieren nach',
        'may_take_time': 'Dies kann einige Zeit dauern',
        'convert_model_to_format_confirm': 'Wollen Sie das Modell konvertieren nach',
        'server_started_successfully': 'Server erfolgreich gestartet',
        'server_stopped_successfully': 'Server erfolgreich gestoppt',
        'settings_save_failed': 'Speichern der Einstellungen fehlgeschlagen',
        'settings_saved_auto': 'Einstellungen automatisch gespeichert',
        'settings_loaded_auto': 'Einstellungen automatisch geladen',
        'settings_file_not_found': 'Einstellungsdatei nicht gefunden, Standardwerte werden verwendet',
        'status': 'Status',
        'translating_in_progress': 'Übersetzung läuft...',
        'translating_progress': 'Fortschritt der Übersetzung',
        'text_fields_cleared': 'Textfelder gelöscht',
        'translation_successful': 'Übersetzung erfolgreich',
        'seconds': 'Sekunden',
        'translation_error': 'Übersetzungsfehler',
        'translation_cancelled': 'Übersetzung abgebrochen',
        'translation_started_background': 'Übersetzung im Hintergrund gestartet',
        'translation_in_progress_cancel': 'Eine Übersetzung läuft. Wollen Sie sie abbrechen?',
        'translation_in_progress_cancel_new': 'Eine Übersetzung läuft. Wollen Sie sie abbrechen, um eine neue zu starten?',
        'downloading_in_progress': 'Herunterladen...',
        'downloading_madlad400_model': 'MADLAD400-Modell herunterladen...',
        'downloading_mbartlarge50_model': 'MBARTLARGE50-Modell herunterladen...',
        'downloading_model_msg': 'Modell herunterladen',
        'conversion_finished_msg': 'Konvertierungsprozess abgeschlossen',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 erfolgreich in CTranslate2 konvertiert',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 erfolgreich in ONNX konvertiert',
        'mbartlarge50_original_model_not_found': 'MBARTLARGE50-Originalmodell nicht gefunden',
        'setting_up_progress': 'Fortschritt der Einrichtung',
        'warning_thread_termination_failed': 'Warnung: Einige Threads konnten nicht beendet werden',
        'warning_thread_timeout': 'Warnung: Timeout beim Warten auf Threads',
        'python_local_exists': 'Lokales Python existiert bereits',
        'downloading_python_installer': 'Python-Installationsprogramm herunterladen...',
        'installing_python': 'Python wird installiert...',
        'python_install_success': 'Lokales Python erfolgreich installiert',
        'python_install_failed': 'Python-Installation fehlgeschlagen',
        'fatal_error_venv_active': 'Schwerwiegender Fehler: Umgebung kann nicht gelöscht werden, da das Programm darüber läuft!',
        'venv_exists': 'Virtuelle Umgebung existiert bereits',
        'venv_created_success': 'Virtuelle Umgebung erfolgreich erstellt',
        'venv_creation_failed': 'Erstellung der virtuellen Umgebung fehlgeschlagen',
        'requirements_file_not_found': 'Anforderungsdatei nicht gefunden',
        'installing_requirements_from': 'Installation der Anforderungen von',
        'download_madlad400_confirm': 'Möchten Sie das MADLAD400-Modell herunterladen?',
        'download_mbartlarge50_confirm': 'Möchten Sie das MBARTLARGE50-Modell herunterladen?',
        'download_model_specific': 'Herunterladen',
        'download_model_tooltip': 'Modell aus dem Internet herunterladen:',
        'error_cuda_not_available': 'Fehler: CUDA ist auf dem System nicht verfügbar',
        'error_pytorch_not_installed': 'Fehler: PyTorch ist nicht installiert',
        'error_missing_lib_c2': 'Erforderliche Bibliothek für CTranslate2 fehlt:',
        'libraries_verified_success': 'Bibliotheken erfolgreich überprüft',
        'error_verifying_libraries': 'Fehler beim Überprüfen der Bibliotheken:',
        'error_deleting_venv': 'Fehler beim Löschen der virtuellen Umgebung:',
        'starting_conversion_to': 'Start der Modellkonvertierung nach:',
        'converting_model': 'Modell konvertieren...',
        'conversion_quant_failed_retry': 'Konvertierung mit Quantisierung fehlgeschlagen, erneuter Versuch ohne:',
        'conversion_success_no_quant': 'Konvertierung ohne Quantisierung erfolgreich',
        'copying_extra_files': 'Zusätzliche Dateien kopieren...',
        'model_converted_success': 'Modell erfolgreich konvertiert',
        'error_conversion': 'Konvertierungsfehler:',
        'error_src_model_not_found': 'Fehler: Quellmodellordner nicht gefunden',
        'deleting_old_folder': 'Alten Ordner löschen',
        'starting_mbart_conversion_to': 'Start der mbartlarge50-Modellkonvertierung nach:',
        'saving_tokenizer_files': 'Tokenizer-Dateien speichern...',
        'conversion_success': 'Konvertierung erfolgreich',
        'exporting_onnx_wait': 'Modell nach ONNX exportieren (dies kann bei großen Modellen lange dauern)',
        'warning_ram_requirement': 'Warnung: Sie benötigen ausreichend RAM (mindestens 16GB).',
        'onnx_export_success_loading_tokenizer': 'Modell erfolgreich exportiert, Tokenizer wird geladen...',
        'saving_raw_model_temp': 'Rohmodell in temporären Ordner speichern...',
        'quantizing_model': 'Modell quantisieren:',
        'quantizing_part': 'Teil quantisieren:',
        'cleaning_temp_files': 'Temporäre Dateien bereinigen...',
        'saving_model_files': 'Modell-Dateien speichern...',
        'warning_no_onnx_files': 'Warnung: Keine ONNX-Dateien gefunden',
        'quantizing': 'Quantisierung',
        'error_quant_failed_no_file': 'Quantisierung fehlgeschlagen: Keine .onnx-Datei im temporären Ordner erstellt für',
        'error_during_quant': 'Fehler während der Quantisierung',
        'error_folder_not_found': 'Ordner nicht gefunden:',
        'error_download_corrupted': 'Download fehlgeschlagen: Leere Dateien gefunden:',
        'error_model_path_not_specified': 'Fehler: Modellpfad nicht angegeben',
        'verifying_model_at': 'Modell unter Pfad überprüfen:',
        'loading_model_local': 'Endgültiges Laden des Modells aus lokalen Dateien...',
        'loading_tokenizer': 'Tokenizer laden',
        'tokenizer_loaded_success': 'Tokenizer erfolgreich geladen',
        'error_loading_tokenizer': 'Fehler beim Laden des Tokenizers:',
        'loading_model': 'Modell laden',
        'model_loaded_success': 'Modell erfolgreich geladen',
        'error_loading_model': 'Fehler beim Laden des Modells:',
        'download_finished_msg': 'Download beendet',
        'model_integrity_verified': 'Modellintegrität erfolgreich überprüft',
        'error_verifying_model': 'Fehler beim Überprüfen des Modells:',
        'verifying_mbart_at': 'MBARTLARGE50-Modell unter Pfad überprüfen:',
        'loading_mbart_local': 'Endgültiges Laden des MBARTLARGE50-Modells aus lokalen Dateien...',
        'error_verifying_mbart': 'Fehler beim Überprüfen des MBARTLARGE50-Modells:',
        'verifying_madlad_at': 'MADLAD400-Modell unter Pfad überprüfen:',
        'loading_madlad_local': 'Endgültiges Laden des MADLAD400-Modells aus lokalen Dateien...',
        'testing_model_on_device': 'Testen des Modellladens auf Gerät:',
        'translator_tokenizer_loaded_success': 'Übersetzer und Tokenizer erfolgreich geladen',
        'error_loading_components': 'Fehler beim Laden der Komponenten:',
        'error_verifying_madlad': 'Fehler beim Überprüfen des MADLAD400-Modells:',
        'download_opus_mt_tooltip': 'Ausgewähltes OPUS-MT-Modell herunterladen',
        'convert_c2_tooltip': 'Modell in das ausgewählte CTranslate2-Format konvertieren',
        'convert_onnx_tooltip': 'Modell in das ausgewählte ONNX-Format konvertieren',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Einrichtung von METranslator:</h2>

        <h3>Schritt 1: Notwendige Bibliotheken installieren (Internet erforderlich)</h3>
        <ol>
            <li>Gehen Sie zur Umgebungseinrichtung.</li>
            <li>Wählen Sie Ihr Gerät: CPU für Personen ohne NVIDIA-GPUs oder GPU für NVIDIA-Benutzer, die CUDA verwenden möchten.</li>
            <li>Wählen Sie andere Optionen und klicken Sie auf Starten.</li>
        </ol>

        <p><b>Hinweis:</b></p>
        <ul>
            <li>Wenn Sie Ihren Gerätetyp ändern müssen, wählen Sie „Virtuelle Umgebung löschen und neu erstellen“, um Bibliothekskonflikte zu vermeiden.</li>
            <li>Das Herunterladen von GPU-Bibliotheken ist umfangreich (ca. 3 GB) und kann einige Zeit in Anspruch nehmen.</li>
        </ul>

        <h3>Schritt 2: Modelle herunterladen und konvertieren (Internet erforderlich)</h3>
        <ol>
            <li>Gehen Sie zu den Download- und Konvertierungseinstellungen.</li>
            <li>Klicken Sie auf Modell herunterladen (wählen Sie zwischen opus-mt-tc-big, MADLAD-400-Ct2 oder mBART-large-50).</li>
            <li>Klicken Sie auf Modell für Ihr Gerät konvertieren (nur für opus-mt-tc-big und mBART-large-50).</li>
        </ol>

        <p><b>Hinweis:</b></p>
        <ul>
            <li>Für das opus-mt-tc-big-Modell müssen Sie die Quell- und Zielsprache angeben.</li>
            <li>Das MADLAD-400-Ct2-Modell ist bereits in ct2-int8_float16 konvertiert und benötigt keine weitere Konvertierung.</li>
            <li>Das opus-mt-tc-big-Modell ist ca. 450 MB groß.</li>
            <li>Die Modelle MADLAD-400-Ct2 und mBART-large-50 sind jeweils ca. 3 GB groß.</li>
        </ul>

        <h3>Schritt 3: Vorbereitung auf die Übersetzung</h3>
        <ol>
            <li>Gehen Sie zu den Einstellungen ⚙️.</li>
            <li>Wählen Sie das Modell aus.</li>
            <li>Wählen Sie den Pfad aus.</li>
            <li>Wählen Sie den Gerätetyp (CPU oder GPU).</li>
        </ol>

        <p>Sie sind nun bereit für die Übersetzung und die Nutzung des Dienstes.</p>

        <h3>Anwendung:</h3>
        <p>Klicken Sie einfach auf Server starten ▶, wann immer Sie eine Übersetzung benötigen.</p>

        <h3>Wir bedanken uns herzlich bei diesen Open-Source-Projekten:</h3>
        <ul>
            <li>Hugging Face für ihre KI-Modelle und Datensätze.
                <ul>
                    <li>Erkunden Sie deren Angebote unter <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Entdecken Sie spezifische Modelle wie <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Schauen Sie sich MADLAD-400-Ct2 unter <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a> an.</li>
                    <li>Erfahren Sie mehr über mBART-large-50 unter <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python für Backend-Scripting.
                <ul>
                    <li>Besuchen Sie <a href="https://www.python.org/">Python</a>, um mehr zu erfahren.</li>
                </ul>
            </li>
            <li>PyTorch für unser Machine-Learning-Framework.
                <ul>
                    <li>Erkunden Sie PyTorch unter <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Autor: Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'es': {
        'app_title': 'METranslator',
        'status_offline': 'Estado: Desconectado',
        'status_loading': 'Estado: Cargando...',
        'status_running': 'Estado: En ejecución',
        'status_error': 'Estado: Error',
        'run_server': 'Iniciar servidor',
        'stop_server': 'Detener servidor',
        'env_setup': 'Configuración del entorno',
        'settings': 'Configuración',
        'download_convert': 'Descargar y Convertir',
        'help': 'Ayuda',
        'to': 'A:',
        'from': 'De:',
        'appearance': 'Apariencia',
        'select_theme': 'Seleccionar tema:',
        'select_model': 'Seleccionar modelo de traducción',
        'multilingual_models': 'Modelos multilingües',
        'device': 'Dispositivo:',
        'server_settings': 'Configuración del servidor',
        'host': 'Host',
        'port': 'Puerto',
        'translate_text_group': 'Traducir texto',
        'source_text': 'Texto original:',
        'translation_label': 'Traducción:',
        'translate_btn': 'Traducir',
        'clear_btn': 'Limpiar',
        'font_size': 'Tamaño de fuente:',
        'close': 'Cerrar',
        'warning': 'Advertencia',
        'server_running_warning': 'El servidor ya está ejecutándose. Debe detener el servidor antes de cambiar el modelo o el dispositivo.',
        'server_running_warning_opus_land': 'El servidor ya está ejecutándose. Debe detener el servidor antes de cambiar el idioma para los modelos OPUS.',
        'stop_server_first': 'Debe detener el servidor primero.',
        'back': 'Atrás',
        'download_multilingual': 'Descargar modelos multilingües',
        'download_madlad400': '⬇️ Descargar modelo multilingüe MADLAD400',
        'download_mbartlarge50': '⬇️ Descargar MBARTLARGE50',
        'convert_c2': 'Convertir a CTranslate2',
        'convert_onnx': 'Convertir a ONNX',
        'convert_btn': 'Convertir',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Seleccionar idiomas',
        'download_model': '⬇️ Descargar modelo',
        'output_direction': 'ltr',
        'lang_label': 'Idioma:',
        'select_lang': 'Idioma de la interfaz:',
        'help_title': 'Instrucciones de uso de METranslator',
        'confirm': 'Confirmar',
        'loading': 'Cargando',
        'info': 'Información',
        'error': 'Error',
        'success': 'Éxito',
        'wait': 'Espere por favor',
        'alert': 'Alerta',
        'server_already_running': 'El servidor ya está en ejecución.',
        'download_failed': 'Descarga fallida',
        'model_path_required': 'Se requiere la ruta del modelo.',
        'model_must_be_downloaded': 'El modelo debe descargarse primero.',
        'server_starting': 'Iniciando servidor...',
        'model_msg': 'Modelo',
        'host_msg': 'Host',
        'port_msg': 'Puerto',
        'confirm_download_msg': '¿Está seguro de que desea descargar el modelo?',
        'converting_in_progress': 'Conversión en curso...',
        'converting_model_to': 'Convirtiendo modelo a',
        'confirm_conversion_msg': '¿Realmente desea iniciar el proceso de conversión?',
        'download_in_progress_warning': 'Ya hay una descarga en curso.',
        'conversion_in_progress_warning': 'Ya hay una conversión en curso.',
        'setup_in_progress_warning': 'La configuración ya está en curso.',
        'original_model_not_found': 'Modelo original no encontrado',
        'download_model_first': 'Por favor, descargue el modelo primero.',
        'conversion_c2_success': 'Modelo convertido a CTranslate2 con éxito.',
        'conversion_onnx_success': 'Modelo convertido a ONNX con éxito.',
        'download_madlad400_success': 'Modelo MADLAD400 descargado con éxito.',
        'download_mbartlarge50_success': 'Modelo MBARTLARGE50 descargado con éxito.',
        'download_success_msg': 'Modelo descargado con éxito.',
        'server_not_active_translation_warning': 'El servidor no está activo. Por favor, inicie el servidor primero.',
        'server_loading_wait_warning': 'El servidor aún se está cargando. Por favor, espere.',
        'enter_text_to_translate': 'Por favor, introduzca texto para traducir.',
        'failed_to_start_translation': 'Error al iniciar la traducción',
        'select_at_least_one_option': 'Por favor, seleccione al menos una opción.',
        'cannot_create_venv_without_python': 'No se puede crear un entorno virtual sin Python instalado.',
        'cannot_install_reqs_without_venv': 'No se pueden instalar bibliotecas sin un entorno virtual.',
        'environment_setup_title': 'Configuración del entorno',
        'portable_environment_setup_title': 'Configuración de entorno virtual portátil',
        'requirements_type_group': 'Tipo de requisitos',
        'cpu_requirements': 'Requisitos de CPU',
        'gpu_requirements': 'Requisitos de GPU (NVIDIA CUDA)',
        'setup_options_group': 'Opciones de configuración',
        'install_python_local': 'Instalar Python localmente',
        'install_python_local_installed': 'Instalar Python localmente (Ya instalado)',
        'install_python_local_tooltip': 'Se descargará e instalará una versión portátil de Python dentro de la carpeta de la aplicación',
        'create_virtual_environment': 'Crear entorno virtual',
        'create_virtual_environment_created': 'Crear entorno virtual (Ya existe)',
        'create_virtual_environment_tooltip': 'Crear un entorno aislado para instalar bibliotecas',
        'recreate_virtual_environment': 'Eliminar y recrear entorno virtual',
        'recreate_virtual_environment_tooltip': 'El entorno existente se eliminará y recreará desde cero (útil al cambiar el tipo de dispositivo)',
        'install_requirements': 'Instalar bibliotecas necesarias',
        'install_requirements_tooltip': 'Instalar bibliotecas necesarias de traducción e IA',
        'start_setup_btn': 'Iniciar',
        'cancel_btn': 'Cancelar',
        'confirm_recreate_venv': 'El entorno virtual actual se eliminará y recreará. ¿Desea continuar?',
        'confirm_start_setup': '¿Desea iniciar el proceso de configuración?',
        'confirm_cancel_setup': '¿Está seguro de que desea cancelar el proceso de configuración?',
        'venv_virtualenv_not_found': 'venv del sistema no encontrado, intentando usar virtualenv...',
        'setting_up_in_progress': 'Configurando...',
        'setting_up_environment': 'Configurando entorno...',
        'environment_setup_finished': 'Configuración del entorno finalizada.',
        'download_in_progress_exit_warning': 'Hay una descarga de modelo en curso. ¿Desea cancelarla antes de salir?',
        'download_madlad400_in_progress_exit_warning': 'Hay una descarga de madlad400 en curso. ¿Desea cancelarla antes de salir?',
        'convert_c2_in_progress_exit_warning': 'Hay una conversión C2 en curso. ¿Desea cancelarla antes de salir?',
        'convert_onnx_in_progress_exit_warning': 'Hay una conversión ONNX en curso. ¿Desea cancelarla antes de salir?',
        'convert_mbart_c2_in_progress_exit_warning': 'Hay una conversión MBART C2 en curso. ¿Desea cancelarla antes de salir?',
        'convert_mbart_onnx_in_progress_exit_warning': 'Hay una conversión MBART ONNX en curso. ¿Desea cancelarla antes de salir?',
        'verification_in_progress_exit_warning': 'Hay una verificación de bibliotecas en curso. ¿Desea cancelarla antes de salir?',
        'translation_in_progress_exit_warning': 'Hay una traducción en curso. ¿Desea cancelarla antes de salir?',
        'server_not_active': 'Servidor desconectado',
        'convert_mbartlarge50_to_format_confirm': '¿Desea convertir el modelo MBARTLARGE50 a',
        'may_take_time': 'Esto puede tardar',
        'convert_model_to_format_confirm': '¿Desea convertir el modelo a',
        'server_started_successfully': 'Servidor iniciado con éxito',
        'server_stopped_successfully': 'Servidor detenido con éxito',
        'settings_save_failed': 'Error al guardar configuración',
        'settings_saved_auto': 'Configuración guardada automáticamente',
        'settings_loaded_auto': 'Configuración cargada automáticamente',
        'settings_file_not_found': 'Archivo de configuración no encontrado, usando valores predeterminados',
        'status': 'Estado',
        'translating_in_progress': 'Traduciendo...',
        'translating_progress': 'Progreso de la traducción',
        'text_fields_cleared': 'Campos de texto borrados',
        'translation_successful': 'Traducción exitosa',
        'seconds': 'segundos',
        'translation_error': 'Error de traducción',
        'translation_cancelled': 'Traducción cancelada',
        'translation_started_background': 'Traducción iniciada en segundo plano',
        'translation_in_progress_cancel': 'Hay una traducción en curso. ¿Desea cancelarla?',
        'translation_in_progress_cancel_new': 'Hay una traducción en curso. ¿Desea cancelarla para iniciar una nueva?',
        'downloading_in_progress': 'Descargando...',
        'downloading_madlad400_model': 'Descargando modelo MADLAD400...',
        'downloading_mbartlarge50_model': 'Descargando modelo MBARTLARGE50...',
        'downloading_model_msg': 'Descargando modelo',
        'conversion_finished_msg': 'Proceso de conversión finalizado',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 convertido a CTranslate2 con éxito',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 convertido a ONNX con éxito',
        'mbartlarge50_original_model_not_found': 'Modelo original MBARTLARGE50 no encontrado',
        'setting_up_progress': 'Progreso de la configuración',
        'warning_thread_termination_failed': 'Advertencia: Algunos subprocesos fallaron al terminar',
        'warning_thread_timeout': 'Advertencia: Tiempo de espera de subproceso agotado',
        'python_local_exists': 'Python local ya existe',
        'downloading_python_installer': 'Descargando instalador de Python...',
        'installing_python': 'Instalando Python...',
        'python_install_success': 'Python local instalado con éxito',
        'python_install_failed': 'Error al instalar Python',
        'fatal_error_venv_active': 'Error fatal: ¡No se puede eliminar el entorno porque el programa se está ejecutando a través de él!',
        'venv_exists': 'El entorno virtual ya existe',
        'venv_created_success': 'Entorno virtual creado con éxito',
        'venv_creation_failed': 'Error al crear entorno virtual',
        'requirements_file_not_found': 'Archivo de requisitos no encontrado',
        'installing_requirements_from': 'Instalando requisitos desde',
        'download_madlad400_confirm': '¿Desea descargar el modelo MADLAD400?',
        'download_mbartlarge50_confirm': '¿Desea descargar el modelo MBARTLARGE50?',
        'download_model_specific': 'Descargar',
        'download_model_tooltip': 'Descargar modelo de internet:',
        'error_cuda_not_available': 'Error: CUDA no está disponible en el sistema',
        'error_pytorch_not_installed': 'Error: PyTorch no está instalado',
        'error_missing_lib_c2': 'Falta la biblioteca requerida para CTranslate2:',
        'libraries_verified_success': 'Bibliotecas verificadas con éxito',
        'error_verifying_libraries': 'Error al verificar bibliotecas:',
        'error_deleting_venv': 'Error al eliminar entorno virtual:',
        'starting_conversion_to': 'Iniciando conversión del modelo a:',
        'converting_model': 'Convirtiendo modelo...',
        'conversion_quant_failed_retry': 'Error en la conversión con cuantificación, reintentando sin ella:',
        'conversion_success_no_quant': 'Conversión exitosa sin cuantificación',
        'copying_extra_files': 'Copiando archivos extra...',
        'model_converted_success': 'Modelo convertido con éxito',
        'error_conversion': 'Error de conversión:',
        'error_src_model_not_found': 'Error: Carpeta del modelo fuente no encontrada',
        'deleting_old_folder': 'Eliminando carpeta antigua',
        'starting_mbart_conversion_to': 'Iniciando conversión del modelo mbartlarge50 a:',
        'saving_tokenizer_files': 'Guardando archivos del Tokenizer...',
        'conversion_success': 'Conversión exitosa',
        'exporting_onnx_wait': 'Exportando modelo a ONNX (esto puede tardar mucho tiempo para modelos grandes)',
        'warning_ram_requirement': 'Advertencia: Necesitará suficiente RAM (al menos 16GB).',
        'onnx_export_success_loading_tokenizer': 'Modelo exportado con éxito, cargando Tokenizer...',
        'saving_raw_model_temp': 'Guardando modelo sin procesar en carpeta temporal...',
        'quantizing_model': 'Cuantificando modelo:',
        'quantizing_part': 'Cuantificando parte:',
        'cleaning_temp_files': 'Limpiando archivos temporales...',
        'saving_model_files': 'Guardando archivos del modelo...',
        'warning_no_onnx_files': 'Advertencia: No se encontraron archivos ONNX',
        'quantizing': 'Cuantificando',
        'error_quant_failed_no_file': 'Error en la cuantificación: No se creó ningún archivo .onnx en la carpeta temporal para',
        'error_during_quant': 'Error durante la cuantificación',
        'error_folder_not_found': 'Carpeta no encontrada:',
        'error_download_corrupted': 'Descarga fallida: Archivos vacíos encontrados:',
        'error_model_path_not_specified': 'Error: Ruta del modelo no especificada',
        'verifying_model_at': 'Verificando modelo en la ruta:',
        'loading_model_local': 'Carga final del modelo desde archivos locales...',
        'loading_tokenizer': 'Cargando Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer cargado con éxito',
        'error_loading_tokenizer': 'Error al cargar Tokenizer:',
        'loading_model': 'Cargando Modelo',
        'model_loaded_success': 'Modelo cargado con éxito',
        'error_loading_model': 'Error al cargar Modelo:',
        'download_finished_msg': 'Descarga finalizada',
        'model_integrity_verified': 'Integridad del modelo verificada con éxito',
        'error_verifying_model': 'Error al verificar modelo:',
        'verifying_mbart_at': 'Verificando modelo MBARTLARGE50 en la ruta:',
        'loading_mbart_local': 'Carga final del modelo MBARTLARGE50 desde archivos locales...',
        'error_verifying_mbart': 'Error al verificar modelo MBARTLARGE50:',
        'verifying_madlad_at': 'Verificando modelo MADLAD400 en la ruta:',
        'loading_madlad_local': 'Carga final del modelo MADLAD400 desde archivos locales...',
        'testing_model_on_device': 'Probando carga del modelo en el dispositivo:',
        'translator_tokenizer_loaded_success': 'Traductor y Tokenizer cargados con éxito',
        'error_loading_components': 'Error al cargar componentes:',
        'error_verifying_madlad': 'Error al verificar modelo MADLAD400:',
        'download_opus_mt_tooltip': 'Descargar el modelo OPUS-MT seleccionado',
        'convert_c2_tooltip': 'Convertir el modelo al formato CTranslate2 seleccionado',
        'convert_onnx_tooltip': 'Convertir el modelo al formato ONNX seleccionado',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Configuración de METranslator:</h2>

        <h3>Paso 1: Instalar las bibliotecas necesarias (Internet requerido)</h3>
        <ol>
            <li>Vaya a Configuración del entorno.</li>
            <li>Elija su dispositivo: CPU para quienes no tienen GPU NVIDIA, o GPU para usuarios de NVIDIA que quieran usar CUDA.</li>
            <li>Seleccione otras opciones y haga clic en Iniciar.</li>
        </ol>

        <p><b>Nota:</b></p>
        <ul>
            <li>Si necesita cambiar su tipo de dispositivo, seleccione "Eliminar y recrear entorno virtual" para evitar conflictos de bibliotecas.</li>
            <li>La descarga de bibliotecas para GPU es considerable (aprox. 3 GB) y puede llevar algún tiempo.</li>
        </ul>

        <h3>Paso 2: Descargar y convertir modelos (Internet requerido)</h3>
        <ol>
            <li>Vaya a Configuración de descarga y conversión.</li>
            <li>Haga clic en Descargar el modelo (elija entre opus-mt-tc-big, MADLAD-400-Ct2 o mBART-large-50).</li>
            <li>Haga clic en Convertir el modelo para su dispositivo (solo para opus-mt-tc-big y mBART-large-50).</li>
        </ol>

        <p><b>Nota:</b></p>
        <ul>
            <li>Para el modelo opus-mt-tc-big, debe especificar los idiomas de origen y destino.</li>
            <li>El modelo MADLAD-400-Ct2 ya está convertido a ct2-int8_float16 y no necesita más conversión.</li>
            <li>El modelo opus-mt-tc-big tiene un tamaño aproximado de 450 MB.</li>
            <li>Los modelos MADLAD-400-Ct2 y mBART-large-50 tienen un tamaño aproximado de 3 GB cada uno.</li>
        </ul>

        <h3>Paso 3: Prepararse para la traducción</h3>
        <ol>
            <li>Vaya a Configuración ⚙️.</li>
            <li>Seleccione el modelo.</li>
            <li>Seleccione la ruta.</li>
            <li>Elija el tipo de dispositivo (CPU o GPU).</li>
        </ol>

        <p>Ya está listo para traducir y utilizar el servicio.</p>

        <h3>Cómo usar:</h3>
        <p>Simplemente haga clic en Iniciar servidor ▶ siempre que necesite una traducción.</p>

        <h3>Agradecemos de corazón a estos proyectos de código abierto:</h3>
        <ul>
            <li>Hugging Face por sus modelos de IA y conjuntos de datos.
                <ul>
                    <li>Explore su oferta en <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Descubra modelos específicos como <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Consulte MADLAD-400-Ct2 en <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>Obtenga más información sobre mBART-large-50 en <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python para el scripting del backend.
                <ul>
                    <li>Visite <a href="https://www.python.org/">Python</a> para saber más.</li>
                </ul>
            </li>
            <li>PyTorch para nuestro marco de aprendizaje automático.
                <ul>
                    <li>Explore PyTorch en <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Autor: Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'it': {
        'app_title': 'METranslator',
        'status_offline': 'Stato: Offline',
        'status_loading': 'Stato: Caricamento...',
        'status_running': 'Stato: In esecuzione',
        'status_error': 'Stato: Errore',
        'run_server': 'Avvia server',
        'stop_server': 'Ferma server',
        'env_setup': 'Imposta ambiente',
        'settings': 'Impostazioni',
        'download_convert': 'Scarica e Converti',
        'help': 'Aiuto',
        'to': 'A:',
        'from': 'Da:',
        'appearance': 'Aspetto',
        'select_theme': 'Seleziona tema:',
        'select_model': 'Seleziona modello di traduzione',
        'multilingual_models': 'Modelli multilingua',
        'device': 'Dispositivo:',
        'server_settings': 'Impostazioni server',
        'host': 'Host',
        'port': 'Porta',
        'translate_text_group': 'Traduci testo',
        'source_text': 'Testo sorgente:',
        'translation_label': 'Traduzione:',
        'translate_btn': 'Traduci',
        'clear_btn': 'Cancella',
        'font_size': 'Dimensione font:',
        'close': 'Chiudi',
        'warning': 'Avviso',
        'server_running_warning': 'Il server è già in esecuzione. È necessario arrestare il server prima di cambiare modello o dispositivo.',
        'server_running_warning_opus_land': 'Il server è già in esecuzione. È necessario arrestare il server prima di cambiare lingua per i modelli OPUS.',
        'stop_server_first': 'È necessario arrestare il server prima.',
        'back': 'Indietro',
        'download_multilingual': 'Scarica modelli multilingua',
        'download_madlad400': '⬇️ Scarica modello multilingua MADLAD400',
        'download_mbartlarge50': '⬇️ Scarica MBARTLARGE50',
        'convert_c2': 'Converti in CTranslate2',
        'convert_onnx': 'Converti in ONNX',
        'convert_btn': 'Converti',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Seleziona lingue',
        'download_model': '⬇️ Scarica modello',
        'output_direction': 'ltr',
        'lang_label': 'Lingua:',
        'select_lang': 'Lingua interfaccia:',
        'help_title': 'Istruzioni per l\'uso di METranslator',
        'confirm': 'Conferma',
        'loading': 'Caricamento',
        'info': 'Informazioni',
        'error': 'Errore',
        'success': 'Successo',
        'wait': 'Attendere prego',
        'alert': 'Avviso',
        'server_already_running': 'Il server è già in esecuzione.',
        'download_failed': 'Download fallito',
        'model_path_required': 'Il percorso del modello è richiesto.',
        'model_must_be_downloaded': 'Il modello deve essere scaricato prima.',
        'server_starting': 'Avvio del server...',
        'model_msg': 'Modello',
        'host_msg': 'Host',
        'port_msg': 'Porta',
        'confirm_download_msg': 'Sei sicuro di voler scaricare il modello?',
        'converting_in_progress': 'Conversione in corso...',
        'converting_model_to': 'Conversione del modello in',
        'confirm_conversion_msg': 'Vuoi davvero avviare il processo di conversione?',
        'download_in_progress_warning': 'Un download è già in corso.',
        'conversion_in_progress_warning': 'Una conversione è già in corso.',
        'setup_in_progress_warning': 'L\'installazione è già in corso.',
        'original_model_not_found': 'Modello originale non trovato',
        'download_model_first': 'Scarica prima il modello.',
        'conversion_c2_success': 'Modello convertito in CTranslate2 con successo.',
        'conversion_onnx_success': 'Modello convertito in ONNX con successo.',
        'download_madlad400_success': 'Modello MADLAD400 scaricato con successo.',
        'download_mbartlarge50_success': 'Modello MBARTLARGE50 scaricato con successo.',
        'download_success_msg': 'Modello scaricato con successo.',
        'server_not_active_translation_warning': 'Il server non è attivo. Avviare prima il server.',
        'server_loading_wait_warning': 'Il server è ancora in caricamento. Attendere prego.',
        'enter_text_to_translate': 'Inserire il testo da tradurre.',
        'failed_to_start_translation': 'Impossibile avviare la traduzione',
        'select_at_least_one_option': 'Selezionare almeno un\'opzione.',
        'cannot_create_venv_without_python': 'Impossibile creare un ambiente virtuale senza Python installato.',
        'cannot_install_reqs_without_venv': 'Impossibile installare le librerie senza un ambiente virtuale.',
        'environment_setup_title': 'Impostazione ambiente',
        'portable_environment_setup_title': 'Impostazione ambiente virtuale portatile',
        'requirements_type_group': 'Tipo di requisiti',
        'cpu_requirements': 'Requisiti CPU',
        'gpu_requirements': 'Requisiti GPU (NVIDIA CUDA)',
        'setup_options_group': 'Opzioni di installazione',
        'install_python_local': 'Installa Python localmente',
        'install_python_local_installed': 'Installa Python localmente (Già installato)',
        'install_python_local_tooltip': 'Una versione portatile di Python verrà scaricata e installata all\'interno della cartella dell\'app',
        'create_virtual_environment': 'Crea ambiente virtuale',
        'create_virtual_environment_created': 'Crea ambiente virtuale (Già esistente)',
        'create_virtual_environment_tooltip': 'Crea un ambiente isolato per installare le librerie',
        'recreate_virtual_environment': 'Elimina e ricrea ambiente virtuale',
        'recreate_virtual_environment_tooltip': 'L\'ambiente esistente verrà eliminato e ricreato da zero (utile quando si cambia tipo di dispositivo)',
        'install_requirements': 'Installa librerie necessarie',
        'install_requirements_tooltip': 'Installa le librerie necessarie per la traduzione e l\'IA',
        'start_setup_btn': 'Inizia',
        'cancel_btn': 'Annulla',
        'confirm_recreate_venv': 'L\'ambiente virtuale corrente verrà eliminato e ricreato. Vuoi continuare?',
        'confirm_start_setup': 'Vuoi avviare il processo di installazione?',
        'confirm_cancel_setup': 'Sei sicuro di voler annullare il processo di installazione?',
        'venv_virtualenv_not_found': 'Sistema venv non trovato, tentativo di utilizzare virtualenv...',
        'setting_up_in_progress': 'Impostazione in corso...',
        'setting_up_environment': 'Impostazione ambiente...',
        'environment_setup_finished': 'Impostazione ambiente completata.',
        'download_in_progress_exit_warning': 'Un download del modello è in corso. Vuoi annullarlo prima di uscire?',
        'download_madlad400_in_progress_exit_warning': 'Un download madlad400 è in corso. Vuoi annullarlo prima di uscire?',
        'convert_c2_in_progress_exit_warning': 'Una conversione C2 è in corso. Vuoi annullarla prima di uscire?',
        'convert_onnx_in_progress_exit_warning': 'Una conversione ONNX è in corso. Vuoi annullarla prima di uscire?',
        'convert_mbart_c2_in_progress_exit_warning': 'Una conversione MBART C2 è in corso. Vuoi annullarla prima di uscire?',
        'convert_mbart_onnx_in_progress_exit_warning': 'Una conversione MBART ONNX è in corso. Vuoi annullarla prima di uscire?',
        'verification_in_progress_exit_warning': 'Una verifica delle librerie è in corso. Vuoi annullarla prima di uscire?',
        'translation_in_progress_exit_warning': 'Una traduzione è in corso. Vuoi annullarla prima di uscire?',
        'server_not_active': 'Server Offline',
        'convert_mbartlarge50_to_format_confirm': 'Vuoi convertire il modello MBARTLARGE50 in',
        'may_take_time': 'Questo potrebbe richiedere tempo',
        'convert_model_to_format_confirm': 'Vuoi convertire il modello in',
        'server_started_successfully': 'Server avviato con successo',
        'server_stopped_successfully': 'Server fermato con successo',
        'settings_save_failed': 'Impossibile salvare le impostazioni',
        'settings_saved_auto': 'Impostazioni salvate automaticamente',
        'settings_loaded_auto': 'Impostazioni caricate automaticamente',
        'settings_file_not_found': 'File impostazioni non trovato, utilizzo dei valori predefiniti',
        'status': 'Stato',
        'translating_in_progress': 'Traduzione in corso...',
        'translating_progress': 'Avanzamento traduzione',
        'text_fields_cleared': 'Campi testo cancellati',
        'translation_successful': 'Traduzione riuscita',
        'seconds': 'secondi',
        'translation_error': 'Errore di traduzione',
        'translation_cancelled': 'Traduzione annullata',
        'translation_started_background': 'Traduzione avviata in background',
        'translation_in_progress_cancel': 'Una traduzione è in corso. Vuoi annullarla?',
        'translation_in_progress_cancel_new': 'Una traduzione è in corso. Vuoi annullarla per iniziarne una nuova?',
        'downloading_in_progress': 'Scaricamento...',
        'downloading_madlad400_model': 'Scaricamento modello MADLAD400...',
        'downloading_mbartlarge50_model': 'Scaricamento modello MBARTLARGE50...',
        'downloading_model_msg': 'Scaricamento modello',
        'conversion_finished_msg': 'Processo di conversione finito',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 convertito in CTranslate2 con successo',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 convertito in ONNX con successo',
        'mbartlarge50_original_model_not_found': 'Modello originale MBARTLARGE50 non trovato',
        'setting_up_progress': 'Avanzamento impostazione',
        'warning_thread_termination_failed': 'Avviso: Alcuni thread non sono riusciti a terminare',
        'warning_thread_timeout': 'Avviso: Timeout attesa thread',
        'python_local_exists': 'Python locale esiste già',
        'downloading_python_installer': 'Scaricamento installer Python...',
        'installing_python': 'Installazione Python...',
        'python_install_success': 'Python locale installato con successo',
        'python_install_failed': 'Impossibile installare Python',
        'fatal_error_venv_active': 'Errore fatale: Impossibile eliminare l\'ambiente perché il programma è in esecuzione attraverso di esso!',
        'venv_exists': 'L\'ambiente virtuale esiste già',
        'venv_created_success': 'Ambiente virtuale creato con successo',
        'venv_creation_failed': 'Impossibile creare ambiente virtuale',
        'requirements_file_not_found': 'File requisiti non trovato',
        'installing_requirements_from': 'Installazione requisiti da',
        'download_madlad400_confirm': 'Vuoi scaricare il modello MADLAD400?',
        'download_mbartlarge50_confirm': 'Vuoi scaricare il modello MBARTLARGE50?',
        'download_model_specific': 'Scarica',
        'download_model_tooltip': 'Scarica modello da internet:',
        'error_cuda_not_available': 'Errore: CUDA non è disponibile sul sistema',
        'error_pytorch_not_installed': 'Errore: PyTorch non è installato',
        'error_missing_lib_c2': 'Libreria richiesta mancante per CTranslate2:',
        'libraries_verified_success': 'Librerie verificate con successo',
        'error_verifying_libraries': 'Errore durante la verifica delle librerie:',
        'error_deleting_venv': 'Errore durante l\'eliminazione dell\'ambiente virtuale:',
        'starting_conversion_to': 'Avvio conversione modello in:',
        'converting_model': 'Conversione modello...',
        'conversion_quant_failed_retry': 'Conversione fallita con quantizzazione, riprovo senza di essa:',
        'conversion_success_no_quant': 'Conversione riuscita senza quantizzazione',
        'copying_extra_files': 'Copia file extra...',
        'model_converted_success': 'Modello convertito con successo',
        'error_conversion': 'Errore di conversione:',
        'error_src_model_not_found': 'Errore: Cartella modello sorgente non trovata',
        'deleting_old_folder': 'Eliminazione vecchia cartella',
        'starting_mbart_conversion_to': 'Avvio conversione modello mbartlarge50 in:',
        'saving_tokenizer_files': 'Salvataggio file Tokenizer...',
        'conversion_success': 'Conversione riuscita',
        'exporting_onnx_wait': 'Esportazione modello in ONNX (ciò potrebbe richiedere molto tempo per modelli grandi)',
        'warning_ram_requirement': 'Avviso: Avrai bisogno di abbastanza RAM (almeno 16GB).',
        'onnx_export_success_loading_tokenizer': 'Modello esportato con successo, caricamento Tokenizer...',
        'saving_raw_model_temp': 'Salvataggio modello grezzo in cartella temporanea...',
        'quantizing_model': 'Quantizzazione modello:',
        'quantizing_part': 'Quantizzazione parte:',
        'cleaning_temp_files': 'Pulizia file temporanei...',
        'saving_model_files': 'Salvataggio file modello...',
        'warning_no_onnx_files': 'Avviso: Nessun file ONNX trovato',
        'quantizing': 'Quantizzazione',
        'error_quant_failed_no_file': 'Quantizzazione fallita: Nessun file .onnx creato nella cartella temporanea per',
        'error_during_quant': 'Errore durante la quantizzazione',
        'error_folder_not_found': 'Cartella non trovata:',
        'error_download_corrupted': 'Download fallito: Trovati file vuoti:',
        'error_model_path_not_specified': 'Errore: Percorso modello non specificato',
        'verifying_model_at': 'Verifica modello al percorso:',
        'loading_model_local': 'Caricamento finale del modello dai file locali...',
        'loading_tokenizer': 'Caricamento Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer caricato con successo',
        'error_loading_tokenizer': 'Errore durante il caricamento del Tokenizer:',
        'loading_model': 'Caricamento Modello',
        'model_loaded_success': 'Modello caricato con successo',
        'error_loading_model': 'Errore durante il caricamento del Modello:',
        'download_finished_msg': 'Download finito',
        'model_integrity_verified': 'Integrità del modello verificata con successo',
        'error_verifying_model': 'Errore durante la verifica del modello:',
        'verifying_mbart_at': 'Verifica modello MBARTLARGE50 al percorso:',
        'loading_mbart_local': 'Caricamento finale del modello MBARTLARGE50 dai file locali...',
        'error_verifying_mbart': 'Errore durante la verifica del modello MBARTLARGE50:',
        'verifying_madlad_at': 'Verifica modello MADLAD400 al percorso:',
        'loading_madlad_local': 'Caricamento finale del modello MADLAD400 dai file locali...',
        'testing_model_on_device': 'Test caricamento modello su dispositivo:',
        'translator_tokenizer_loaded_success': 'Traduttore e Tokenizer caricati con successo',
        'error_loading_components': 'Errore durante il caricamento dei componenti:',
        'error_verifying_madlad': 'Errore durante la verifica del modello MADLAD400:',
        'download_opus_mt_tooltip': 'Scarica il modello OPUS-MT selezionato',
        'convert_c2_tooltip': 'Converti il modello nel formato CTranslate2 selezionato',
        'convert_onnx_tooltip': 'Converti il modello nel formato ONNX selezionato',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Configurazione di METranslator:</h2>

        <h3>Passaggio 1: Installa le librerie necessarie (Internet richiesto)</h3>
        <ol>
            <li>Vai a Impostazione ambiente.</li>
            <li>Scegli il tuo dispositivo: CPU per chi non ha GPU NVIDIA, o GPU per gli utenti NVIDIA che desiderano utilizzare CUDA.</li>
            <li>Seleziona le altre opzioni e fai clic su Inizia.</li>
        </ol>

        <p><b>Nota:</b></p>
        <ul>
            <li>Se è necessario modificare il tipo di dispositivo, selezionare "Elimina e ricrea ambiente virtuale" per evitare conflitti tra librerie.</li>
            <li>Il download delle librerie GPU è consistente (circa 3 GB) e potrebbe richiedere del tempo.</li>
        </ul>

        <h3>Passaggio 2: Scarica e converti i modelli (Internet richiesto)</h3>
        <ol>
            <li>Vai a Scarica e Converti.</li>
            <li>Fai clic su Scarica il modello (scegli tra opus-mt-tc-big, MADLAD-400-Ct2 o mBART-large-50).</li>
            <li>Fai clic su Converti il modello per il tuo dispositivo (solo per opus-mt-tc-big e mBART-large-50).</li>
        </ol>

        <p><b>Nota:</b></p>
        <ul>
            <li>Per il modello opus-mt-tc-big, è necessario specificare le lingue di origine e di destinazione.</li>
            <li>Il modello MADLAD-400-Ct2 è già convertito in ct2-int8_float16 e non necessita di ulteriori conversioni.</li>
            <li>Il modello opus-mt-tc-big ha una dimensione di circa 450 MB.</li>
            <li>I modelli MADLAD-400-Ct2 e mBART-large-50 hanno una dimensione di circa 3 GB ciascuno.</li>
        </ul>

        <h3>Passaggio 3: Preparati per la traduzione</h3>
        <ol>
            <li>Vai a Impostazioni ⚙️.</li>
            <li>Seleziona il modello.</li>
            <li>Seleziona il percorso.</li>
            <li>Scegli il tipo di dispositivo (CPU o GPU).</li>
        </ol>

        <p>Ora sei pronto per tradurre e utilizzare il servizio.</p>

        <h3>Come usare:</h3>
        <p>Basta fare clic su Avvia server ▶ ogni volta che hai bisogno di una traduzione.</p>

        <h3>Ringraziamo di cuore questi progetti open-source:</h3>
        <ul>
            <li>Hugging Face per i loro modelli di IA e set di dati.
                <ul>
                    <li>Esplora la loro offerta su <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Scopri modelli specifici come <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Dai un'occhiata a MADLAD-400-Ct2 su <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>Scopri di più su mBART-large-50 su <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python per lo scripting del backend.
                <ul>
                    <li>Visita <a href="https://www.python.org/">Python</a> per saperne di più.</li>
                </ul>
            </li>
            <li>PyTorch per il nostro framework di apprendimento automatico.
                <ul>
                    <li>Esplora PyTorch su <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Autore: Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'pt': {
        'app_title': 'METranslator',
        'status_offline': 'Estado: Offline',
        'status_loading': 'Estado: A carregar...',
        'status_running': 'Estado: A executar',
        'status_error': 'Estado: Erro',
        'run_server': 'Iniciar servidor',
        'stop_server': 'Parar servidor',
        'env_setup': 'Configuração do ambiente',
        'settings': 'Definições',
        'download_convert': 'Descarregar e Converter',
        'help': 'Ajuda',
        'to': 'Para:',
        'from': 'De:',
        'appearance': 'Aparência',
        'select_theme': 'Selecionar tema:',
        'select_model': 'Selecionar modelo de tradução',
        'multilingual_models': 'Modelos multilingues',
        'device': 'Dispositivo:',
        'server_settings': 'Definições do servidor',
        'host': 'Anfitrião',
        'port': 'Porta',
        'translate_text_group': 'Traduzir texto',
        'source_text': 'Texto original:',
        'translation_label': 'Tradução:',
        'translate_btn': 'Traduzir',
        'clear_btn': 'Limpar',
        'font_size': 'Tamanho da letra:',
        'close': 'Fechar',
        'warning': 'Aviso',
        'server_running_warning': 'O servidor já está a correr. Deve parar o servidor antes de mudar o modelo ou dispositivo.',
        'server_running_warning_opus_land': 'O servidor já está a correr. Deve parar o servidor antes de mudar o idioma para modelos OPUS.',
        'stop_server_first': 'Deve parar o servidor primeiro.',
        'back': 'Voltar',
        'download_multilingual': 'Descarregar modelos multilingues',
        'download_madlad400': '⬇️ Descarregar modelo multilingue MADLAD400',
        'download_mbartlarge50': '⬇️ Descarregar MBARTLARGE50',
        'convert_c2': 'Converter para CTranslate2',
        'convert_onnx': 'Converter para ONNX',
        'convert_btn': 'Converter',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Selecionar idiomas',
        'download_model': '⬇️ Descarregar modelo',
        'output_direction': 'ltr',
        'lang_label': 'Idioma:',
        'select_lang': 'Idioma da interface:',
        'help_title': 'Instruções de uso do METranslator',
        'confirm': 'Confirmar',
        'loading': 'A carregar',
        'info': 'Informação',
        'error': 'Erro',
        'success': 'Sucesso',
        'wait': 'Por favor aguarde',
        'alert': 'Alerta',
        'server_already_running': 'O servidor já está a correr.',
        'download_failed': 'Falha ao descarregar',
        'model_path_required': 'O caminho do modelo é obrigatório.',
        'model_must_be_downloaded': 'O modelo deve ser descarregado primeiro.',
        'server_starting': 'A iniciar o servidor...',
        'model_msg': 'Modelo',
        'host_msg': 'Anfitrião',
        'port_msg': 'Porta',
        'confirm_download_msg': 'Tem a certeza de que deseja descarregar o modelo?',
        'converting_in_progress': 'Conversão em curso...',
        'converting_model_to': 'A converter modelo para',
        'confirm_conversion_msg': 'Deseja realmente iniciar o processo de conversão?',
        'download_in_progress_warning': 'Um descarregamento já está em curso.',
        'conversion_in_progress_warning': 'Uma conversão já está em curso.',
        'setup_in_progress_warning': 'A configuração já está em curso.',
        'original_model_not_found': 'Modelo original não encontrado',
        'download_model_first': 'Por favor, descarregue o modelo primeiro.',
        'conversion_c2_success': 'Modelo convertido para CTranslate2 com sucesso.',
        'conversion_onnx_success': 'Modelo convertido para ONNX com sucesso.',
        'download_madlad400_success': 'Modelo MADLAD400 descarregado com sucesso.',
        'download_mbartlarge50_success': 'Modelo MBARTLARGE50 descarregado com sucesso.',
        'download_success_msg': 'Modelo descarregado com sucesso.',
        'server_not_active_translation_warning': 'O servidor não está ativo. Por favor, inicie o servidor primeiro.',
        'server_loading_wait_warning': 'O servidor ainda está a carregar. Por favor aguarde.',
        'enter_text_to_translate': 'Por favor, introduza o texto para traduzir.',
        'failed_to_start_translation': 'Falha ao iniciar a tradução',
        'select_at_least_one_option': 'Por favor, selecione pelo menos uma opção.',
        'cannot_create_venv_without_python': 'Não é possível criar um ambiente virtual sem Python instalado.',
        'cannot_install_reqs_without_venv': 'Não é possível instalar bibliotecas sem um ambiente virtual.',
        'environment_setup_title': 'Configuração do ambiente',
        'portable_environment_setup_title': 'Configuração de ambiente virtual portátil',
        'requirements_type_group': 'Tipo de requisitos',
        'cpu_requirements': 'Requisitos de CPU',
        'gpu_requirements': 'Requisitos de GPU (NVIDIA CUDA)',
        'setup_options_group': 'Opções de configuração',
        'install_python_local': 'Instalar Python localmente',
        'install_python_local_installed': 'Instalar Python localmente (Já instalado)',
        'install_python_local_tooltip': 'Uma versão portátil do Python será descarregada e instalada dentro da pasta da aplicação',
        'create_virtual_environment': 'Criar ambiente virtual',
        'create_virtual_environment_created': 'Criar ambiente virtual (Já existe)',
        'create_virtual_environment_tooltip': 'Criar um ambiente isolado para instalar bibliotecas',
        'recreate_virtual_environment': 'Eliminar e recriar ambiente virtual',
        'recreate_virtual_environment_tooltip': 'O ambiente existente será eliminado e recriado do zero (útil ao alterar o tipo de dispositivo)',
        'install_requirements': 'Instalar bibliotecas necessárias',
        'install_requirements_tooltip': 'Instalar bibliotecas necessárias de tradução e IA',
        'start_setup_btn': 'Iniciar',
        'cancel_btn': 'Cancelar',
        'confirm_recreate_venv': 'O ambiente virtual atual será eliminado e recriado. Deseja continuar?',
        'confirm_start_setup': 'Deseja iniciar o processo de configuração?',
        'confirm_cancel_setup': 'Tem a certeza de que deseja cancelar o processo de configuração?',
        'venv_virtualenv_not_found': 'Sistema venv não encontrado, tentando usar virtualenv...',
        'setting_up_in_progress': 'A configurar...',
        'setting_up_environment': 'A configurar ambiente...',
        'environment_setup_finished': 'Configuração do ambiente terminada.',
        'download_in_progress_exit_warning': 'Um descarregamento de modelo está em curso. Deseja cancelá-lo antes de sair?',
        'download_madlad400_in_progress_exit_warning': 'Um descarregamento madlad400 está em curso. Deseja cancelá-lo antes de sair?',
        'convert_c2_in_progress_exit_warning': 'Uma conversão C2 está em curso. Deseja cancelá-la antes de sair?',
        'convert_onnx_in_progress_exit_warning': 'Uma conversão ONNX está em curso. Deseja cancelá-la antes de sair?',
        'convert_mbart_c2_in_progress_exit_warning': 'Uma conversão MBART C2 está em curso. Deseja cancelá-la antes de sair?',
        'convert_mbart_onnx_in_progress_exit_warning': 'Uma conversão MBART ONNX está em curso. Deseja cancelá-la antes de sair?',
        'verification_in_progress_exit_warning': 'Uma verificação de bibliotecas está em curso. Deseja cancelá-la antes de sair?',
        'translation_in_progress_exit_warning': 'Uma tradução está em curso. Deseja cancelá-la antes de sair?',
        'server_not_active': 'Servidor Offline',
        'convert_mbartlarge50_to_format_confirm': 'Deseja converter o modelo MBARTLARGE50 para',
        'may_take_time': 'Isto pode demorar algum tempo',
        'convert_model_to_format_confirm': 'Deseja converter o modelo para',
        'server_started_successfully': 'Servidor iniciado com sucesso',
        'server_stopped_successfully': 'Servidor parado com sucesso',
        'settings_save_failed': 'Falha ao guardar definições',
        'settings_saved_auto': 'Definições guardadas automaticamente',
        'settings_loaded_auto': 'Definições carregadas automaticamente',
        'settings_file_not_found': 'Ficheiro de definições não encontrado, a usar valores predefinidos',
        'status': 'Estado',
        'translating_in_progress': 'A traduzir...',
        'translating_progress': 'Progresso da tradução',
        'text_fields_cleared': 'Campos de texto limpos',
        'translation_successful': 'Tradução bem sucedida',
        'seconds': 'segundos',
        'translation_error': 'Erro de tradução',
        'translation_cancelled': 'Tradução cancelada',
        'translation_started_background': 'Tradução iniciada em segundo plano',
        'translation_in_progress_cancel': 'Uma tradução está em curso. Deseja cancelá-la?',
        'translation_in_progress_cancel_new': 'Uma tradução está em curso. Deseja cancelá-la para iniciar uma nova?',
        'downloading_in_progress': 'A descarregar...',
        'downloading_madlad400_model': 'A descarregar modelo MADLAD400...',
        'downloading_mbartlarge50_model': 'A descarregar modelo MBARTLARGE50...',
        'downloading_model_msg': 'A descarregar modelo',
        'conversion_finished_msg': 'Processo de conversão concluído',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 convertido para CTranslate2 com sucesso',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 convertido para ONNX com sucesso',
        'mbartlarge50_original_model_not_found': 'Modelo original MBARTLARGE50 não encontrado',
        'setting_up_progress': 'Progresso da configuração',
        'warning_thread_termination_failed': 'Aviso: Algumas threads falharam ao terminar',
        'warning_thread_timeout': 'Aviso: Tempo limite de espera da thread',
        'python_local_exists': 'Python local já existe',
        'downloading_python_installer': 'A descarregar instalador Python...',
        'installing_python': 'A instalar Python...',
        'python_install_success': 'Python local instalado com sucesso',
        'python_install_failed': 'Falha ao instalar Python',
        'fatal_error_venv_active': 'Erro fatal: Não é possível eliminar o ambiente porque o programa está a correr nele!',
        'venv_exists': 'O ambiente virtual já existe',
        'venv_created_success': 'Ambiente virtual criado com sucesso',
        'venv_creation_failed': 'Falha ao criar ambiente virtual',
        'requirements_file_not_found': 'Ficheiro de requisitos não encontrado',
        'installing_requirements_from': 'A instalar requisitos de',
        'download_madlad400_confirm': 'Deseja descarregar o modelo MADLAD400?',
        'download_mbartlarge50_confirm': 'Deseja descarregar o modelo MBARTLARGE50?',
        'download_model_specific': 'Descarregar',
        'download_model_tooltip': 'Descarregar modelo da internet:',
        'error_cuda_not_available': 'Erro: CUDA não está disponível no sistema',
        'error_pytorch_not_installed': 'Erro: PyTorch não está instalado',
        'error_missing_lib_c2': 'Biblioteca necessária em falta para CTranslate2:',
        'libraries_verified_success': 'Bibliotecas verificadas com sucesso',
        'error_verifying_libraries': 'Erro ao verificar bibliotecas:',
        'error_deleting_venv': 'Erro ao eliminar ambiente virtual:',
        'starting_conversion_to': 'A iniciar conversão do modelo para:',
        'converting_model': 'A converter modelo...',
        'conversion_quant_failed_retry': 'Conversão falhou com quantização, a tentar sem ela:',
        'conversion_success_no_quant': 'Conversão bem sucedida sem quantização',
        'copying_extra_files': 'A copiar ficheiros extra...',
        'model_converted_success': 'Modelo convertido com sucesso',
        'error_conversion': 'Erro de conversão:',
        'error_src_model_not_found': 'Erro: Pasta do modelo de origem não encontrada',
        'deleting_old_folder': 'A eliminar pasta antiga',
        'starting_mbart_conversion_to': 'A iniciar conversão do modelo mbartlarge50 para:',
        'saving_tokenizer_files': 'A guardar ficheiros Tokenizer...',
        'conversion_success': 'Conversão bem sucedida',
        'exporting_onnx_wait': 'A exportar modelo para ONNX (isto pode demorar muito tempo para modelos grandes)',
        'warning_ram_requirement': 'Aviso: Precisará de RAM suficiente (pelo menos 16GB).',
        'onnx_export_success_loading_tokenizer': 'Modelo exportado com sucesso, a carregar Tokenizer...',
        'saving_raw_model_temp': 'A guardar modelo original na pasta temporária...',
        'quantizing_model': 'A quantizar modelo:',
        'quantizing_part': 'A quantizar parte:',
        'cleaning_temp_files': 'A limpar ficheiros temporários...',
        'saving_model_files': 'A guardar ficheiros do modelo...',
        'warning_no_onnx_files': 'Aviso: Nenhum ficheiro ONNX encontrado',
        'quantizing': 'A quantizar',
        'error_quant_failed_no_file': 'Quantização falhou: Nenhum ficheiro .onnx criado na pasta temporária para',
        'error_during_quant': 'Erro durante a quantização',
        'error_folder_not_found': 'Pasta não encontrada:',
        'error_download_corrupted': 'Descarregamento falhou: Ficheiros vazios encontrados:',
        'error_model_path_not_specified': 'Erro: Caminho do modelo não especificado',
        'verifying_model_at': 'A verificar modelo no caminho:',
        'loading_model_local': 'Carregamento final do modelo de ficheiros locais...',
        'loading_tokenizer': 'A carregar Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer carregado com sucesso',
        'error_loading_tokenizer': 'Erro ao carregar Tokenizer:',
        'loading_model': 'A carregar Modelo',
        'model_loaded_success': 'Modelo carregado com sucesso',
        'error_loading_model': 'Erro ao carregar Modelo:',
        'download_finished_msg': 'Descarregamento concluído',
        'model_integrity_verified': 'Integridade do modelo verificada com sucesso',
        'error_verifying_model': 'Erro ao verificar modelo:',
        'verifying_mbart_at': 'A verificar modelo MBARTLARGE50 no caminho:',
        'loading_mbart_local': 'Carregamento final do modelo MBARTLARGE50 de ficheiros locais...',
        'error_verifying_mbart': 'Erro ao verificar modelo MBARTLARGE50:',
        'verifying_madlad_at': 'A verificar modelo MADLAD400 no caminho:',
        'loading_madlad_local': 'Carregamento final do modelo MADLAD400 de ficheiros locais...',
        'testing_model_on_device': 'A testar carregamento do modelo no dispositivo:',
        'translator_tokenizer_loaded_success': 'Tradutor e Tokenizer carregados com sucesso',
        'error_loading_components': 'Erro ao carregar componentes:',
        'error_verifying_madlad': 'Erro ao verificar modelo MADLAD400:',
        'download_opus_mt_tooltip': 'Descarregar o modelo OPUS-MT selecionado',
        'convert_c2_tooltip': 'Converter o modelo para o formato CTranslate2 selecionado',
        'convert_onnx_tooltip': 'Converter o modelo para o formato ONNX selecionado',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Configuração do METranslator:</h2>

        <h3>Passo 1: Instalar as bibliotecas necessárias (Internet necessária)</h3>
        <ol>
            <li>Vá para Configuração do ambiente.</li>
            <li>Escolha o seu dispositivo: CPU para quem não tem GPUs NVIDIA, ou GPU para utilizadores NVIDIA que pretendem utilizar CUDA.</li>
            <li>Selecione outras opções e clique em Iniciar.</li>
        </ol>

        <p><b>Nota:</b></p>
        <ul>
            <li>Se precisar de alterar o seu tipo de dispositivo, selecione "Eliminar e recriar ambiente virtual" para evitar conflitos de bibliotecas.</li>
            <li>O descarregamento de bibliotecas GPU é considerável (aprox. 3 GB) e pode demorar algum tempo.</li>
        </ul>

        <h3>Passo 2: Descarregar e converter modelos (Internet necessária)</h3>
        <ol>
            <li>Vá para Descarregar e Converter.</li>
            <li>Clique em Descarregar o modelo (escolha entre opus-mt-tc-big, MADLAD-400-Ct2 ou mBART-large-50).</li>
            <li>Clique em Converter o modelo para o seu dispositivo (apenas para opus-mt-tc-big e mBART-large-50).</li>
        </ol>

        <p><b>Nota:</b></p>
        <ul>
            <li>Para o modelo opus-mt-tc-big, deve especificar os idiomas de origem e de destino.</li>
            <li>O modelo MADLAD-400-Ct2 já está convertido para ct2-int8_float16 e não necessita de mais conversões.</li>
            <li>O modelo opus-mt-tc-big tem aproximadamente 450 MB de tamanho.</li>
            <li>Os modelos MADLAD-400-Ct2 e mBART-large-50 têm aproximadamente 3 GB cada.</li>
        </ul>

        <h3>Passo 3: Preparar para a tradução</h3>
        <ol>
            <li>Vá para Definições ⚙️.</li>
            <li>Selecione o modelo.</li>
            <li>Selecione o caminho.</li>
            <li>Escolha o tipo de dispositivo (CPU ou GPU).</li>
        </ol>

        <p>Está agora pronto para traduzir e utilizar o serviço.</p>

        <h3>Como utilizar:</h3>
        <p>Basta clicar em Iniciar servidor ▶ sempre que precisar de uma tradução.</p>

        <h3>Agradecemos sinceramente a estes projetos de código aberto:</h3>
        <ul>
            <li>Hugging Face pelos seus modelos de IA e conjuntos de dados.
                <ul>
                    <li>Explore as suas ofertas em <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Descubra modelos específicos como <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Consulte o MADLAD-400-Ct2 em <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>Saiba mais sobre o mBART-large-50 em <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python para scripting backend.
                <ul>
                    <li>Visite o <a href="https://www.python.org/">Python</a> para saber mais.</li>
                </ul>
            </li>
            <li>PyTorch para a nossa framework de aprendizagem automática.
                <ul>
                    <li>Explore o PyTorch em <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Autor: Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'ru': {
        'app_title': 'METranslator',
        'status_offline': 'Статус: Не в сети',
        'status_loading': 'Статус: Загрузка...',
        'status_running': 'Статус: Работает',
        'status_error': 'Статус: Ошибка',
        'run_server': 'Запустить сервер',
        'stop_server': 'Остановить сервер',
        'env_setup': 'Настройка окружения',
        'settings': 'Настройки',
        'download_convert': 'Загрузка и конвертация',
        'help': 'Помощь',
        'to': 'В:',
        'from': 'Из:',
        'appearance': 'Внешний вид',
        'select_theme': 'Выбрать тему:',
        'select_model': 'Выбрать модель перевода',
        'multilingual_models': 'Многоязычные модели',
        'device': 'Устройство:',
        'server_settings': 'Настройки сервера',
        'host': 'Хост',
        'port': 'Порт',
        'translate_text_group': 'Перевести текст',
        'source_text': 'Исходный текст:',
        'translation_label': 'Перевод:',
        'translate_btn': 'Перевести',
        'clear_btn': 'Очистить',
        'font_size': 'Размер шрифта:',
        'close': 'Закрыть',
        'warning': 'Предупреждение',
        'server_running_warning': 'Сервер уже запущен. Вы должны остановить сервер перед изменением модели или устройства.',
        'server_running_warning_opus_land': 'Сервер уже запущен. Вы должны остановить сервер перед изменением языка для моделей OPUS.',
        'stop_server_first': 'Сначала необходимо остановить сервер.',
        'back': 'Назад',
        'download_multilingual': 'Скачать многоязычные модели',
        'download_madlad400': '⬇️ Скачать многоязычную модель MADLAD400',
        'download_mbartlarge50': '⬇️ Скачать MBARTLARGE50',
        'convert_c2': 'Конвертировать в CTranslate2',
        'convert_onnx': 'Конвертировать в ONNX',
        'convert_btn': 'Конвертировать',
        'opus_mt': 'OPUS-MT',
        'select_languages': 'Выбрать языки',
        'download_model': '⬇️ Скачать модель',
        'output_direction': 'ltr',
        'lang_label': 'Язык:',
        'select_lang': 'Язык интерфейса:',
        'help_title': 'Инструкция по использованию METranslator',
        'confirm': 'Подтвердить',
        'loading': 'Загрузка',
        'info': 'Информация',
        'error': 'Ошибка',
        'success': 'Успех',
        'wait': 'Пожалуйста, подождите',
        'alert': 'Внимание',
        'server_already_running': 'Сервер уже запущен.',
        'download_failed': 'Ошибка загрузки',
        'model_path_required': 'Требуется путь к модели.',
        'model_must_be_downloaded': 'Модель должна быть сначала загружена.',
        'server_starting': 'Запуск сервера...',
        'model_msg': 'Модель',
        'host_msg': 'Хост',
        'port_msg': 'Порт',
        'confirm_download_msg': 'Вы уверены, что хотите скачать модель?',
        'converting_in_progress': 'Конвертация...',
        'converting_model_to': 'Конвертация модели в',
        'confirm_conversion_msg': 'Вы действительно хотите начать процесс конвертации?',
        'download_in_progress_warning': 'Загрузка уже выполняется.',
        'conversion_in_progress_warning': 'Конвертация уже выполняется.',
        'setup_in_progress_warning': 'Установка уже выполняется.',
        'original_model_not_found': 'Исходная модель не найдена',
        'download_model_first': 'Пожалуйста, сначала скачайте модель.',
        'conversion_c2_success': 'Модель успешно конвертирована в CTranslate2.',
        'conversion_onnx_success': 'Модель успешно конвертирована в ONNX.',
        'download_madlad400_success': 'Модель MADLAD400 успешно загружена.',
        'download_mbartlarge50_success': 'Модель MBARTLARGE50 успешно загружена.',
        'download_success_msg': 'Модель успешно загружена.',
        'server_not_active_translation_warning': 'Сервер не активен. Пожалуйста, сначала запустите сервер.',
        'server_loading_wait_warning': 'Сервер все еще загружается. Пожалуйста, подождите.',
        'enter_text_to_translate': 'Пожалуйста, введите текст для перевода.',
        'failed_to_start_translation': 'Не удалось начать перевод',
        'select_at_least_one_option': 'Пожалуйста, выберите хотя бы один вариант.',
        'cannot_create_venv_without_python': 'Невозможно создать виртуальное окружение без установленного Python.',
        'cannot_install_reqs_without_venv': 'Невозможно установить библиотеки без виртуального окружения.',
        'environment_setup_title': 'Настройка окружения',
        'portable_environment_setup_title': 'Настройка портативного виртуального окружения',
        'requirements_type_group': 'Тип требований',
        'cpu_requirements': 'Требования к ЦП',
        'gpu_requirements': 'Требования к GPU (NVIDIA CUDA)',
        'setup_options_group': 'Параметры установки',
        'install_python_local': 'Установить Python локально',
        'install_python_local_installed': 'Установить Python локально (Уже установлено)',
        'install_python_local_tooltip': 'Портативная версия Python будет загружена и установлена внутри папки приложения',
        'create_virtual_environment': 'Создать виртуальное окружение',
        'create_virtual_environment_created': 'Создать виртуальное окружение (Уже существует)',
        'create_virtual_environment_tooltip': 'Создать изолированное окружение для установки библиотек',
        'recreate_virtual_environment': 'Удалить и пересоздать виртуальное окружение',
        'recreate_virtual_environment_tooltip': 'Текущее окружение будет удалено и создано заново (полезно при смене типа устройства)',
        'install_requirements': 'Установить необходимые библиотеки',
        'install_requirements_tooltip': 'Установить необходимые библиотеки для перевода и ИИ',
        'start_setup_btn': 'Начать',
        'cancel_btn': 'Отмена',
        'confirm_recreate_venv': 'Текущее виртуальное окружение будет удалено и создано заново. Вы хотите продолжить?',
        'confirm_start_setup': 'Вы хотите начать процесс установки?',
        'confirm_cancel_setup': 'Вы уверены, что хотите отменить процесс установки?',
        'venv_virtualenv_not_found': 'Системный venv не найден, попытка использовать virtualenv...',
        'setting_up_in_progress': 'Настройка...',
        'setting_up_environment': 'Настройка окружения...',
        'environment_setup_finished': 'Настройка окружения завершена.',
        'download_in_progress_exit_warning': 'Выполняется загрузка модели. Вы хотите отменить ее перед выходом?',
        'download_madlad400_in_progress_exit_warning': 'Выполняется загрузка madlad400. Вы хотите отменить ее перед выходом?',
        'convert_c2_in_progress_exit_warning': 'Выполняется конвертация C2. Вы хотите отменить ее перед выходом?',
        'convert_onnx_in_progress_exit_warning': 'Выполняется конвертация ONNX. Вы хотите отменить ее перед выходом?',
        'convert_mbart_c2_in_progress_exit_warning': 'Выполняется конвертация MBART C2. Вы хотите отменить ее перед выходом?',
        'convert_mbart_onnx_in_progress_exit_warning': 'Выполняется конвертация MBART ONNX. Вы хотите отменить ее перед выходом?',
        'verification_in_progress_exit_warning': 'Выполняется проверка библиотек. Вы хотите отменить ее перед выходом?',
        'translation_in_progress_exit_warning': 'Выполняется перевод. Вы хотите отменить его перед выходом?',
        'server_not_active': 'Сервер не в сети',
        'convert_mbartlarge50_to_format_confirm': 'Вы хотите конвертировать модель MBARTLARGE50 в',
        'may_take_time': 'Это может занять время',
        'convert_model_to_format_confirm': 'Вы хотите конвертировать модель в',
        'server_started_successfully': 'Сервер успешно запущен',
        'server_stopped_successfully': 'Сервер успешно остановлен',
        'settings_save_failed': 'Не удалось сохранить настройки',
        'settings_saved_auto': 'Настройки сохранены автоматически',
        'settings_loaded_auto': 'Настройки загружены автоматически',
        'settings_file_not_found': 'Файл настроек не найден, используются значения по умолчанию',
        'status': 'Статус',
        'translating_in_progress': 'Перевод...',
        'translating_progress': 'Прогресс перевода',
        'text_fields_cleared': 'Текстовые поля очищены',
        'translation_successful': 'Перевод выполнен успешно',
        'seconds': 'секунд',
        'translation_error': 'Ошибка перевода',
        'translation_cancelled': 'Перевод отменен',
        'translation_started_background': 'Перевод запущен в фоновом режиме',
        'translation_in_progress_cancel': 'Выполняется перевод. Вы хотите отменить его?',
        'translation_in_progress_cancel_new': 'Выполняется перевод. Вы хотите отменить его, чтобы начать новый?',
        'downloading_in_progress': 'Загрузка...',
        'downloading_madlad400_model': 'Загрузка модели MADLAD400...',
        'downloading_mbartlarge50_model': 'Загрузка модели MBARTLARGE50...',
        'downloading_model_msg': 'Загрузка модели',
        'conversion_finished_msg': 'Процесс конвертации завершен',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 успешно конвертирована в CTranslate2',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 успешно конвертирована в ONNX',
        'mbartlarge50_original_model_not_found': 'Исходная модель MBARTLARGE50 не найдена',
        'setting_up_progress': 'Прогресс настройки',
        'warning_thread_termination_failed': 'Предупреждение: Не удалось завершить некоторые потоки',
        'warning_thread_timeout': 'Предупреждение: Тайм-аут ожидания потока',
        'python_local_exists': 'Локальный Python уже существует',
        'downloading_python_installer': 'Загрузка установщика Python...',
        'installing_python': 'Установка Python...',
        'python_install_success': 'Локальный Python успешно установлен',
        'python_install_failed': 'Не удалось установить Python',
        'fatal_error_venv_active': 'Критическая ошибка: Невозможно удалить окружение, так как программа запущена в нем!',
        'venv_exists': 'Виртуальное окружение уже существует',
        'venv_created_success': 'Виртуальное окружение успешно создано',
        'venv_creation_failed': 'Не удалось создать виртуальное окружение',
        'requirements_file_not_found': 'Файл требований не найден',
        'installing_requirements_from': 'Установка требований из',
        'download_madlad400_confirm': 'Вы хотите загрузить модель MADLAD400?',
        'download_mbartlarge50_confirm': 'Вы хотите загрузить модель MBARTLARGE50?',
        'download_model_specific': 'Загрузить',
        'download_model_tooltip': 'Загрузить модель из интернета:',
        'error_cuda_not_available': 'Ошибка: CUDA недоступна в системе',
        'error_pytorch_not_installed': 'Ошибка: PyTorch не установлен',
        'error_missing_lib_c2': 'Отсутствует необходимая библиотека для CTranslate2:',
        'libraries_verified_success': 'Библиотеки успешно проверены',
        'error_verifying_libraries': 'Ошибка проверки библиотек:',
        'error_deleting_venv': 'Ошибка удаления виртуального окружения:',
        'starting_conversion_to': 'Начало конвертации модели в:',
        'converting_model': 'Конвертация модели...',
        'conversion_quant_failed_retry': 'Ошибка конвертации с квантованием, повторная попытка без него:',
        'conversion_success_no_quant': 'Успешная конвертация без квантования',
        'copying_extra_files': 'Копирование дополнительных файлов...',
        'model_converted_success': 'Модель успешно конвертирована',
        'error_conversion': 'Ошибка конвертации:',
        'error_src_model_not_found': 'Ошибка: Папка исходной модели не найдена',
        'deleting_old_folder': 'Удаление старой папки',
        'starting_mbart_conversion_to': 'Начало конвертации модели mbartlarge50 в:',
        'saving_tokenizer_files': 'Сохранение файлов Tokenizer...',
        'conversion_success': 'Конвертация успешна',
        'exporting_onnx_wait': 'Экспорт модели в ONNX (это может занять много времени для больших моделей)',
        'warning_ram_requirement': 'Предупреждение: Вам потребуется достаточно оперативной памяти (не менее 16 ГБ).',
        'onnx_export_success_loading_tokenizer': 'Модель успешно экспортирована, загрузка Tokenizer...',
        'saving_raw_model_temp': 'Сохранение исходной модели во временной папке...',
        'quantizing_model': 'Квантование модели:',
        'quantizing_part': 'Квантование части:',
        'cleaning_temp_files': 'Очистка временных файлов...',
        'saving_model_files': 'Сохранение файлов модели...',
        'warning_no_onnx_files': 'Предупреждение: Файлы ONNX не найдены',
        'quantizing': 'Квантование',
        'error_quant_failed_no_file': 'Ошибка квантования: Файл .onnx не создан во временной папке для',
        'error_during_quant': 'Ошибка во время квантования',
        'error_folder_not_found': 'Папка не найдена:',
        'error_download_corrupted': 'Ошибка загрузки: Найдены пустые файлы:',
        'error_model_path_not_specified': 'Ошибка: Путь к модели не указан',
        'verifying_model_at': 'Проверка модели по пути:',
        'loading_model_local': 'Финальная загрузка модели из локальных файлов...',
        'loading_tokenizer': 'Загрузка Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer успешно загружен',
        'error_loading_tokenizer': 'Ошибка загрузки Tokenizer:',
        'loading_model': 'Загрузка Model',
        'model_loaded_success': 'Model успешно загружена',
        'error_loading_model': 'Ошибка загрузки Model:',
        'download_finished_msg': 'Загрузка завершена',
        'model_integrity_verified': 'Целостность модели успешно проверена',
        'error_verifying_model': 'Ошибка проверки модели:',
        'verifying_mbart_at': 'Проверка модели MBARTLARGE50 по пути:',
        'loading_mbart_local': 'Финальная загрузка модели MBARTLARGE50 из локальных файлов...',
        'error_verifying_mbart': 'Ошибка проверки модели MBARTLARGE50:',
        'verifying_madlad_at': 'Проверка модели MADLAD400 по пути:',
        'loading_madlad_local': 'Финальная загрузка модели MADLAD400 из локальных файлов...',
        'testing_model_on_device': 'Тестирование загрузки модели на устройстве:',
        'translator_tokenizer_loaded_success': 'Переводчик и Tokenizer успешно загружены',
        'error_loading_components': 'Ошибка загрузки компонентов:',
        'error_verifying_madlad': 'Ошибка проверки модели MADLAD400:',
        'download_opus_mt_tooltip': 'Скачать выбранную модель OPUS-MT',
        'convert_c2_tooltip': 'Конвертировать модель в выбранный формат CTranslate2',
        'convert_onnx_tooltip': 'Конвертировать модель в выбранный формат ONNX',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>Настройка METranslator:</h2>

        <h3>Шаг 1: Установка необходимых библиотек (требуется интернет)</h3>
        <ol>
            <li>Перейдите в раздел «Настройка окружения».</li>
            <li>Выберите устройство: CPU для тех, у кого нет видеокарт NVIDIA, или GPU для пользователей NVIDIA, желающих использовать CUDA.</li>
            <li>Выберите другие параметры и нажмите «Начать».</li>
        </ol>

        <p><b>Примечание:</b></p>
        <ul>
            <li>Если вам нужно изменить тип устройства, выберите «Удалить и пересоздать виртуальное окружение», чтобы избежать конфликтов библиотек.</li>
            <li>Загрузка библиотек GPU имеет значительный объем (около 3 ГБ) и может занять некоторое время.</li>
        </ul>

        <h3>Шаг 2: Загрузка и конвертация моделей (требуется интернет)</h3>
        <ol>
            <li>Перейдите в «Загрузка и конвертация».</li>
            <li>Нажмите «Скачать модель» (выберите opus-mt-tc-big, MADLAD-400-Ct2 или mBART-large-50).</li>
            <li>Нажмите «Конвертировать модель для вашего устройства» (только для opus-mt-tc-big и mBART-large-50).</li>
        </ol>

        <p><b>Примечание:</b></p>
        <ul>
            <li>Для модели opus-mt-tc-big необходимо указать исходный и целевой языки.</li>
            <li>Модель MADLAD-400-Ct2 уже конвертирована в ct2-int8_float16 и не требует дальнейшей конвертации.</li>
            <li>Модель opus-mt-tc-big имеет размер около 450 МБ.</li>
            <li>Модели MADLAD-400-Ct2 и mBART-large-50 имеют размер около 3 ГБ каждая.</li>
        </ul>

        <h3>Шаг 3: Подготовка к переводу</h3>
        <ol>
            <li>Перейдите в «Настройки» ⚙️.</li>
            <li>Выберите модель.</li>
            <li>Выберите путь.</li>
            <li>Выберите тип устройства (CPU или GPU).</li>
        </ol>

        <p>Теперь вы готовы к переводу и использованию сервиса.</p>

        <h3>Как использовать:</h3>
        <p>Просто нажмите «Запустить сервер» ▶, когда вам понадобится перевод.</p>

        <h3>Мы искренне благодарим эти проекты с открытым исходным кодом:</h3>
        <ul>
            <li>Hugging Face за их модели ИИ и наборы данных.
                <ul>
                    <li>Изучите их предложения на <a href="https://huggingface.co/">Hugging Face</a>.</li>
                    <li>Откройте для себя конкретные модели, такие как <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>.</li>
                    <li>Ознакомьтесь с MADLAD-400-Ct2 на <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>.</li>
                    <li>Узнайте больше о mBART-large-50 на <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>.</li>
                </ul>
            </li>
            <li>Python для серверных сценариев.
                <ul>
                    <li>Посетите <a href="https://www.python.org/">Python</a>, чтобы узнать больше.</li>
                </ul>
            </li>
            <li>PyTorch для нашей среды машинного обучения.
                <ul>
                    <li>Изучите PyTorch на <a href="https://pytorch.org/">PyTorch</a>.</li>
                </ul>
            </li>
        </ul>

        <p>Автор: Marwan Alhamaty Email: marwanalhamaty@gmail.com</p>
        """,
    },
    'zh': {
        'app_title': 'METranslator',
        'status_offline': '状态：离线',
        'status_loading': '状态：加载中...',
        'status_running': '状态：运行中',
        'status_error': '状态：错误',
        'run_server': '运行服务器',
        'stop_server': '停止服务器',
        'env_setup': '环境设置',
        'settings': '设置',
        'download_convert': '下载与转换设置',
        'help': '帮助',
        'to': '至：',
        'from': '从：',
        'appearance': '外观',
        'select_theme': '选择主题：',
        'select_model': '选择翻译模型',
        'multilingual_models': '多语言模型',
        'device': '设备：',
        'server_settings': '服务器设置',
        'host': '主机',
        'port': '端口',
        'translate_text_group': '翻译文本',
        'source_text': '源文本：',
        'translation_label': '译文：',
        'translate_btn': '翻译',
        'clear_btn': '清除',
        'font_size': '字体大小：',
        'close': '关闭',
        'warning': '警告',
        'server_running_warning': '服务器正在运行。更改模型或设备前必须停止服务器。',
        'server_running_warning_opus_land': '服务器正在运行。更改 OPUS 模型的语言前必须停止服务器。',
        'stop_server_first': '您必须先停止服务器。',
        'back': '返回',
        'download_multilingual': '下载多语言模型',
        'download_madlad400': '⬇️ 下载 MADLAD400 多语言模型',
        'download_mbartlarge50': '⬇️ 下载 MBARTLARGE50',
        'convert_c2': '转换为 CTranslate2',
        'convert_onnx': '转换为 ONNX',
        'convert_btn': '转换',
        'opus_mt': 'OPUS-MT',
        'select_languages': '选择语言',
        'download_model': '⬇️ 下载模型',
        'output_direction': 'ltr',
        'lang_label': '语言：',
        'select_lang': '界面语言：',
        'help_title': 'METranslator 使用说明',
        'confirm': '确认',
        'loading': '加载中',
        'info': '信息',
        'error': '错误',
        'success': '成功',
        'wait': '请稍候',
        'alert': '提醒',
        'server_already_running': '服务器已在运行。',
        'download_failed': '下载失败',
        'model_path_required': '需要模型路径。',
        'model_must_be_downloaded': '必须先下载模型。',
        'server_starting': '正在启动服务器...',
        'model_msg': '模型',
        'host_msg': '主机',
        'port_msg': '端口',
        'confirm_download_msg': '您确定要下载该模型吗？',
        'converting_in_progress': '正在转换...',
        'converting_model_to': '正在将模型转换为',
        'confirm_conversion_msg': '您确定要开始转换过程吗？',
        'download_in_progress_warning': '已有下载任务正在进行。',
        'conversion_in_progress_warning': '已有转换任务正在进行。',
        'setup_in_progress_warning': '已有安装任务正在进行。',
        'original_model_not_found': '找不到原始模型',
        'download_model_first': '请先下载模型。',
        'conversion_c2_success': '模型已成功转换为 CTranslate2。',
        'conversion_onnx_success': '模型已成功转换为 ONNX。',
        'download_madlad400_success': 'MADLAD400 模型下载成功。',
        'download_mbartlarge50_success': 'MBARTLARGE50 模型下载成功。',
        'download_success_msg': '模型下载成功。',
        'server_not_active_translation_warning': '服务器未激活。请先启动服务器。',
        'server_loading_wait_warning': '服务器仍在加载中。请稍候。',
        'enter_text_to_translate': '请输入要翻译的文本。',
        'failed_to_start_translation': '翻译启动失败',
        'select_at_least_one_option': '请至少选择一个选项。',
        'cannot_create_venv_without_python': '未安装 Python 无法创建虚拟环境。',
        'cannot_install_reqs_without_venv': '没有虚拟环境无法安装库。',
        'environment_setup_title': '环境设置',
        'portable_environment_setup_title': '便携式虚拟环境设置',
        'requirements_type_group': '需求类型',
        'cpu_requirements': 'CPU 需求',
        'gpu_requirements': 'GPU 需求 (NVIDIA CUDA)',
        'setup_options_group': '设置选项',
        'install_python_local': '本地安装 Python',
        'install_python_local_installed': '本地安装 Python (已安装)',
        'install_python_local_tooltip': '将下载并安装便携版 Python 到应用程序文件夹内',
        'create_virtual_environment': '创建虚拟环境',
        'create_virtual_environment_created': '创建虚拟环境 (已存在)',
        'create_virtual_environment_tooltip': '创建一个隔离的环境来安装库',
        'recreate_virtual_environment': '删除并重新创建虚拟环境',
        'recreate_virtual_environment_tooltip': '现有的环境将被删除并从头开始重建（在更改设备类型时很有用）',
        'install_requirements': '安装必要的库',
        'install_requirements_tooltip': '安装必要的翻译和 AI 库',
        'start_setup_btn': '开始',
        'cancel_btn': '取消',
        'confirm_recreate_venv': '当前的虚拟环境将被删除并重新创建。您想继续吗？',
        'confirm_start_setup': '您想开始设置过程吗？',
        'confirm_cancel_setup': '您确定要取消设置过程吗？',
        'venv_virtualenv_not_found': '找不到系统 venv，正在尝试使用 virtualenv...',
        'setting_up_in_progress': '正在设置...',
        'setting_up_environment': '正在设置环境...',
        'environment_setup_finished': '环境设置完成。',
        'download_in_progress_exit_warning': '模型下载正在进行中。退出前要取消吗？',
        'download_madlad400_in_progress_exit_warning': 'madlad400 下载正在进行中。退出前要取消吗？',
        'convert_c2_in_progress_exit_warning': 'C2 转换正在进行中。退出前要取消吗？',
        'convert_onnx_in_progress_exit_warning': 'ONNX 转换正在进行中。退出前要取消吗？',
        'convert_mbart_c2_in_progress_exit_warning': 'MBART C2 转换正在进行中。退出前要取消吗？',
        'convert_mbart_onnx_in_progress_exit_warning': 'MBART ONNX 转换正在进行中。退出前要取消吗？',
        'verification_in_progress_exit_warning': '库验证正在进行中。退出前要取消吗？',
        'translation_in_progress_exit_warning': '翻译正在进行中。退出前要取消吗？',
        'server_not_active': '服务器离线',
        'convert_mbartlarge50_to_format_confirm': '要将 MBARTLARGE50 模型转换为',
        'may_take_time': '这可能需要一些时间',
        'convert_model_to_format_confirm': '要将模型转换为',
        'server_started_successfully': '服务器启动成功',
        'server_stopped_successfully': '服务器停止成功',
        'settings_save_failed': '设置保存失败',
        'settings_saved_auto': '设置已自动保存',
        'settings_loaded_auto': '设置已自动加载',
        'settings_file_not_found': '找不到设置文件，正在使用默认值',
        'status': '状态',
        'translating_in_progress': '正在翻译...',
        'translating_progress': '翻译进度',
        'text_fields_cleared': '文本字段已清除',
        'translation_successful': '翻译成功',
        'seconds': '秒',
        'translation_error': '翻译错误',
        'translation_cancelled': '翻译已取消',
        'translation_started_background': '翻译已在后台开始',
        'translation_in_progress_cancel': '翻译正在进行中。您想取消吗？',
        'translation_in_progress_cancel_new': '翻译正在进行中。您想取消它以开始新的翻译吗？',
        'downloading_in_progress': '正在下载...',
        'downloading_madlad400_model': '正在下载 MADLAD400 模型...',
        'downloading_mbartlarge50_model': '正在下载 MBARTLARGE50 模型...',
        'downloading_model_msg': '正在下载模型',
        'conversion_finished_msg': '转换过程已完成',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50 已成功转换为 CTranslate2',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50 已成功转换为 ONNX',
        'mbartlarge50_original_model_not_found': '找不到 MBARTLARGE50 原始模型',
        'setting_up_progress': '设置进度',
        'warning_thread_termination_failed': '警告：某些线程未能终止',
        'warning_thread_timeout': '警告：线程等待超时',
        'python_local_exists': '本地 Python 已存在',
        'downloading_python_installer': '正在下载 Python 安装程序...',
        'installing_python': '正在安装 Python...',
        'python_install_success': '本地 Python 安装成功',
        'python_install_failed': 'Python 安装失败',
        'fatal_error_venv_active': '致命错误：无法删除环境，因为程序正在其中运行！',
        'venv_exists': '虚拟环境已存在',
        'venv_created_success': '虚拟环境创建成功',
        'venv_creation_failed': '虚拟环境创建失败',
        'requirements_file_not_found': '找不到需求文件',
        'installing_requirements_from': '正在从以下位置安装需求',
        'download_madlad400_confirm': '您想下载 MADLAD400 模型吗？',
        'download_mbartlarge50_confirm': '您想下载 MBARTLARGE50 模型吗？',
        'download_model_specific': '下载',
        'download_model_tooltip': '从互联网下载模型：',
        'error_cuda_not_available': '错误：系统上不可用 CUDA',
        'error_pytorch_not_installed': '错误：未安装 PyTorch',
        'error_missing_lib_c2': '缺少 CTranslate2 所需的库：',
        'libraries_verified_success': '库验证成功',
        'error_verifying_libraries': '验证库时出错：',
        'error_deleting_venv': '删除虚拟环境时出错：',
        'starting_conversion_to': '开始将模型转换为：',
        'converting_model': '正在转换模型...',
        'conversion_quant_failed_retry': '量化转换失败，正在重试不带量化的转换：',
        'conversion_success_no_quant': '无量化转换成功',
        'copying_extra_files': '正在复制额外文件...',
        'model_converted_success': '模型转换成功',
        'error_conversion': '转换错误：',
        'error_src_model_not_found': '错误：找不到源模型文件夹',
        'deleting_old_folder': '正在删除旧文件夹',
        'starting_mbart_conversion_to': '开始将 mbartlarge50 模型转换为：',
        'saving_tokenizer_files': '正在保存 Tokenizer 文件...',
        'conversion_success': '转换成功',
        'exporting_onnx_wait': '正在将模型导出为 ONNX（对于大型模型这可能需要很长时间）',
        'warning_ram_requirement': '警告：您需要足够的 RAM（至少 16GB）。',
        'onnx_export_success_loading_tokenizer': '模型导出成功，正在加载 Tokenizer...',
        'saving_raw_model_temp': '正在将原始模型保存在临时文件夹中...',
        'quantizing_model': '正在量化模型：',
        'quantizing_part': '正在量化部分：',
        'cleaning_temp_files': '正在清理临时文件...',
        'saving_model_files': '正在保存模型文件...',
        'warning_no_onnx_files': '警告：找不到 ONNX 文件',
        'quantizing': '量化中',
        'error_quant_failed_no_file': '量化失败：未在临时文件夹中创建 .onnx 文件，针对',
        'error_during_quant': '量化期间出错',
        'error_folder_not_found': '找不到文件夹：',
        'error_download_corrupted': '下载失败：发现空文件：',
        'error_model_path_not_specified': '错误：未指定模型路径',
        'verifying_model_at': '正在验证路径处的模型：',
        'loading_model_local': '正在从本地文件最终加载模型...',
        'loading_tokenizer': '正在加载 Tokenizer',
        'tokenizer_loaded_success': 'Tokenizer 加载成功',
        'error_loading_tokenizer': '加载 Tokenizer 时出错：',
        'loading_model': '正在加载 Model',
        'model_loaded_success': 'Model 加载成功',
        'error_loading_model': '加载 Model 时出错：',
        'download_finished_msg': '下载完成',
        'model_integrity_verified': '模型完整性验证成功',
        'error_verifying_model': '验证模型时出错：',
        'verifying_mbart_at': '正在验证路径处的 MBARTLARGE50 模型：',
        'loading_mbart_local': '正在从本地文件最终加载 MBARTLARGE50 模型...',
        'error_verifying_mbart': '验证 MBARTLARGE50 模型时出错：',
        'verifying_madlad_at': '正在验证路径处的 MADLAD400 模型：',
        'loading_madlad_local': '正在从本地文件最终加载 MADLAD400 模型...',
        'testing_model_on_device': '正在测试在设备上加载模型：',
        'translator_tokenizer_loaded_success': 'Translator 和 Tokenizer 加载成功',
        'error_loading_components': '加载组件时出错：',
        'error_verifying_madlad': '验证 MADLAD400 模型时出错：',
        'download_opus_mt_tooltip': '下载选定的 OPUS-MT 模型',
        'convert_c2_tooltip': '将模型转换为选定的 CTranslate2 格式',
        'convert_onnx_tooltip': '将模型转换为选定的 ONNX 格式',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>设置 METranslator：</h2>

        <h3>第 1 步：安装必要的库（需要互联网）</h3>
        <ol>
            <li>转到“环境设置”。</li>
            <li>选择您的设备：没有 NVIDIA GPU 的用户选择 CPU，希望使用 CUDA 的 NVIDIA 用户选择 GPU。</li>
            <li>选择其他选项并点击“开始”。</li>
        </ol>

        <p><b>注意：</b></p>
        <ul>
            <li>如果您需要更改设备类型，请选择“删除并重新创建虚拟环境”以防止库冲突。</li>
            <li>下载 GPU 库很大（约 3GB），可能需要一些时间。</li>
        </ul>

        <h3>第 2 步：下载并转换模型（需要互联网）</h3>
        <ol>
            <li>转到“下载与转换设置”。</li>
            <li>点击“下载模型”（从 opus-mt-tc-big、MADLAD-400-Ct2 或 mBART-large-50 中选择）。</li>
            <li>点击“为您的设备转换模型”（仅适用于 opus-mt-tc-big 和 mBART-large-50）。</li>
        </ol>

        <p><b>注意：</b></p>
        <ul>
            <li>对于 opus-mt-tc-big 模型，您必须指定源语言和目标语言。</li>
            <li>MADLAD-400-Ct2 模型已经转换为 ct2-int8_float16，不需要进一步转换。</li>
            <li>opus-mt-tc-big 模型的大小约为 450MB。</li>
            <li>MADLAD-400-Ct2 和 mBART-large-50 模型的大小各约为 3GB。</li>
        </ul>

        <h3>第 3 步：准备翻译</h3>
        <ol>
            <li>转到“设置”⚙️。</li>
            <li>选择模型。</li>
            <li>选择路径。</li>
            <li>选择设备类型（CPU 或 GPU）。</li>
        </ol>

        <p>现在您可以开始翻译并使用该服务了。</p>

        <h3>如何使用：</h3>
        <p>只需在需要翻译时点击“运行服务器”▶ 即可。</p>

        <h3>我们衷心感谢这些开源项目：</h3>
        <ul>
            <li>Hugging Face 提供的 AI 模型和数据集。
                <ul>
                    <li>访问 <a href="https://huggingface.co/">Hugging Face</a> 探索他们的产品。</li>
                    <li>发现特定的模型，如 <a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>。</li>
                    <li>在 <a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a> 查看 MADLAD-400-Ct2。</li>
                    <li>在 <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a> 了解更多关于 mBART-large-50 的信息。</li>
                </ul>
            </li>
            <li>Python 用于后端脚本编写。
                <ul>
                    <li>访问 <a href="https://www.python.org/">Python</a> 了解更多。</li>
                </ul>
            </li>
            <li>PyTorch 作为我们的机器学习框架。
                <ul>
                    <li>在 <a href="https://pytorch.org/">PyTorch</a> 探索 PyTorch。</li>
                </ul>
            </li>
        </ul>

        <p>作者：Marwan Alhamaty 电子邮件：marwanalhamaty@gmail.com</p>
        """,
    },
    'ja': {
        'app_title': 'METranslator',
        'status_offline': 'ステータス: オフライン',
        'status_loading': 'ステータス: 読み込み中...',
        'status_running': 'ステータス: 実行中',
        'status_error': 'ステータス: エラー',
        'run_server': 'サーバーを起動',
        'stop_server': 'サーバーを停止',
        'env_setup': '環境設定',
        'settings': '設定',
        'download_convert': 'ダウンロードと変換設定',
        'help': 'ヘルプ',
        'to': '宛先:',
        'from': '元:',
        'appearance': '外観',
        'select_theme': 'テーマを選択:',
        'select_model': '翻訳モデルを選択',
        'multilingual_models': '多言語モデル',
        'device': 'デバイス:',
        'server_settings': 'サーバー設定',
        'host': 'ホスト',
        'port': 'ポート',
        'translate_text_group': 'テキスト翻訳',
        'source_text': 'ソーステキスト:',
        'translation_label': '翻訳:',
        'translate_btn': '翻訳',
        'clear_btn': 'クリア',
        'font_size': 'フォントサイズ:',
        'close': '閉じる',
        'warning': '警告',
        'server_running_warning': 'サーバーは既に実行中です。モデルまたはデバイスを変更する前にサーバーを停止する必要があります。',
        'server_running_warning_opus_land': 'サーバーは既に実行中です。OPUSモデルの言語を変更する前にサーバーを停止する必要があります。',
        'stop_server_first': '最初にサーバーを停止する必要があります。',
        'back': '戻る',
        'download_multilingual': '多言語モデルをダウンロード',
        'download_madlad400': '⬇️ MADLAD400多言語モデルをダウンロード',
        'download_mbartlarge50': '⬇️ MBARTLARGE50をダウンロード',
        'convert_c2': 'CTranslate2に変換',
        'convert_onnx': 'ONNXに変換',
        'convert_btn': '変換',
        'opus_mt': 'OPUS-MT',
        'select_languages': '言語を選択',
        'download_model': '⬇️ モデルをダウンロード',
        'output_direction': 'ltr',
        'lang_label': '言語:',
        'select_lang': 'インターフェース言語:',
        'help_title': 'METranslator使用方法',
        'confirm': '確認',
        'loading': '読み込み中',
        'info': '情報',
        'error': 'エラー',
        'success': '成功',
        'wait': 'お待ちください',
        'alert': 'アラート',
        'server_already_running': 'サーバーは既に実行中です。',
        'download_failed': 'ダウンロードに失敗しました',
        'model_path_required': 'モデルパスが必要です。',
        'model_must_be_downloaded': 'モデルを先にダウンロードする必要があります。',
        'server_starting': 'サーバーを起動中...',
        'model_msg': 'モデル',
        'host_msg': 'ホスト',
        'port_msg': 'ポート',
        'confirm_download_msg': '本当にモデルをダウンロードしますか？',
        'converting_in_progress': '変換中...',
        'converting_model_to': 'モデルを変換中',
        'confirm_conversion_msg': '本当に変換プロセスを開始しますか？',
        'download_in_progress_warning': 'ダウンロードは既に進行中です。',
        'conversion_in_progress_warning': '変換は既に進行中です。',
        'setup_in_progress_warning': 'セットアップは既に進行中です。',
        'original_model_not_found': '元のモデルが見つかりません',
        'download_model_first': '最初にモデルをダウンロードしてください。',
        'conversion_c2_success': 'モデルは正常にCTranslate2に変換されました。',
        'conversion_onnx_success': 'モデルは正常にONNXに変換されました。',
        'download_madlad400_success': 'MADLAD400モデルのダウンロードが成功しました。',
        'download_mbartlarge50_success': 'MBARTLARGE50モデルのダウンロードが成功しました。',
        'download_success_msg': 'モデルのダウンロードが成功しました。',
        'server_not_active_translation_warning': 'サーバーがアクティブではありません。最初にサーバーを起動してください。',
        'server_loading_wait_warning': 'サーバーはまだ読み込み中です。お待ちください。',
        'enter_text_to_translate': '翻訳するテキストを入力してください。',
        'failed_to_start_translation': '翻訳の開始に失敗しました',
        'select_at_least_one_option': '少なくとも1つのオプションを選択してください。',
        'cannot_create_venv_without_python': 'Pythonがインストールされていないと仮想環境を作成できません。',
        'cannot_install_reqs_without_venv': '仮想環境がないとライブラリをインストールできません。',
        'environment_setup_title': '環境設定',
        'portable_environment_setup_title': 'ポータブル仮想環境の設定',
        'requirements_type_group': '要件タイプ',
        'cpu_requirements': 'CPU要件',
        'gpu_requirements': 'GPU要件 (NVIDIA CUDA)',
        'setup_options_group': 'セットアップオプション',
        'install_python_local': 'Pythonをローカルにインストール',
        'install_python_local_installed': 'Pythonをローカルにインストール (既にインストール済み)',
        'install_python_local_tooltip': 'アプリフォルダ内にポータブル版Pythonがダウンロードされてインストールされます',
        'create_virtual_environment': '仮想環境を作成',
        'create_virtual_environment_created': '仮想環境を作成 (既に存在)',
        'create_virtual_environment_tooltip': 'ライブラリをインストールするための分離された環境を作成します',
        'recreate_virtual_environment': '仮想環境を削除して再作成',
        'recreate_virtual_environment_tooltip': '既存の環境は削除され、最初から作り直されます（デバイスタイプを変更する場合に便利です）',
        'install_requirements': '必要なライブラリをインストール',
        'install_requirements_tooltip': '翻訳とAIに必要なライブラリをインストールします',
        'start_setup_btn': '開始',
        'cancel_btn': 'キャンセル',
        'confirm_recreate_venv': '現在の仮想環境は削除され、再作成されます。続行しますか？',
        'confirm_start_setup': 'セットアッププロセスを開始しますか？',
        'confirm_cancel_setup': 'セットアッププロセスをキャンセルしてもよろしいですか？',
        'venv_virtualenv_not_found': 'システムのvenvが見つかりません。virtualenvを使用しようとしています...',
        'setting_up_in_progress': 'セットアップ中...',
        'setting_up_environment': '環境を設定中...',
        'environment_setup_finished': '環境設定が完了しました。',
        'download_in_progress_exit_warning': 'モデルのダウンロードが進行中です。終了する前にキャンセルしますか？',
        'download_madlad400_in_progress_exit_warning': 'madlad400のダウンロードが進行中です。終了する前にキャンセルしますか？',
        'convert_c2_in_progress_exit_warning': 'C2変換が進行中です。終了する前にキャンセルしますか？',
        'convert_onnx_in_progress_exit_warning': 'ONNX変換が進行中です。終了する前にキャンセルしますか？',
        'convert_mbart_c2_in_progress_exit_warning': 'MBART C2変換が進行中です。終了する前にキャンセルしますか？',
        'convert_mbart_onnx_in_progress_exit_warning': 'MBART ONNX変換が進行中です。終了する前にキャンセルしますか？',
        'verification_in_progress_exit_warning': 'ライブラリの検証が進行中です。終了する前にキャンセルしますか？',
        'translation_in_progress_exit_warning': '翻訳が進行中です。終了する前にキャンセルしますか？',
        'server_not_active': 'サーバーオフライン',
        'convert_mbartlarge50_to_format_confirm': 'MBARTLARGE50モデルを変換しますか',
        'may_take_time': '時間がかかる場合があります',
        'convert_model_to_format_confirm': 'モデルを変換しますか',
        'server_started_successfully': 'サーバーの起動に成功しました',
        'server_stopped_successfully': 'サーバーの停止に成功しました',
        'settings_save_failed': '設定の保存に失敗しました',
        'settings_saved_auto': '設定は自動的に保存されました',
        'settings_loaded_auto': '設定は自動的に読み込まれました',
        'settings_file_not_found': '設定ファイルが見つかりません。デフォルト値を使用します',
        'status': 'ステータス',
        'translating_in_progress': '翻訳中...',
        'translating_progress': '翻訳の進行状況',
        'text_fields_cleared': 'テキストフィールドがクリアされました',
        'translation_successful': '翻訳が成功しました',
        'seconds': '秒',
        'translation_error': '翻訳エラー',
        'translation_cancelled': '翻訳がキャンセルされました',
        'translation_started_background': '翻訳がバックグラウンドで開始されました',
        'translation_in_progress_cancel': '翻訳が進行中です。キャンセルしますか？',
        'translation_in_progress_cancel_new': '翻訳が進行中です。キャンセルして新しい翻訳を開始しますか？',
        'downloading_in_progress': 'ダウンロード中...',
        'downloading_madlad400_model': 'MADLAD400モデルをダウンロード中...',
        'downloading_mbartlarge50_model': 'MBARTLARGE50モデルをダウンロード中...',
        'downloading_model_msg': 'モデルをダウンロード中',
        'conversion_finished_msg': '変換プロセスが完了しました',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50は正常にCTranslate2に変換されました',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50は正常にONNXに変換されました',
        'mbartlarge50_original_model_not_found': 'MBARTLARGE50の元のモデルが見つかりません',
        'setting_up_progress': 'セットアップの進行状況',
        'warning_thread_termination_failed': '警告: 一部のスレッドの終了に失敗しました',
        'warning_thread_timeout': '警告: スレッド待機タイムアウト',
        'python_local_exists': 'ローカルPythonは既に存在します',
        'downloading_python_installer': 'Pythonインストーラーをダウンロード中...',
        'installing_python': 'Pythonをインストール中...',
        'python_install_success': 'ローカルPythonのインストールに成功しました',
        'python_install_failed': 'Pythonのインストールに失敗しました',
        'fatal_error_venv_active': '致命的なエラー: プログラムが実行されているため環境を削除できません！',
        'venv_exists': '仮想環境は既に存在します',
        'venv_created_success': '仮想環境の作成に成功しました',
        'venv_creation_failed': '仮想環境の作成に失敗しました',
        'requirements_file_not_found': '要件ファイルが見つかりません',
        'installing_requirements_from': 'から要件をインストール中',
        'download_madlad400_confirm': 'MADLAD400モデルをダウンロードしますか？',
        'download_mbartlarge50_confirm': 'MBARTLARGE50モデルをダウンロードしますか？',
        'download_model_specific': 'ダウンロード',
        'download_model_tooltip': 'インターネットからモデルをダウンロード:',
        'error_cuda_not_available': 'エラー: システムでCUDAが利用できません',
        'error_pytorch_not_installed': 'エラー: PyTorchがインストールされていません',
        'error_missing_lib_c2': 'CTranslate2に必要なライブラリがありません:',
        'libraries_verified_success': 'ライブラリの検証に成功しました',
        'error_verifying_libraries': 'ライブラリの検証エラー:',
        'error_deleting_venv': '仮想環境の削除エラー:',
        'starting_conversion_to': 'モデルの変換を開始:',
        'converting_model': 'モデルを変換中...',
        'conversion_quant_failed_retry': '量子化による変換に失敗しました。量子化なしで再試行しています:',
        'conversion_success_no_quant': '量子化なしで変換が成功しました',
        'copying_extra_files': '追加ファイルをコピー中...',
        'model_converted_success': 'モデルは正常に変換されました',
        'error_conversion': '変換エラー:',
        'error_src_model_not_found': 'エラー: ソースモデルフォルダが見つかりません',
        'deleting_old_folder': '古いフォルダを削除中',
        'starting_mbart_conversion_to': 'mbartlarge50モデルの変換を開始:',
        'saving_tokenizer_files': 'Tokenizerファイルを保存中...',
        'conversion_success': '変換成功',
        'exporting_onnx_wait': 'モデルをONNXにエクスポート中（大きなモデルには時間がかかる場合があります）',
        'warning_ram_requirement': '警告: 十分なRAM（少なくとも16GB）が必要です。',
        'onnx_export_success_loading_tokenizer': 'モデルのエクスポートに成功しました。Tokenizerを読み込み中...',
        'saving_raw_model_temp': '一時フォルダに生のモデルを保存中...',
        'quantizing_model': 'モデルを量子化中:',
        'quantizing_part': 'パートを量子化中:',
        'cleaning_temp_files': '一時ファイルをクリーンアップ中...',
        'saving_model_files': 'モデルファイルを保存中...',
        'warning_no_onnx_files': '警告: ONNXファイルが見つかりません',
        'quantizing': '量子化',
        'error_quant_failed_no_file': '量子化に失敗しました: .onnxファイルが一時フォルダに作成されませんでした',
        'error_during_quant': '量子化中のエラー',
        'error_folder_not_found': 'フォルダが見つかりません:',
        'error_download_corrupted': 'ダウンロードに失敗しました: 空のファイルが見つかりました:',
        'error_model_path_not_specified': 'エラー: モデルパスが指定されていません',
        'verifying_model_at': 'パスでモデルを検証中:',
        'loading_model_local': 'ローカルファイルからモデルを最終読み込み中...',
        'loading_tokenizer': 'Tokenizerを読み込み中',
        'tokenizer_loaded_success': 'Tokenizerの読み込みに成功しました',
        'error_loading_tokenizer': 'Tokenizerの読み込みエラー:',
        'loading_model': 'Modelを読み込み中',
        'model_loaded_success': 'Modelの読み込みに成功しました',
        'error_loading_model': 'Modelの読み込みエラー:',
        'download_finished_msg': 'ダウンロード完了',
        'model_integrity_verified': 'モデルの整合性検証に成功しました',
        'error_verifying_model': 'モデル検証エラー:',
        'verifying_mbart_at': 'パスでMBARTLARGE50モデルを検証中:',
        'loading_mbart_local': 'ローカルファイルからMBARTLARGE50モデルを最終読み込み中...',
        'error_verifying_mbart': 'MBARTLARGE50モデル検証エラー:',
        'verifying_madlad_at': 'パスでMADLAD400モデルを検証中:',
        'loading_madlad_local': 'ローカルファイルからMADLAD400モデルを最終読み込み中...',
        'testing_model_on_device': 'デバイスでモデルの読み込みをテスト中:',
        'translator_tokenizer_loaded_success': '翻訳者とTokenizerが正常に読み込まれました',
        'error_loading_components': 'コンポーネントの読み込みエラー:',
        'error_verifying_madlad': 'MADLAD400モデル検証エラー:',
        'download_opus_mt_tooltip': '選択したOPUS-MTモデルをダウンロード',
        'convert_c2_tooltip': 'モデルを選択したCTranslate2形式に変換',
        'convert_onnx_tooltip': 'モデルを選択したONNX形式に変換',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>METranslatorのセットアップ：</h2>

        <h3>ステップ1：必要なライブラリのインストール（インターネットが必要）</h3>
        <ol>
            <li>「環境設定」に移動します。</li>
            <li>デバイスを選択します：NVIDIA GPUをお持ちでない方はCPUを、CUDAを使用したいNVIDIAユーザーの方はGPUを選択してください。</li>
            <li>その他のオプションを選択して「開始」をクリックします。</li>
        </ol>

        <p><b>注意：</b></p>
        <ul>
            <li>デバイスタイプを变更する必要がある場合は、ライブラリの競合を防ぐために「仮想環境を削除して再作成」を選択してください。</li>
            <li>GPUライブラリのダウンロードは容量が大きく（約3GB）、時間がかかる場合があります。</li>
        </ul>

        <h3>ステップ2：モデルのダウンロードと変換（インターネットが必要）</h3>
        <ol>
            <li>「ダウンロードと変換設定」に移動します。</li>
            <li>「モデルをダウンロード」をクリックします（opus-mt-tc-big、MADLAD-400-Ct2、またはmBART-large-50から選択）。</li>
            <li>「デバイス用にモデルを変換」をクリックします（opus-mt-tc-bigおよびmBART-large-50のみ）。</li>
        </ol>

        <p><b>注意：</b></p>
        <ul>
            <li>opus-mt-tc-bigモデルの場合、ソース言語とターゲット言語を指定する必要があります。</li>
            <li>MADLAD-400-Ct2モデルはすでにct2-int8_float16に変換されているため、さらなる変換は必要ありません。</li>
            <li>opus-mt-tc-bigモデルのサイズは約450MBです。</li>
            <li>MADLAD-400-Ct2およびmBART-large-50モデルのサイズはそれぞれ約3GBです。</li>
        </ul>

        <h3>ステップ3：翻訳の準備</h3>
        <ol>
            <li>「設定」⚙️に移動します。</li>
            <li>モデルを選択します。</li>
            <li>パスを選択します。</li>
            <li>デバイスタイプ（CPUまたはGPU）を選択します。</li>
        </ol>

        <p>これで翻訳とサービスの利用準備が整いました。</p>

        <h3>使用方法：</h3>
        <p>翻訳が必要なときに「サーバーを起動」▶をクリックするだけです。</p>

        <h3>これらのオープンソースプロジェクトに心から感謝します：</h3>
        <ul>
            <li>Hugging Face（AIモデルとデータセット）。
                <ul>
                    <li><a href="https://huggingface.co/">Hugging Face</a>で提供内容を確認してください。</li>
                    <li><a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>などの特定のモデルを探索してください。</li>
                    <li><a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>でMADLAD-400-Ct2をチェックしてください。</li>
                    <li><a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>でmBART-large-50の詳細を確認してください。</li>
                </ul>
            </li>
            <li>Python（バックエンドスプリプティング）。
                <ul>
                    <li>詳細は<a href="https://www.python.org/">Python</a>をご覧ください。</li>
                </ul>
            </li>
            <li>PyTorch（機械学習フレームワーク）。
                <ul>
                    <li><a href="https://pytorch.org/">PyTorch</a>でPyTorchを探索してください。</li>
                </ul>
            </li>
        </ul>

        <p>作成者：Marwan Alhamaty メール：marwanalhamaty@gmail.com</p>
        """,
    },
    'ko': {
        'app_title': 'METranslator',
        'status_offline': '상태: 오프라인',
        'status_loading': '상태: 로딩 중...',
        'status_running': '상태: 실행 중',
        'status_error': '상태: 오류',
        'run_server': '서버 실행',
        'stop_server': '서버 중지',
        'env_setup': '환경 설정',
        'settings': '설정',
        'download_convert': '다운로드 및 변환 설정',
        'help': '도움말',
        'to': '대상:',
        'from': '원본:',
        'appearance': '모양',
        'select_theme': '테마 선택:',
        'select_model': '번역 모델 선택',
        'multilingual_models': '다국어 모델',
        'device': '장치:',
        'server_settings': '서버 설정',
        'host': '호스트',
        'port': '포트',
        'translate_text_group': '텍스트 번역',
        'source_text': '원본 텍스트:',
        'translation_label': '번역:',
        'translate_btn': '번역',
        'clear_btn': '지우기',
        'font_size': '글꼴 크기:',
        'close': '닫기',
        'warning': '경고',
        'server_running_warning': '서버가 이미 실행 중입니다. 모델이나 장치를 변경하려면 먼저 서버를 중지해야 합니다.',
        'server_running_warning_opus_land': '서버가 이미 실행 중입니다. OPUS 모델의 언어를 변경하려면 먼저 서버를 중지해야 합니다.',
        'stop_server_first': '먼저 서버를 중지해야 합니다.',
        'back': '뒤로',
        'download_multilingual': '다국어 모델 다운로드',
        'download_madlad400': '⬇️ MADLAD400 다국어 모델 다운로드',
        'download_mbartlarge50': '⬇️ MBARTLARGE50 다운로드',
        'convert_c2': 'CTranslate2로 변환',
        'convert_onnx': 'ONNX로 변환',
        'convert_btn': '변환',
        'opus_mt': 'OPUS-MT',
        'select_languages': '언어 선택',
        'download_model': '⬇️ 모델 다운로드',
        'output_direction': 'ltr',
        'lang_label': '언어:',
        'select_lang': '인터페이스 언어:',
        'help_title': 'METranslator 사용 지침',
        'confirm': '확인',
        'loading': '로딩 중',
        'info': '정보',
        'error': '오류',
        'success': '성공',
        'wait': '잠시 기다려 주세요',
        'alert': '알림',
        'server_already_running': '서버가 이미 실행 중입니다.',
        'download_failed': '다운로드 실패',
        'model_path_required': '모델 경로가 필요합니다.',
        'model_must_be_downloaded': '모델을 먼저 다운로드해야 합니다.',
        'server_starting': '서버 시작 중...',
        'model_msg': '모델',
        'host_msg': '호스트',
        'port_msg': '포트',
        'confirm_download_msg': '이 모델을 다운로드하시겠습니까?',
        'converting_in_progress': '변환 진행 중...',
        'converting_model_to': '모델 변환 중',
        'confirm_conversion_msg': '정말로 변환 프로세스를 시작하시겠습니까?',
        'download_in_progress_warning': '이미 다운로드가 진행 중입니다.',
        'conversion_in_progress_warning': '이미 변환이 진행 중입니다.',
        'setup_in_progress_warning': '설정이 이미 진행 중입니다.',
        'original_model_not_found': '원본 모델을 찾을 수 없음',
        'download_model_first': '먼저 모델을 다운로드하세요.',
        'conversion_c2_success': '모델이 CTranslate2로 성공적으로 변환되었습니다.',
        'conversion_onnx_success': '모델이 ONNX로 성공적으로 변환되었습니다.',
        'download_madlad400_success': 'MADLAD400 모델이 성공적으로 다운로드되었습니다.',
        'download_mbartlarge50_success': 'MBARTLARGE50 모델이 성공적으로 다운로드되었습니다.',
        'download_success_msg': '모델이 성공적으로 다운로드되었습니다.',
        'server_not_active_translation_warning': '서버가 활성화되지 않았습니다. 먼저 서버를 시작하세요.',
        'server_loading_wait_warning': '서버가 아직 로딩 중입니다. 잠시 기다려 주세요.',
        'enter_text_to_translate': '번역할 텍스트를 입력하세요.',
        'failed_to_start_translation': '번역 시작 실패',
        'select_at_least_one_option': '최소 하나의 옵션을 선택하세요.',
        'cannot_create_venv_without_python': 'Python이 설치되지 않으면 가상 환경을 만들 수 없습니다.',
        'cannot_install_reqs_without_venv': '가상 환경 없이는 라이브러리를 설치할 수 없습니다.',
        'environment_setup_title': '환경 설정',
        'portable_environment_setup_title': '포터블 가상 환경 설정',
        'requirements_type_group': '요구 사항 유형',
        'cpu_requirements': 'CPU 요구 사항',
        'gpu_requirements': 'GPU 요구 사항 (NVIDIA CUDA)',
        'setup_options_group': '설정 옵션',
        'install_python_local': 'Python 로컬 설치',
        'install_python_local_installed': 'Python 로컬 설치 (이미 설치됨)',
        'install_python_local_tooltip': '앱 폴더 내에 포터블 버전의 Python이 다운로드되어 설치됩니다.',
        'create_virtual_environment': '가상 환경 생성',
        'create_virtual_environment_created': '가상 환경 생성 (이미 존재함)',
        'create_virtual_environment_tooltip': '라이브러리를 설치하기 위해 격리된 환경 생성',
        'recreate_virtual_environment': '가상 환경 삭제 및 재생성',
        'recreate_virtual_environment_tooltip': '기존 환경이 삭제되고 처음부터 다시 생성됩니다 (장치 유형을 변경할 때 유용)',
        'install_requirements': '필요한 라이브러리 설치',
        'install_requirements_tooltip': '필요한 번역 및 AI 라이브러리 설치',
        'start_setup_btn': '시작',
        'cancel_btn': '취소',
        'confirm_recreate_venv': '현재 가상 환경이 삭제되고 다시 생성됩니다. 계속하시겠습니까?',
        'confirm_start_setup': '설정 프로세스를 시작하시겠습니까?',
        'confirm_cancel_setup': '정말로 설정 프로세스를 취소하시겠습니까?',
        'venv_virtualenv_not_found': '시스템 venv를 찾을 수 없음, virtualenv를 사용하려고 시도 중...',
        'setting_up_in_progress': '설정 중...',
        'setting_up_environment': '환경 설정 중...',
        'environment_setup_finished': '환경 설정 완료.',
        'download_in_progress_exit_warning': '모델 다운로드가 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'download_madlad400_in_progress_exit_warning': 'madlad400 다운로드가 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'convert_c2_in_progress_exit_warning': 'C2 변환이 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'convert_onnx_in_progress_exit_warning': 'ONNX 변환이 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'convert_mbart_c2_in_progress_exit_warning': 'MBART C2 변환이 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'convert_mbart_onnx_in_progress_exit_warning': 'MBART ONNX 변환이 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'verification_in_progress_exit_warning': '라이브러리 검증이 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'translation_in_progress_exit_warning': '번역이 진행 중입니다. 종료하기 전에 취소하시겠습니까?',
        'server_not_active': '서버 오프라인',
        'convert_mbartlarge50_to_format_confirm': 'MBARTLARGE50 모델을 변환하시겠습니까',
        'may_take_time': '시간이 걸릴 수 있습니다',
        'convert_model_to_format_confirm': '모델을 변환하시겠습니까',
        'server_started_successfully': '서버가 성공적으로 시작됨',
        'server_stopped_successfully': '서버가 성공적으로 중지됨',
        'settings_save_failed': '설정 저장 실패',
        'settings_saved_auto': '설정이 자동으로 저장됨',
        'settings_loaded_auto': '설정이 자동으로 로드됨',
        'settings_file_not_found': '설정 파일을 찾을 수 없음, 기본값 사용',
        'status': '상태',
        'translating_in_progress': '번역 중...',
        'translating_progress': '번역 진행률',
        'text_fields_cleared': '텍스트 필드가 지워짐',
        'translation_successful': '번역 성공',
        'seconds': '초',
        'translation_error': '번역 오류',
        'translation_cancelled': '번역 취소됨',
        'translation_started_background': '백그라운드에서 번역 시작됨',
        'translation_in_progress_cancel': '번역이 진행 중입니다. 취소하시겠습니까?',
        'translation_in_progress_cancel_new': '번역이 진행 중입니다. 취소하고 새 번역을 시작하시겠습니까?',
        'downloading_in_progress': '다운로드 중...',
        'downloading_madlad400_model': 'MADLAD400 모델 다운로드 중...',
        'downloading_mbartlarge50_model': 'MBARTLARGE50 모델 다운로드 중...',
        'downloading_model_msg': '모델 다운로드 중',
        'conversion_finished_msg': '변환 프로세스 완료',
        'conversion_mbartlarge50_c2_success': 'MBARTLARGE50가 CTranslate2로 성공적으로 변환됨',
        'conversion_mbartlarge50_onnx_success': 'MBARTLARGE50가 ONNX로 성공적으로 변환됨',
        'mbartlarge50_original_model_not_found': 'MBARTLARGE50 원본 모델을 찾을 수 없음',
        'setting_up_progress': '설정 진행률',
        'warning_thread_termination_failed': '경고: 일부 스레드가 종료하지 못함',
        'warning_thread_timeout': '경고: 스레드 대기 시간 초과',
        'python_local_exists': '로컬 Python이 이미 존재함',
        'downloading_python_installer': 'Python 설치 프로그램 다운로드 중...',
        'installing_python': 'Python 설치 중...',
        'python_install_success': '로컬 Python이 성공적으로 설치됨',
        'python_install_failed': 'Python 설치 실패',
        'fatal_error_venv_active': '치명적 오류: 프로그램이 실행 중이므로 환경을 삭제할 수 없습니다!',
        'venv_exists': '가상 환경이 이미 존재함',
        'venv_created_success': '가상 환경이 성공적으로 생성됨',
        'venv_creation_failed': '가상 환경 생성 실패',
        'requirements_file_not_found': '요구 사항 파일을 찾을 수 없음',
        'installing_requirements_from': '에서 요구 사항 설치 중',
        'download_madlad400_confirm': 'MADLAD400 모델을 다운로드하시겠습니까?',
        'download_mbartlarge50_confirm': 'MBARTLARGE50 모델을 다운로드하시겠습니까?',
        'download_model_specific': '다운로드',
        'download_model_tooltip': '인터넷에서 모델 다운로드:',
        'error_cuda_not_available': '오류: 시스템에서 CUDA를 사용할 수 없음',
        'error_pytorch_not_installed': '오류: PyTorch가 설치되지 않음',
        'error_missing_lib_c2': 'CTranslate2에 필요한 라이브러리 누락:',
        'libraries_verified_success': '라이브러리 검증 성공',
        'error_verifying_libraries': '라이브러리 검증 오류:',
        'error_deleting_venv': '가상 환경 삭제 오류:',
        'starting_conversion_to': '모델 변환 시작:',
        'converting_model': '모델 변환 중...',
        'conversion_quant_failed_retry': '양자화 변환 실패, 양자화 없이 재시도 중:',
        'conversion_success_no_quant': '양자화 없이 변환 성공',
        'copying_extra_files': '추가 파일 복사 중...',
        'model_converted_success': '모델 변환 성공',
        'error_conversion': '변환 오류:',
        'error_src_model_not_found': '오류: 원본 모델 폴더를 찾을 수 없음',
        'deleting_old_folder': '오래된 폴더 삭제 중',
        'starting_mbart_conversion_to': 'mbartlarge50 모델 변환 시작:',
        'saving_tokenizer_files': 'Tokenizer 파일 저장 중...',
        'conversion_success': '변환 성공',
        'exporting_onnx_wait': '모델을 ONNX로 내보내는 중 (대형 모델의 경우 시간이 오래 걸릴 수 있음)',
        'warning_ram_requirement': '경고: 충분한 RAM(최소 16GB)이 필요합니다.',
        'onnx_export_success_loading_tokenizer': '모델 내보내기 성공, Tokenizer 로드 중...',
        'saving_raw_model_temp': '임시 폴더에 원시 모델 저장 중...',
        'quantizing_model': '모델 양자화 중:',
        'quantizing_part': '부분 양자화 중:',
        'cleaning_temp_files': '임시 파일 정리 중...',
        'saving_model_files': '모델 파일 저장 중...',
        'warning_no_onnx_files': '경고: ONNX 파일을 찾을 수 없음',
        'quantizing': '양자화',
        'error_quant_failed_no_file': '양자화 실패: 임시 폴더에 .onnx 파일이 생성되지 않음',
        'error_during_quant': '양자화 중 오류 발생',
        'error_folder_not_found': '폴더를 찾을 수 없음:',
        'error_download_corrupted': '다운로드 실패: 빈 파일이 발견됨:',
        'error_model_path_not_specified': '오류: 모델 경로가 지정되지 않음',
        'verifying_model_at': '경로에서 모델 검증 중:',
        'loading_model_local': '로컬 파일에서 모델 최종 로드 중...',
        'loading_tokenizer': 'Tokenizer 로드 중',
        'tokenizer_loaded_success': 'Tokenizer 로드 성공',
        'error_loading_tokenizer': 'Tokenizer 로드 오류:',
        'loading_model': '모델 로드 중',
        'model_loaded_success': '모델 로드 성공',
        'error_loading_model': '모델 로드 오류:',
        'download_finished_msg': '다운로드 완료',
        'model_integrity_verified': '모델 무결성 검증 성공',
        'error_verifying_model': '모델 검증 오류:',
        'verifying_mbart_at': '경로에서 MBARTLARGE50 모델 검증 중:',
        'loading_mbart_local': '로컬 파일에서 MBARTLARGE50 모델 최종 로드 중...',
        'error_verifying_mbart': 'MBARTLARGE50 모델 검증 오류:',
        'verifying_madlad_at': '경로에서 MADLAD400 모델 검증 중:',
        'loading_madlad_local': '로컬 파일에서 MADLAD400 모델 최종 로드 중...',
        'testing_model_on_device': '장치에서 모델 로드 테스트 중:',
        'translator_tokenizer_loaded_success': '번역기 및 Tokenizer 로드 성공',
        'error_loading_components': '구성 요소 로드 오류:',
        'error_verifying_madlad': 'MADLAD400 모델 검증 오류:',
        'download_opus_mt_tooltip': '선택한 OPUS-MT 모델 다운로드',
        'convert_c2_tooltip': '모델을 선택한 CTranslate2 형식으로 변환',
        'convert_onnx_tooltip': '모델을 선택한 ONNX 형식으로 변환',
        'help_content': """
        <h1 align="center">METranslator</h1>
        <h2>METranslator 설정:</h2>

        <h3>1단계: 필요한 라이브러리 설치 (인터넷 필요)</h3>
        <ol>
            <li>'환경 설정'으로 이동합니다.</li>
            <li>장치를 선택합니다: NVIDIA GPU가 없는 경우 CPU를, CUDA를 사용하려는 NVIDIA 사용자는 GPU를 선택합니다.</li>
            <li>기타 옵션을 선택하고 '시작'을 클릭합니다.</li>
        </ol>

        <p><b>참고:</b></p>
        <ul>
            <li>장치 유형을 변경해야 하는 경우, 라이브러리 충돌을 방지하기 위해 '가상 환경 삭제 및 재생성'을 선택하십시오.</li>
            <li>GPU 라이브러리 다운로드는 용량이 크며(약 3GB) 시간이 걸릴 수 있습니다.</li>
        </ul>

        <h3>2단계: 모델 다운로드 및 변환 (인터넷 필요)</h3>
        <ol>
            <li>'다운로드 및 변환 설정'으로 이동합니다.</li>
            <li>'모델 다운로드'를 클릭합니다 (opus-mt-tc-big, MADLAD-400-Ct2 또는 mBART-large-50 중 선택).</li>
            <li>'장치용 모델 변환'을 클릭합니다 (opus-mt-tc-big 및 mBART-large-50만 해당).</li>
        </ol>

        <p><b>참고:</b></p>
        <ul>
            <li>opus-mt-tc-big 모델의 경우 원본 및 대상 언어를 지정해야 합니다.</li>
            <li>MADLAD-400-Ct2 모델은 이미 ct2-int8_float16으로 변환되어 있어 추가 변환이 필요하지 않습니다.</li>
            <li>opus-mt-tc-big 모델은 약 450MB 크기입니다.</li>
            <li>MADLAD-400-Ct2 및 mBART-large-50 모델은 각각 약 3GB입니다.</li>
        </ul>

        <h3>3단계: 번역 준비</h3>
        <ol>
            <li>'설정' ⚙️으로 이동합니다.</li>
            <li>모델을 선택합니다.</li>
            <li>경로를 선택합니다.</li>
            <li>장치 유형(CPU 또는 GPU)을 선택합니다.</li>
        </ol>

        <p>이제 번역 및 서비스 이용 준비가 완료되었습니다.</p>

        <h3>사용 방법:</h3>
        <p>번역이 필요할 때마다 '서버 실행' ▶을 클릭하기만 하면 됩니다.</p>

        <h3>이 오픈 소스 프로젝트들에 깊은 감사를 표합니다:</h3>
        <ul>
            <li>Hugging Face (AI 모델 및 데이터 세트 제공).
                <ul>
                    <li><a href="https://huggingface.co/">Hugging Face</a>에서 제공하는 서비스를 확인해 보세요.</li>
                    <li><a href="https://huggingface.co/models?other=opus-mt-tc">opus-mt-tc</a>와 같은 특정 모델을 찾아보세요.</li>
                    <li><a href="https://huggingface.co/SoybeanMilk/madlad400-3b-mt-ct2-int8_float16">SoybeanMilk/madlad400-3b-mt-ct2-int8_float16</a>에서 MADLAD-400-Ct2를 확인해 보세요.</li>
                    <li><a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt">facebook/mbart-large-50-many-to-many-mmt</a>에서 mBART-large-50에 대해 자세히 알아보세요.</li>
                </ul>
            </li>
            <li>Python (백엔드 스크립팅).
                <ul>
                    <li>자세한 내용은 <a href="https://www.python.org/">Python</a>을 방문하세요.</li>
                </ul>
            </li>
            <li>PyTorch (기계 학습 프레임워크).
                <ul>
                    <li><a href="https://pytorch.org/">PyTorch</a>에서 PyTorch를 살펴보세요.</li>
                </ul>
            </li>
        </ul>

        <p>작성자: Marwan Alhamaty 이메일: marwanalhamaty@gmail.com</p>
        """,
    }
    

}
