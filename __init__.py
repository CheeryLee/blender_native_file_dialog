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

####
##  TODO: Change module that finds the path to script
####
import sys, os

bl_info = {
    "name": "Native File Dialog",
    "author": "Alexander Pluzhnikov",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "",
    "description": "Use native system dialogs instead of Blender ones",
    "warning": "Still in development, some parts may be broken!",
    "wiki_url": "https://github.com/CheeryLee/blender_native_file_dialog",
    "category": "System",
    }

# TODO: It is Mac path. Change it to cross-platform
def get_working_dir():
    path = sys.executable
    i = 0
    while i < 3:
        path = path.rpartition('/')[0]
        i += 1
    return path

def register():
    # TODO: It is Mac path. Change it to cross-platform
    path = get_working_dir() + "/Contents/Resources/2.79/scripts/addons/native_file_dialog"
    sys.path.append(path)
    
    import ops, change_keymap
    import _bl_ui.space_text
    import _bl_ui.space_info
    import _bl_ui.space_image
    
    # Operators registration
    ops._register()
    
    # Interface registration
    _bl_ui.space_text._register()
    _bl_ui.space_info._register()
    _bl_ui.space_image._register()

    # Hotkeys registartion
    change_keymap.set_keymap()

    print("Native file dialog is enabled")

def unregister():
    # TODO: It is Mac path. Change it to cross-platform
    path = get_working_dir() + "/Contents/Resources/2.79/scripts/addons/native_file_dialog"
    sys.path.append(path)
    
    import ops, change_keymap
    import _bl_ui.space_text
    import _bl_ui.space_info
    import _bl_ui.space_image
    import bpy

    ops._unregister()
    _bl_ui.space_text._unregister()
    _bl_ui.space_info._unregister()
    _bl_ui.space_image._unregister()
    change_keymap.remove_keymap()

    bpy.utils.unregister_module(__name__)

    # This string is buggy on stable 2.79 release on macOS.
    # Fixed in newer night versions.
    bpy.ops.script.reload()

    print("Native file dialog is disabled")

if __name__ == "__main__":
    register()