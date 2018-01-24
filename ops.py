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

import subprocess
import copy
import bpy
from bpy.props import BoolProperty


# TODO: It is Mac path. Change it to cross-platform
# DOUBLE POSTING
def get_working_dir():
    import sys
    
    path = sys.executable
    i = 0
    while i < 3:
        path = path.rpartition('/')[0]
        i += 1
    return path


command = get_working_dir() + "/Contents/Resources/2.79/python/bin/python3.5m "
command = command + get_working_dir() + "/Contents/Resources/2.79/scripts/addons/native_file_dialog/file_dialog.py"

###############
## Save file ##
###############
class SaveFile(bpy.types.Operator):
    bl_idname = "native_wm.save_mainfile"
    bl_label = "NATIVE: Save Blender File"
    
    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")

        # Exclude repeating when you save file once more
        if bpy.data.filepath == '':
            fileName = run_save_dialog(filetype = "save_mainfile", initialDir = None)

        try:
            if bpy.data.filepath == '':
                bpy.ops.wm.save_mainfile(filepath = fileName)
                print("INFO: File " + fileName + " saved")
            else:
                bpy.ops.wm.save_mainfile(filepath = bpy.data.filepath)
                print("INFO: File " + bpy.data.filepath + " saved")
        except RuntimeError:
            print("ERROR: Can't save file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)
    

##################
## Save file as ##
##################
class SaveFileAs(bpy.types.Operator):
    bl_idname = "native_wm.save_as_mainfile"
    bl_label = "NATIVE: Save As Blender File"
    copy = BoolProperty()

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")
        
        if bpy.data.filepath == '':
            fileName = run_save_dialog(filetype = "save_mainfile", initialDir = None)
        else:
            _initialDir = bpy.data.filepath.rpartition('/')[0]
            fileName = run_save_dialog(filetype = "save_mainfile", initialDir = _initialDir)
        
        try:
            bpy.ops.wm.save_mainfile(filepath = fileName)
            print("INFO: File " + fileName + " saved")
        except RuntimeError:
            print("ERROR: Can't save file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        self.copy = False
        return self.execute(context)


################
## Save image ##
################
class SaveImage(bpy.types.Operator):
    bl_idname = "native_image.save"
    bl_label = "NATIVE: Save Image"

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")

        for area in bpy.context.screen.areas:
            if area.type == 'IMAGE_EDITOR':
                filePath = area.spaces[0].image.filepath

        try:
            bpy.ops.image.save()
            print("INFO: File " + filePath + " saved")
        except RuntimeError:
            print("ERROR: Can't save file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


###################
## Save image as ##
###################
class SaveImageAs(bpy.types.Operator):
    bl_idname = "native_image.save_as"
    bl_label = "NATIVE: Save As Image"
    copy = BoolProperty()

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")
        
        # Get opened textfile
        for area in bpy.context.screen.areas:
            if area.type == 'IMAGE_EDITOR':
                filePath = area.spaces[0].image.filepath

        if filePath == '':
            fileName = run_save_dialog(filetype = "image_save", initialDir = None)
        else:
            _initialDir = filePath.rpartition('/')[0]
            fileName = run_save_dialog(filetype = "image_save", initialDir = _initialDir)

        if fileName != '':
            try:
                bpy.ops.image.save_as(filepath = fileName)
                print("INFO: Image file " + fileName + " saved")
            except RuntimeError:
                print("ERROR: Can't save text file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        self.copy = False
        return self.execute(context)


###############
## Save text ##
###############
class SaveText(bpy.types.Operator):
    bl_idname = "native_text.save"
    bl_label = "NATIVE: Save Text"

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")

        # Get opened textfile
        for area in bpy.context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                filePath = area.spaces[0].text.filepath

                try:
                    bpy.ops.text.save_as(filepath = filePath)
                    print("INFO: Text file " + area.spaces[0].text.name + " saved")
                except RuntimeError:
                    print("ERROR: Can't save text file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


##################
## Save text as ##
##################
class SaveTextAs(bpy.types.Operator):
    bl_idname = "native_text.save_as"
    bl_label = "NATIVE: Save As Text"

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")
        
        # Get opened textfile
        for area in bpy.context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                filePath = area.spaces[0].text.filepath

        if filePath == '':
            fileName = run_save_dialog(filetype = "text_save", initialDir = None)
        else:
            _initialDir = filePath.rpartition('/')[0]
            fileName = run_save_dialog(filetype = "text_save", initialDir = _initialDir)

        if fileName != '':
            try:
                bpy.ops.text.save_as(filepath = fileName)
                print("INFO: Text file " + fileName + " saved")
            except RuntimeError:
                print("ERROR: Can't save text file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


###############
## Open file ##
###############
class OpenFile(bpy.types.Operator):
    bl_idname = "native_wm.open_mainfile"
    bl_label = "Open Blender File"
    
    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")
        
        fileName = run_open_dialog(filetype = "open_mainfile")
        try:
            bpy.ops.wm.open_mainfile(filepath = fileName)
            print("INFO: File " + fileName + " opened")
        except RuntimeError:
            print("ERROR: Can't open file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


################
## Open image ##
################
class OpenImage(bpy.types.Operator):
    bl_idname = "native_image.open"
    bl_label = "Open Image"

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")
        
        fileName = run_open_dialog(filetype = "image_open")
        try:
            bpy.ops.image.open(filepath = fileName)
            print("INFO: File " + fileName + " opened")
        except RuntimeError:
            print("ERROR: Can't open file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


###############
## Open text ##
###############
class OpenText(bpy.types.Operator):
    bl_idname = "native_text.open"
    bl_label = "Open Text Block"

    def __init__(self):
        print("Native file dialog is working now")

    def execute(self, context):
        print("Dialog is opened")
        
        fileName = run_open_dialog(filetype = "text_open")
        try:
            bpy.ops.wm.open_mainfile(filepath = fileName)
            print("INFO: File " + fileName + " opened")
        except RuntimeError:
            print("ERROR: Can't open file!")

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


##
## Dialog functions
##
def run_open_dialog(filetype):
    fileName = subprocess.check_output(command + " " + filetype, shell = True)
    fileName = fileName.decode('UTF-8')
    fileName = fileName.strip()
    return fileName

def run_save_dialog(filetype, initialDir = None):
    if initialDir is None:
        fileName = subprocess.check_output(command + " " + filetype, shell = True)
    else:
        fileName = subprocess.check_output(command + " " + filetype + " " + initialDir, shell = True)

    fileName = fileName.decode('UTF-8')
    fileName = fileName.strip()
    return fileName

classes = (
    SaveFile,
    SaveFileAs,
    SaveImage,
    SaveImageAs,
    SaveText,
    SaveTextAs,

    OpenFile,
    OpenImage,
    OpenText
)

def _register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)