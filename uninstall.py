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
import subprocess
import tkinter as tk
from tkinter import messagebox
import tempfile
import threading
import shutil
import time
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return True
    else:
        # Re-run the program with admin rights
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
            return False
        except:
            return False
# Enhanced Futuristic Theme Constants
BG_COLOR = "#0a0a12"      # Deeper dark blue
TITLE_BG = "#121220"      # Darker title bar
CYAN_ACCENT = "#00f3ff"   # Neon Cyan
CYAN_GLOW = "#005a5f"     # Darker cyan for glow
MATRIX_GREEN = "#39ff14"  # Brighter Matrix green
TEXT_COLOR = "#ffffff"    # Pure white for main text
TEXT_DIM = "#888899"      # Dimmed text for descriptions

class ModernUninstaller(tk.Tk):
    def __init__(self, app_dir, silent_mode=False):
        super().__init__()
        self.app_dir = app_dir
        self.silent_mode = silent_mode
        
        # Window Setup
        self.overrideredirect(True)
        self.geometry("620x420")
        self.configure(bg=CYAN_ACCENT) # This creates the neon border
        
        # Inner Body
        self.body = tk.Frame(self, bg=BG_COLOR)
        self.body.place(x=1, y=1, width=618, height=418)
        
        # Center and Bring to Top
        self.center_window()
        self.attributes("-topmost", True)
        self.lift()

        # Custom Title Bar
        self.title_bar = tk.Frame(self.body, bg=TITLE_BG, height=40)
        self.title_bar.pack(fill=tk.X)
        self.title_bar.pack_propagate(False)

        self.title_label = tk.Label(self.title_bar, text="ＭＥＴＲＡＮＳＬＡＴＯＲ  //  ＰＵＲＧＥ", 
                                    bg=TITLE_BG, fg=CYAN_ACCENT, font=("Consolas", 10, "bold"))
        self.title_label.pack(side=tk.LEFT, padx=15)

        self.close_btn = tk.Button(self.title_bar, text="✕", bg=TITLE_BG, fg=TEXT_DIM, 
                                   bd=0, padx=15, command=self.on_close, 
                                   activebackground="#ff2a2a", activeforeground="white",
                                   font=("Segoe UI", 11), cursor="hand2")
        self.close_btn.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.close_btn.bind("<Enter>", lambda e: self.close_btn.configure(bg="#ff2a2a", fg="white"))
        self.close_btn.bind("<Leave>", lambda e: self.close_btn.configure(bg=TITLE_BG, fg=TEXT_DIM))

        # Dragging logic
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)
        self.title_label.bind("<Button-1>", self.start_move)
        self.title_label.bind("<B1-Motion>", self.do_move)

        # Main Content Frame
        self.main_frame = tk.Frame(self.body, bg=BG_COLOR, padx=40, pady=30)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(self.main_frame, text="UNINSTALLATION REQUIRED", 
                                     bg=BG_COLOR, fg=CYAN_ACCENT, font=("Segoe UI Light", 18))
        self.status_label.pack(pady=(0, 10))

        self.desc_label = tk.Label(self.main_frame, text="You are about to initiate a full system purge. This action will \npermanently remove all application components and user data.", 
                                   bg=BG_COLOR, fg=TEXT_DIM, font=("Segoe UI", 9), justify=tk.CENTER)
        self.desc_label.pack(pady=(0, 30))

        # Buttons for Confirmation
        self.btn_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        self.btn_frame.pack(pady=10)

        # Modern Button Factory
        def create_btn(master, text, color, cmd):
            btn = tk.Button(master, text=text, bg=BG_COLOR, fg=color, 
                            font=("Segoe UI", 9, "bold"), padx=25, pady=10, 
                            bd=1, relief=tk.FLAT, highlightthickness=1, 
                            highlightbackground=color, activebackground=color, 
                            activeforeground=BG_COLOR, cursor="hand2", command=cmd)
            btn.bind("<Enter>", lambda e: btn.configure(bg=color, fg=BG_COLOR))
            btn.bind("<Leave>", lambda e: btn.configure(bg=BG_COLOR, fg=color))
            return btn

        self.yes_btn = create_btn(self.btn_frame, "CONFIRM PURGE", "#ff2a2a", self.start_purging)
        self.yes_btn.pack(side=tk.LEFT, padx=15)

        self.no_btn = create_btn(self.btn_frame, "ABORT MISSION", CYAN_ACCENT, self.on_close)
        self.no_btn.pack(side=tk.LEFT, padx=15)

        # Progress Area (Initially Hidden)
        self.progress_container = None
        self.log_text = None

        # Footer
        self.footer_label = tk.Label(self.body, text="SYSTEM VERSION 2.0 // CORE INTELLIGENCE LABS", 
                                     bg=BG_COLOR, fg="#333344", font=("Consolas", 8))
        self.footer_label.pack(side=tk.BOTTOM, pady=15)

        # State vars
        self.is_uninstalling = False
        self._offsetx = 0
        self._offsety = 0
        self.focus_force()

        # Center with a slight delay to ensure correct positioning
        self.after(10, self.center_window)

    def center_window(self):
        self.update_idletasks()
        width = 620
        height = 420
        
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate position to center
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Apply geometry and ensure it stays centered
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.deiconify() # Show the window after positioning

    def start_move(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def do_move(self, event):
        x = self.winfo_x() + event.x - self._offsetx
        y = self.winfo_y() + event.y - self._offsety
        self.geometry(f"+{x}+{y}")

    def on_close(self):
        if self.is_uninstalling:
            if messagebox.askyesno("Confirm", "Uninstallation is in progress. Exit anyway?"):
                self.destroy()
                sys.exit(0)
        else:
            self.destroy()
            sys.exit(0)

    def start_purging(self):
        # UI Transition
        self.btn_frame.destroy()
        self.desc_label.destroy()
        self.status_label.configure(text="SYSTEM PURGE IN PROGRESS", font=("Segoe UI Light", 14), fg=TEXT_COLOR)
        
        # Progress Bar Construction
        self.progress_canvas = tk.Canvas(self.main_frame, height=4, bg="#121225", 
                                         highlightthickness=0, bd=0)
        self.progress_canvas.pack(fill=tk.X, pady=(20, 20))
        
        self.prog_bg = self.progress_canvas.create_rectangle(0, 0, 600, 4, fill="#1a1a30", outline="")
        self.prog_bar = self.progress_canvas.create_rectangle(0, 0, 0, 4, fill=CYAN_ACCENT, outline="")
        
        # Log Area
        tk.Label(self.main_frame, text="ACCESSING LOCAL FILES...", bg=BG_COLOR, 
                 fg=CYAN_ACCENT, font=("Consolas", 8, "bold")).pack(anchor="w")
        
        self.log_text = tk.Text(self.main_frame, bg="#050510", fg=MATRIX_GREEN, height=10,
                                font=("Consolas", 9), state=tk.DISABLED, bd=0, 
                                highlightthickness=1, highlightbackground="#1a1a30", padx=10, pady=10)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        self.start_uninstall_thread()

    def log(self, message):
        if self.log_text:
            self.log_text.configure(state=tk.NORMAL)
            self.log_text.insert(tk.END, f"> {message.upper()}\n")
            self.log_text.see(tk.END)
            self.log_text.configure(state=tk.DISABLED)
            self.update_idletasks()

    def update_progress(self, percent):
        if hasattr(self, 'progress_canvas'):
            width = self.progress_canvas.winfo_width()
            new_width = (percent / 100) * width
            self.progress_canvas.coords(self.prog_bar, 0, 0, new_width, 4)
            self.update_idletasks()

    def start_uninstall_thread(self):
        self.is_uninstalling = True
        thread = threading.Thread(target=self.run_uninstallation, daemon=True)
        thread.start()

    def run_uninstallation(self):
        try:
            self.log("Accessing system files...")
            time.sleep(1)
            
            # 1. Gather files/folders
            try:
                items = os.listdir(self.app_dir)
            except Exception as e:
                self.log(f"Error accessing directory: {e}")
                items = []

            total_items = max(len(items), 1)
            
            # 2. Kill processes
            self.log("Terminating active core...")
            subprocess.run(["taskkill", "/F", "/T", "/IM", "METranslator.exe"], 
                           capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            time.sleep(0.5)
            self.update_progress(10)
            
            # 3. Delete files
            self.log("Purging application data...")
            current_exe = os.path.basename(sys.executable)
            
            for i, item in enumerate(items):
                # Don't try to delete the uninstaller itself yet
                if item == current_exe or item == "uninstall.py" or item == "uninstall.exe" or item == "_internal":
                    continue
                
                item_path = os.path.join(self.app_dir, item)
                try:
                    self.log(f"Purging: {item}...")
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                except Exception as e:
                    self.log(f"Access denied: {item}")
                
                progress = 10 + (i / total_items) * 85
                self.update_progress(progress)
                time.sleep(0.02)

            self.update_progress(95)
            self.log("Generating final cleanup script...")
            batch_script = create_cleanup_script(self.app_dir)
            
            self.update_progress(100)
            self.status_label.configure(text="UNINSTALL COMPLETE", fg=CYAN_ACCENT)
            self.log("System purged. Final cleanup in 3 seconds...")
            time.sleep(3)
            
            # Launch batch script from a neutral directory (TEMP) - ALWAYS NO WINDOW
            subprocess.Popen([batch_script], shell=True, 
                             creationflags=subprocess.CREATE_NO_WINDOW, 
                             cwd=os.environ.get('TEMP'))
            
            self.destroy()
            sys.exit(0)

        except Exception as e:
            self.log(f"FATAL ERROR: {e}")
            if self.status_label.winfo_exists():
                self.status_label.configure(text="PURGE FAILED", fg="#ff4b2b")
            self.is_uninstalling = False

def create_cleanup_script(target_dir):
    """
    Creates a robust batch script that:
    1. Moves its work context to TEMP to unlock the app folder.
    2. Waits for all processes to die.
    3. Retries deletion if it fails initially.
    """
    fd, batch_path = tempfile.mkstemp(suffix=".bat", text=True)
    os.close(fd)
    
    # Batch script content
    batch_content = f"""@echo off
title System Cleanup...
:: Move context to temp to avoid locking the target folder
cd /d "%TEMP%"
echo Waiting for uninstaller to finalize...
timeout /t 3 /nobreak > nul

:: Forcefully terminate any remaining processes
taskkill /F /T /IM "METranslator.exe" 2>nul
taskkill /F /T /IM "uninstall.exe" 2>nul

echo Purging directory: "{target_dir}"
if exist "{target_dir}" (
    :: Try deleting multiple times in case of locks
    rmdir /s /q "{target_dir}" 2>nul
    if exist "{target_dir}" (
        timeout /t 2 /nobreak > nul
        rmdir /s /q "{target_dir}" 2>nul
    )
)

echo Cleanup Phase Complete.
(goto) 2>nul & del "%~f0"
"""

    with open(batch_path, "w") as f:
        f.write(batch_content)
        
    return batch_path

def perform_uninstall():
    # Check for silent flag
    silent_mode = False
    if len(sys.argv) > 1 and any(arg.lower() in ("--silent", "/s") for arg in sys.argv):
        silent_mode = True

    # Get the directory where this script is located (the app root)
    if getattr(sys, 'frozen', False):
         app_dir = os.path.dirname(sys.executable)
    else:
         app_dir = os.path.dirname(os.path.abspath(__file__))

    if not silent_mode:
        # Launch Modern GUI for progress
        app = ModernUninstaller(app_dir, silent_mode)
        app.mainloop()
    else:
        # Silent Mode Logic
        try:
            # Simple silent path: direct batch cleanup
            batch_script = create_cleanup_script(app_dir)
            subprocess.Popen([batch_script], shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
            sys.exit(0)
        except:
            sys.exit(1)

if __name__ == "__main__":
    if not run_as_admin():
        sys.exit(0)
    perform_uninstall()
