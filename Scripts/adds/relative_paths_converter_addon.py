bl_info = {
    "name": "RelativePathConverter",
    "version": (1, 0, 0),
    "blender": (2, 90, 3),
    "author": "Andrey Alekseev",
    "location": "Image Editor -> N-panel -> Image -> RelativePathConverter",
    "description": "Converts image's absolute path to relative path",
    "category": "Image",
}
import bpy
from pathlib import Path


class Relative_Path_Converter_OT(bpy.types.Operator):
    bl_idname = 'image.relative_path_converter'
    bl_label = "RelativePathConverter"
    bl_description = "Converts image's absolute path to relative path"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        abs_filepath =  context.edit_image.filepath
        #parent_path = Path (abs_filepath).parent.absolute()
        #print(parent_path)
        #context.edit_image.filepath = bpy.path.relpath(abs_filepath, parent_path.parent.absolute())
        context.edit_image.filepath = bpy.path.relpath(abs_filepath)
        return {'FINISHED'}


# UI panel
class VIEW3D_PT_Relative_Path_Converter(bpy.types.Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Image'
    bl_label = 'RelativePathConverter'

    def draw(self, context):
        col = self.layout.column()
        col.operator('image.relative_path_converter', text='Convert Path')

        

##

blender_classes = [
    Relative_Path_Converter_OT,
    VIEW3D_PT_Relative_Path_Converter,
]

## 

def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)


def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)