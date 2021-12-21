bl_info = {
    "name": "Relative Path Converter",
    "version": (1, 0, 0),
    "blender": (2, 90, 3),
    "author": "Andrey Alekseev",
    "location": "Image Editor -> N-panel -> Image -> RelativePathConverter",
    "description": "Converts image's absolute path to relative path",
    "category": "Image",
}
import bpy
from pathlib import Path


class RPCAddonSettings(bpy.types.PropertyGroup):
    convert_all: bpy.props.BoolProperty(
        name="Convert All", 
        default=False,
        description="If true, tool will convert all images path's from absolute to relative. If false, it will convert only selected image's path"
    )   

# Main operator 
class IMAGE_OT_Relative_Path_Converter(bpy.types.Operator):
    bl_idname = 'image.relative_path_converter'
    bl_label = 'RelativePathConverterOT'
    bl_description = 'Converts image\'s absolute path to relative path'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.rpc_addon_settings.convert_all:
            all_images = bpy.data.images
            for image in all_images:
                if image.filepath != "":
                    image.filepath = bpy.path.relpath(image.filepath)
        else:
            abs_filepath =  context.edit_image.filepath
            #parent_path = Path (abs_filepath).parent.absolute()
            #context.edit_image.filepath = bpy.path.relpath(abs_filepath, parent_path.parent.absolute())
            context.edit_image.filepath = bpy.path.relpath(abs_filepath)
        return {'FINISHED'}


# UI panel
class IMAGE_EDITOR_PT_Relative_Path_Converter(bpy.types.Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Image'
    bl_label = 'RelativePathConverterPT'

    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene.rpc_addon_settings, "convert_all")
        col.operator('image.relative_path_converter', text='Convert Path')

        

##

blender_classes = [
    IMAGE_OT_Relative_Path_Converter,
    IMAGE_EDITOR_PT_Relative_Path_Converter,
    RPCAddonSettings
]

## 

def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)
    bpy.types.Scene.rpc_addon_settings = bpy.props.PointerProperty(type=RPCAddonSettings)


def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
    bpy.types.Scene.rpc_addon_settings
