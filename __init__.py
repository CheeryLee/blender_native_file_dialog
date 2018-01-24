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

# TODO: It is Mac path. Change it to cross-platform
def get_working_dir():
    path = sys.executable
    i = 0
    while i < 3:
        path = path.rpartition('/')[0]
        i += 1
    return path

if __name__ == "__main__":
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
    change_keymap.set_blender_keymap()