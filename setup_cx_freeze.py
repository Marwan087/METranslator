from cx_Freeze import setup, Executable
import os

# هذا الملف سيقوم بتجميع launcher.py فقط
build_exe_options = {
    "packages": ["tkinter", "subprocess", "os", "sys", "threading", "requests", "time", "certifi", "platform"], # مكتبات المُشغّل وواجهة التثبيت
    "excludes": ["unittest", "email", "http.server", "pydoc"],
    "include_files": [
        # يجب تضمين هذه الملفات لتكون متاحة للمُشغّل وواجهة التثبيت
        ("icons", "icons"),
        ("METranslator.py", "METranslator.py"),
        ("worker_classes.py", "worker_classes.py"),
        ("translations.py", "translations.py"),
        ("worker_tasks.py", "worker_tasks.py"),
        ("server_worker_direct.py", "server_worker_direct.py"),
        ("requirementsbuild.txt", "requirementsbuild.txt"),
        ("requirements.txt", "requirements.txt"),
        ("requirementscpu.txt", "requirementscpu.txt"),
        ("requirementsgpu.txt", "requirementsgpu.txt")
    ],
    "silent": False,
}
icon_path = os.path.join("icons", "MET.ico")
setup(
    name="METranslator",
    version="1.0",
    description="Translation Tool",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            script="gui_installer.py",          # <-- هذا هو الملف الرئيسي الذي سيتم تجميعه
            base="Win32GUI",               # <-- لإخفاء نافذة الأوامر للمُشغّل
            target_name="METranslator.exe",
            icon=icon_path # <-- الاسم النهائي للملف التنفيذي
        )
    ]
)