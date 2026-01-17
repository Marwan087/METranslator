
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import threading
import os
import sys
import subprocess
import urllib.request
import glob
import zipfile
import shutil


# --- الإعدادات ---
PYTHON_VERSION = "3.13.5"
MAIN_SCRIPT_NAME = "METranslator.py"
REQUIREMENTS_FILE_NAME = "requirements.txt"
FLAG_FILE = ".installed"

# تحديد مجلد التطبيق بشكل صحيح
if getattr(sys, 'frozen', False):
    APP_FOLDER = os.path.dirname(sys.executable)
else:
    APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
PYTHON_RUNTIME_DIR = os.path.join(APP_FOLDER, 'python_runtime')
MAIN_SCRIPT = os.path.join(APP_FOLDER, MAIN_SCRIPT_NAME)
REQUIREMENTS_FILE = os.path.join(APP_FOLDER, REQUIREMENTS_FILE_NAME)
# تحديد علم إخفاء النافذة (يعمل فقط على ويندوز)
CREATION_FLAGS = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0

# --- الألوان والتصميم ---
COLORS = {
    "bg": "#0f0f1a",        # خلفية داكنة جداً
    "fg": "#e0e0e0",        # نص فاتح
    "accent": "#00f3ff",    # سيان نيون للتقدم والتركيز
    "accent_hover": "#00dbe6", 
    "secondary_bg": "#1a1a2e", # خلفية العناصر الفرعية
    "log_bg": "#0a0a12",    # خلفية السجل
    "log_fg": "#00ff41",    # نص السجل (أخضر "ماتريكس")
    "danger": "#ff2a6d",    # أحمر للأخطاء/الإغلاق
    "title_bg": "#161625"   # شريط العنوان
}

class ModernButton(tk.Button):
    def __init__(self, master, **kwargs):
        # استخراج الألوان الخاصة إذا وجدت، وإلا استخدام الافتراضي
        bg_color = kwargs.pop('bg', COLORS["secondary_bg"])
        fg_color = kwargs.pop('fg', COLORS["accent"])
        active_bg = kwargs.pop('activebackground', COLORS["accent"])
        active_fg = kwargs.pop('activeforeground', COLORS["bg"])
        
        super().__init__(master, **kwargs)
        self.configure(
            bg=bg_color, fg=fg_color,
            activebackground=active_bg, activeforeground=active_fg,
            relief=tk.FLAT, borderwidth=0, cursor="hand2",
            font=("Segoe UI", 10, "bold")
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
    def on_enter(self, e):
        if self['state'] != tk.DISABLED:
            # تغميق الخلفية قليلاً عند التحويم
            pass 

    def on_leave(self, e):
        pass

class CustomProgressBar(tk.Canvas):
    def __init__(self, master, width=400, height=10, bg=COLORS["secondary_bg"], fill=COLORS["accent"]):
        super().__init__(master, width=width, height=height, bg=bg, highlightthickness=0)
        self.width = width
        self.height = height
        self.fill_color = fill
        self.rect_id = self.create_rectangle(0, 0, 0, height, fill=fill, width=0)
        self.value = 0.0
        
    def set_progress(self, value):
        # value from 0 to 100
        self.value = value
        w = (value / 100) * self.width
        self.coords(self.rect_id, 0, 0, w, self.height)


class InstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("METranslator Setup")
        
        # إزالة إطار الويندوز التقليدي
        self.root.overrideredirect(True)
        self.root.configure(bg=COLORS["bg"])
        
        # تحديد الحجم والموقع
        self.width = 500
        self.height = 250
        self.center_window()
        
        try:
            # أيقونة
            if getattr(sys, 'frozen', False):
                icon_path = os.path.join(APP_FOLDER, 'icons', 'MET.ico')
            else:
                icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'MET.ico')
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Could not load icon: {e}")

        # --- شريط العنوان المخصص ---
        self.title_bar = tk.Frame(self.root, bg=COLORS["title_bg"], height=30)
        self.title_bar.pack(fill=tk.X, side=tk.TOP)
        self.title_bar.pack_propagate(False)
        
        # تحريك النافذة
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)
        
        # عنوان التطبيق
        self.title_label = tk.Label(self.title_bar, text="METranslator Installer", bg=COLORS["title_bg"], fg=COLORS["fg"], font=("Segoe UI", 10))
        self.title_label.pack(side=tk.LEFT, padx=10)
        
        # زر الإغلاق
        self.close_btn = tk.Button(self.title_bar, text="✕", bg=COLORS["title_bg"], fg=COLORS["fg"], 
                                   activebackground=COLORS["danger"], activeforeground="white",
                                   relief=tk.FLAT, bd=0, command=self.close_app, width=4)
        # self.close_btn.pack(side=tk.RIGHT) # يمكن تفعيله إذا أردنا السماح بالإغلاق أثناء التثبيت

        # --- المحتوى الرئيسي ---
        self.main_frame = tk.Frame(self.root, bg=COLORS["bg"], padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # النص الرئيسي
        self.status_label = tk.Label(self.main_frame, text="Preparing installation...", 
                                     font=("Segoe UI", 14, "bold"), bg=COLORS["bg"], fg=COLORS["accent"])
        self.status_label.pack(pady=(0, 20))

        # شريط التقدم المخصص
        self.progress = CustomProgressBar(self.main_frame, width=460, height=8, bg=COLORS["secondary_bg"], fill=COLORS["accent"])
        self.progress.pack(pady=10)
        
        # نسبة التقدم
        self.pct_label = tk.Label(self.main_frame, text="0%", font=("Segoe UI", 10), bg=COLORS["bg"], fg=COLORS["fg"])
        self.pct_label.pack()

        # زر السجل
        self.log_visible = False
        
        # حاوية للأزرار لترتيبها بشكل أفقي
        self.buttons_container = tk.Frame(self.main_frame, bg=COLORS["bg"])
        self.buttons_container.pack(pady=10)
        
        self.toggle_log_btn = ModernButton(self.buttons_container, text="Show Details", command=self.toggle_log_visibility, width=15)
        self.toggle_log_btn.pack(side=tk.LEFT, padx=5)

        # زر الإلغاء
        self.cancel_btn = ModernButton(self.buttons_container, text="Cancel", command=self.close_app, bg=COLORS["danger"], fg="white", width=10)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

        # منطقة السجل (مخفية)
        self.log_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=60, height=10, 
                                                  bg=COLORS["log_bg"], fg=COLORS["log_fg"], 
                                                  insertbackground="white", state=tk.DISABLED, relief=tk.FLAT)
        
        # زر الإغلاق النهائي
        self.exit_btn = ModernButton(self.main_frame, text="Exit", command=self.close_app, bg=COLORS["danger"], fg="white")
        
        # بدء التثبيت
        threading.Thread(target=self.run_installation, daemon=True).start()

    def center_window(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (self.width/2)
        y = (hs/2) - (self.height/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def close_app(self):
        self.root.destroy()

    def log(self, message):
        """إضافة رسالة إلى منطقة النص"""
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, f"> {message}\n")
        self.log_area.see(tk.END)
        self.log_area.config(state=tk.DISABLED)
        # self.root.update_idletasks() # Removed to prevent lag on heavy logs

    def update_progress(self, value):
        """تحديث شريط التقدم"""
        self.progress.set_progress(value)
        self.pct_label.config(text=f"{int(value)}%")
        self.root.update_idletasks()

    def toggle_log_visibility(self):
        if self.log_visible:
            self.log_area.pack_forget()
            self.toggle_log_btn.config(text="Show Details")
            self.log_visible = False
            self.height = 250
            self.root.geometry(f"{self.width}x{self.height}")
        else:
            self.log_area.pack(pady=10, fill=tk.BOTH, expand=True)
            self.toggle_log_btn.config(text="Hide Details")
            self.log_visible = True
            self.height = 450
            self.root.geometry(f"{self.width}x{self.height}")
            
    # --- دوال التثبيت القديمة (مع تعديلات بسيطة للنصوص) ---

    def _install_local_python(self):
        """تثبيت بايثون محلي (Embeddable) في مجلد التطبيق"""
        python_exe = os.path.join(PYTHON_RUNTIME_DIR, 'python.exe')
        if os.path.exists(python_exe):
            self.log("Local Python found.")
            return True
            
        self.log("Local Python not found. Installing Embeddable Python...")
        self.status_label.config(text="Downloading Python Runtime...")
        
        # URL for Embeddable package
        # Note: Requires manual pip install
        installer_url = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-embed-amd64.zip"
        zip_path = os.path.join(APP_FOLDER, 'python_embed.zip')
        
        try:
            # 1. Download ZIP
            self.log(f"Downloading from {installer_url}...")
            response = urllib.request.urlopen(installer_url)
            total_size = int(response.headers.get('Content-Length', 0))
            downloaded = 0
            chunk_size = 8192
            
            with open(zip_path, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        progress = (downloaded / total_size) * 15 # 0-15% for download
                        self.update_progress(progress)
            
            # 2. Extract ZIP
            self.log("Extracting Python...")
            self.status_label.config(text="Extracting Python...")
            os.makedirs(PYTHON_RUNTIME_DIR, exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(PYTHON_RUNTIME_DIR)
                
            self.update_progress(20)

            # 3. Enable site-packages (Modify ._pth file)
            # Find the file like python313._pth
            pth_files = glob.glob(os.path.join(PYTHON_RUNTIME_DIR, '*._pth'))
            if pth_files:
                pth_file = pth_files[0]
                self.log(f"Configuring {os.path.basename(pth_file)} to enable pip...")
                with open(pth_file, 'r') as f:
                    content = f.read()
                # Uncomment 'import site' to match the specific line "import site"
                # The line is usually "#import site". We just replace it.
                if "#import site" in content:
                    content = content.replace("#import site", "import site")
                    with open(pth_file, 'w') as f:
                        f.write(content)
                else:
                    self.log("Warning: '#import site' not found in .pth file. Pip might not work.")

            # 4. Install pip
            self.log("Downloading pip installer (get-pip.py)...")
            get_pip_url = "https://bootstrap.pypa.io/get-pip.py"
            get_pip_path = os.path.join(PYTHON_RUNTIME_DIR, 'get-pip.py')
            
            # Download get-pip
            urllib.request.urlretrieve(get_pip_url, get_pip_path)
            
            self.log("Installing pip...")
            self.status_label.config(text="Installing pip...")
            
            # Run get-pip.py
            cmd = [python_exe, get_pip_path, "--no-warn-script-location"]
            result = subprocess.run(cmd, capture_output=True, text=True, creationflags=CREATION_FLAGS)
            
            if result.returncode != 0:
                self.log(f"Pip Install Failed: {result.stderr}")
                # We return False if pip fails because dependencies won't install
                return False
                
            self.log("Pip installed successfully.")
            self.update_progress(25)  # 25% after setup
            
            return True
            
        except Exception as e:
            self.log(f"Error installing Python: {str(e)}")
            return False
        finally:
            if os.path.exists(zip_path):
                os.remove(zip_path)
            # We can keep or delete get-pip.py. Let's delete it to keep it clean.
            if os.path.exists(os.path.join(PYTHON_RUNTIME_DIR, 'get-pip.py')):
                try:
                    os.remove(os.path.join(PYTHON_RUNTIME_DIR, 'get-pip.py'))
                except:
                    pass

    def run_installation(self):
        """تنفيذ خطوات التثبيت الكاملة"""
        try:
            self.log("Initializing METranslator Setup...")
            self.update_progress(0)
            
            # الخطوة 1: تثبيت بايثون محلياً
            if not self._install_local_python():
                messagebox.showerror("Error", "Failed to install Python.")
                self.status_label.config(text="Installation Failed", fg=COLORS["danger"])
                self.cancel_btn.pack_forget()
                self.exit_btn.pack(pady=10)
                return
            self.update_progress(25)
            
            # الخطوة الجديدة 2: تثبيت المكتبات مباشرة في python_runtime
            runtime_python = os.path.join(PYTHON_RUNTIME_DIR, 'python.exe')
            self.log("Installing dependencies... This may take a while.")
            self.status_label.config(text="Installing Dependencies...")
            
            # تشغيل pip
            process = subprocess.Popen([runtime_python, "-m", "pip", "install", "-r", REQUIREMENTS_FILE], 
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, creationflags=CREATION_FLAGS)
            
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    msg = output.strip()
                    self.log(msg)
                    # تحديث تقدم تقريبي
                    current_progress = self.progress.value
                    if current_progress < 70:
                        self.update_progress(current_progress + 0.5) 

            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, process.args)
            
            self.log("Dependencies installed.")
            self.update_progress(75)
            
            # الخطوة 3: إنشاء ملف العلم وتشغيل التطبيق
            with open(os.path.join(APP_FOLDER, FLAG_FILE), 'w') as f:
                f.write("ok")
            
            self.log("Setup complete.")
            self.status_label.config(text="Ready to Launch!", fg=COLORS["log_fg"])
            self.update_progress(100)
            
            self.log(f"Launching application...")
            subprocess.Popen([runtime_python, MAIN_SCRIPT], creationflags=CREATION_FLAGS)
            
            self.log("Application launched. Closing installer...")
            self.cancel_btn.pack_forget()
            self.root.after(2000, self.root.destroy)
            
        except Exception as e:
            self.log(f"Error: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.status_label.config(text="Error Occurred", fg=COLORS["danger"])
            self.cancel_btn.pack_forget()
            self.exit_btn.pack(pady=10)

# === المنطق الجديد للتحقق من التثبيت قبل فتح الواجهة ===
if __name__ == "__main__":
    flag_file_path = os.path.join(APP_FOLDER, FLAG_FILE)
    runtime_python = os.path.join(PYTHON_RUNTIME_DIR, 'python.exe')
    
    if os.path.exists(flag_file_path) and os.path.exists(runtime_python) and os.path.exists(MAIN_SCRIPT):
        try:
            subprocess.Popen([runtime_python, MAIN_SCRIPT], creationflags=CREATION_FLAGS)
            sys.exit(0)
        except Exception as e:
            print(f"Error launching app: {e}. Forcing re-installation.")
            if os.path.exists(flag_file_path):
                os.remove(flag_file_path)

    # إعداد واجهة المستخدم
    root = tk.Tk()
    app = InstallerGUI(root)
    root.mainloop()