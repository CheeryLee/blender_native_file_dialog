#
# Copyright (c) 2018 Alexander "CheeryLee" Pluzhnikov
# 
# This file is part of blender_native_file_dialog.
# 
# blender_native_file_dialog is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# blender_native_file_dialog is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with blender_native_file_dialog.  If not, see <http://www.gnu.org/licenses/>.
#

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import platform
import os
import sys
import subprocess

# raise app above all for macOS
def raise_app(root : Tk):
    root.attributes("-topmost", True)
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
        script = tmpl.format(os.getpid())
        output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
    root.after(0, lambda: root.attributes("-topmost", False))

def save_file_dialog():
    if len(sys.argv) > 2:
        if sys.argv[2] != '':
            initialDir = sys.argv[2]
    else:
        initialDir = ""

    fileName = asksaveasfilename(title = "Save Blender File",
                                    initialdir = initialDir,
                                    defaultextension = ".blend",
                                    filetypes = (("Blender projects", "*.blend"), ("", "")))
    print(fileName)

def save_image_dialog():
    pass

def save_text_dialog():
    if len(sys.argv) > 2:
        if sys.argv[2] != '':
            initialDir = sys.argv[2]
    else:
        initialDir = ""

    fileName = asksaveasfilename(title = "Save Text Block",
                                    initialdir = initialDir,
                                    defaultextension = ".txt",
                                    filetypes = (("Text files", "*.txt"),
                                    ("Python scripts", "*.py"), ("", "")))
    print(fileName)

def open_file_dialog():
    fileName = askopenfilename(filetypes = (("Blender projects", "*.blend"), ("", "")))
    print(fileName)

def open_image_dialog(root):
    pass

def open_text_dialog():
    fileName = askopenfilename(filetypes = (("Text files", "*.txt"),
                                            ("Python scripts", "*.py"), ("", "")))
    print(fileName)

if __name__ == "__main__":
    root = Tk()
    raise_app(root)
    root.focus_force()
    root.withdraw()
    
    format = sys.argv[1]

    if format == "save_mainfile":
        save_file_dialog()
    elif format == "image_save":
        save_image_dialog()
    elif format == "text_save":
        save_text_dialog()
    elif format == "open_mainfile":
        open_file_dialog()
    elif format == "image_open":
        open_image_dialog()
    elif format == "text_open":
        open_text_dialog()
    else:
        print("ERROR: Wrong argument was passed to script. Check the source!")