# Native file dialog for Blender

Native file dialog add-on for Blender. It uses Tkinter as the default window system.

From this:

![Screenshot](https://github.com/CheeryLee/blender_native_file_dialog/blob/2.79/data/std_dialog.png "How it was")
... to this:

![Screenshot](https://github.com/CheeryLee/blender_native_file_dialog/blob/2.79/data/native_dialog.png "How it becomes")

# How to install
## macOS
1. Be sure that **Tcl/Tk** are already installed in the system. Commonly they are named as ```Tk.framework``` and ```Tcl.framework``` and placed in ```/Library/Frameworks/``` folder. If there are no such files, follow the next step. Otherwise, read step 3.
2. Firstly you need to install **Tcl/Tk** frameworks for your system. The best choice is **ActiveTcl**. You can find it here: https://www.python.org/download/mac/tcltk/.
3. After installation download one of the add-on's releases and place the folder in ```blender.app/Contents/Resources/<version>/scripts/addons``` (blender.app directory can be opened by mouse right button clicking on "Show Package Contents").
4. Run Blender. Click ```File -> User Preferences.. -> Add-ons -> System```. Make ```System: Native File Dialog``` active.
5. Now native file dialog system are working. There will be the system dialogs instead of standard ones (the screenshots above shows the macOS example).

# Disclaimer
There may be errors in the process of work. Add-on overloads already built-in Python scripts. It's absolutely impossible to rewrite everything without rebuilding the whole editor. 
