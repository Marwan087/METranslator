@echo off

:: إعدادات المجلدات والملفات
set "APP_NAME=METranslator"
set "TARGET_DIR=%APP_NAME%"
set "ZIP_NAME=%APP_NAME%.7z"

echo ========================================================
echo       METranslator - Build Script
echo ========================================================

:: 1. تنظيف المجلدات السابقة
echo [1/5] Cleaning old build files...
if exist "%TARGET_DIR%" rd /s /q "%TARGET_DIR%"
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
if exist "uninstall.spec" del /q "uninstall.spec"
if exist "%ZIP_NAME%" del /q "%ZIP_NAME%"

:: 2. بناء البرنامج الرئيسي باستخدام cx_Freeze
echo [2/5] Building main application (METranslator.exe) with cx_Freeze...
call python setup_cx_freeze.py build
if errorlevel 1 goto :BUILD_FAILED

:: 3. بناء ملف إلغاء التثبيت باستخدام PyInstaller
echo [3/5] Building uninstaller (uninstall.exe) with PyInstaller...
call pyinstaller --onefile --windowed --icon="icons\uninstall.ico" uninstall.py
if errorlevel 1 goto :BUILD_FAILED

:: 4. جمع الملفات في المجلد النهائي
echo [4/5] Organizing files into "%TARGET_DIR%" folder...
mkdir "%TARGET_DIR%" 2>nul

:: البحث عن مجلد exe الناتج من cx_Freeze
set "FROZEN_DIR="
for /d %%D in (build\exe.*) do set "FROZEN_DIR=%%D"

if "%FROZEN_DIR%" == "" goto :NO_FROZEN_DIR

echo Copying cx_Freeze output from "%FROZEN_DIR%"...
xcopy /e /y "%FROZEN_DIR%\*" "%TARGET_DIR%\"

:: نسخ ملف uninstall.exe من مجلد dist
if exist "dist\uninstall.exe" copy /y "dist\uninstall.exe" "%TARGET_DIR%\"

:: نسخ الملفات الإضافية
if exist "LICENSE" copy /y "LICENSE" "%TARGET_DIR%\"
if exist "README.md" copy /y "README.md" "%TARGET_DIR%\"
if exist "README_AR.md" copy /y "README_AR.md" "%TARGET_DIR%\"

:: 5. ضغط المجلد باستخدام 7-Zip
echo [5/5] Creating 7z archive...

set "SEVENZIP=7z"
where 7z >nul 2>nul
if not errorlevel 1 goto :START_COMPRESS

set "SEVENZIP=C:\Program Files\7-Zip\7z.exe"
if exist "%SEVENZIP%" goto :START_COMPRESS

set "SEVENZIP=C:\Program Files (x86)\7-Zip\7z.exe"
if exist "%SEVENZIP%" goto :START_COMPRESS

echo [ERROR] 7-Zip not found.
pause
exit /b 1

:START_COMPRESS
echo Using 7-Zip: "%SEVENZIP%"
"%SEVENZIP%" a -t7z "%ZIP_NAME%" "%TARGET_DIR%"
if errorlevel 1 goto :ZIP_FAILED

echo.
echo ========================================================
echo SUCCESS: The package is ready: %ZIP_NAME%
echo ========================================================

:: 6. تنظيف ملفات البناء المؤقتة بعد النجاح
echo [6/6] Cleaning up temporary build folders...
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
if exist "%TARGET_DIR%" rd /s /q "%TARGET_DIR%"
if exist "uninstall.spec" del /q "uninstall.spec"

goto :END

:BUILD_FAILED
echo [ERROR] Build failed.
goto :END

:NO_FROZEN_DIR
echo [ERROR] cx_Freeze output directory not found!
goto :END

:ZIP_FAILED
echo [ERROR] Compression failed.
goto :END

:END
pause