bl_info = {
    "name": "Custom Im/Ex-port",
    "version": (0, 1, 0),
    "blender": (2, 80, 3),
    "author": "Andrey <andrey.aleks00@gmail.com>",
    "category": "Object",
}
import os
import bpy
import pathlib

class EXPORT_SCENE_OT_custom_export(bpy.types.Operator):
    bl_idname = 'export_scene.fbx_custom'
    bl_label = 'Custom Export'

    def execute(self, context):

        export_obs = context.selected_objects
        if export_obs:
            for ob in export_obs:
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        else:
            return {'CANCELLED'}

        # abspath = bpy.path.abspath(context.scene.export_path)
        # export_path = pathlib.Path(abspath)

        target_file = os.path.join(context.scene.export_path, context.scene.export_fname)
        bpy.ops.export_scene.fbx(filepath=target_file, use_selection=True, object_types={'MESH'}, bake_space_transform=True, bake_anim=False)

        return {'FINISHED'}

class EXPORT_SCENE_PT_custom_export(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_label = 'Im/Ex'

    def draw(self, context):
        col = self.layout

        col.operator('export_scene.fbx_custom')



blender_classes = [
    EXPORT_SCENE_PT_custom_export,
    EXPORT_SCENE_OT_custom_export,
]


## 

def register():
    bpy.types.Scene.export_path = bpy.props.StringProperty(
        name = "FBX Folder",
        subtype='DIR_PATH',
        default='//',
    )

    bpy.types.Scene.export_fname = bpy.props.StringProperty(
        name = "FBX Filename",
    )

    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

def unregister():
    del bpy.types.Scene.export_path
    del bpy.types.Scene.export_fname

    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)