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

import bpy

keymap_names = (
    'Window',
    'Image Generic',
    'Text'
)

addon_idnames = (
    'native_wm.save_mainfile',
    'native_wm.save_as_mainfile',
    'native_image.save',
    'native_image.save_as',
    'native_text.save',
    'native_text.save_as',
    'native_wm.open_mainfile',
    'native_image.open',
    'native_text.open'
)

def set_keymap():
    make_keymap()

def remove_keymap():
    wm = bpy.context.window_manager

    for kn in keymap_names:
        for k in wm.keyconfigs.addon.keymaps[kn].keymap_items:
            for name in addon_idnames:
                if name == k.idname:
                    wm.keyconfigs.addon.keymaps[kn].keymap_items.remove(k)
                    print(name + " is removed")
                    break

def make_keymap():
    wm = bpy.context.window_manager

    keymaps = wm.keyconfigs.addon.keymaps.new(name = 'Window', space_type='EMPTY', region_type='WINDOW')
    keymaps.keymap_items.new("native_wm.save_mainfile", "S", "PRESS", oskey = True)
    keymaps.keymap_items.new("native_wm.save_mainfile", "S", "PRESS", ctrl = True)
    keymaps.keymap_items.new("native_wm.save_mainfile", "W", "PRESS", ctrl = True)
    keymaps.keymap_items.new("native_wm.save_as_mainfile", "S", "PRESS", oskey = True, shift = True)
    keymaps.keymap_items.new("native_wm.save_as_mainfile", "S", "PRESS", ctrl = True, shift = True)
    keymaps.keymap_items.new("native_wm.save_as_mainfile", "F2", "PRESS")
    keymaps.keymap_items.new("native_wm.save_as_mainfile", "S", "PRESS", ctrl = True, alt = True)
    keymaps.keymap_items.new("native_wm.open_mainfile", "O", "PRESS", ctrl = True)
    keymaps.keymap_items.new("native_wm.open_mainfile", "O", "PRESS", oskey = True)
    keymaps.keymap_items.new("native_wm.open_mainfile", "F1", "PRESS")

    keymaps = wm.keyconfigs.addon.keymaps.new(name = 'Image Generic', space_type='IMAGE_EDITOR', region_type='WINDOW')
    keymaps.keymap_items.new("native_image.save", "S", "PRESS", alt = True)
    keymaps.keymap_items.new("native_image.save_as", "F3", "PRESS")
    keymaps.keymap_items.new("native_image.open", "O", "PRESS", alt = True)

    keymaps = wm.keyconfigs.addon.keymaps.new(name = 'Text', space_type='TEXT_EDITOR', region_type='WINDOW')
    keymaps.keymap_items.new("native_text.save", "S", "PRESS", alt = True, oskey = True)
    keymaps.keymap_items.new("native_text.save", "S", "PRESS", alt = True)
    keymaps.keymap_items.new("native_text.save_as", "S", "PRESS", alt = True, shift = True, oskey = True)
    keymaps.keymap_items.new("native_text.save_as", "S", "PRESS", alt = True, shift = True, ctrl = True)
    keymaps.keymap_items.new("native_text.open", "O", "PRESS", alt = True)