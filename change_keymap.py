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
    'Screen',
    'Image Generic',
    'Text'
)

save_idnames = (
    'wm.save_mainfile',
    'wm.save_as_mainfile',
    'image.save',
    'image.save_as',
    'text.save',
    'text.save_as'
)

open_idnames = (
    'wm.open_mainfile',
    'image.open',
    'text.open'
)

def set_blender_keymap():
    make_keymap(config = 'Blender')

def make_keymap(config):
    wm = bpy.context.window_manager

    for km in keymap_names:
        keymaps = wm.keyconfigs[config].keymaps[km]

        # Save keymap
        for k in keymaps.keymap_items:
            for id in save_idnames:
                if k.idname == id:
                    keymaps.keymap_items.new("native_" + id, k.type, k.value, any = k.any, 
                                            shift = k.shift, ctrl = k.ctrl, alt = k.alt, oskey = k.oskey, 
                                            key_modifier = k.key_modifier)
                    k.active = False

        # Open keymap
        for k in keymaps.keymap_items:
            for id in open_idnames:
                if k.idname == id:
                    keymaps.keymap_items.new("native_" + id, k.type, k.value, any = k.any, 
                                            shift = k.shift, ctrl = k.ctrl, alt = k.alt, oskey = k.oskey, 
                                            key_modifier = k.key_modifier)
                    k.active = False