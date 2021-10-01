bl_info = {
    "name": "Custom Import/Export",
    "version": (1, 0, 0),
    "blender": (2, 80, 3),
    "author": "Andrey Alekseev <andrey.aleks00@gmail.com>",
    "location": "3D-viewport -> N-panel -> Tool -> Custom Import/Export",
    "description": "Allows you to import some FBX, do some changes and rewrite this FBX at one click",
    "warning": "Works only with FBX",
    "category": "Object",
}
import bpy
import pathlib


# returns file's path
def get_fname_path(context):
        abspath = bpy.path.abspath(context.scene.fname)
        fname_path = pathlib.Path(abspath)
        return fname_path   


# import operator
class IMPORT_SCENE_OT_importer(bpy.types.Operator):
    bl_idname = 'import_scene.fbx_custom'
    bl_label = "Import FBX"

    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=str(get_fname_path(context)))
        return {'FINISHED'}


# export operator. Uses selected objects, applies all transforms, export selected
# Export settings: "Selected Objects" true, Object Types - only MESH, "Apply Transform" true, "Bake Animations" false. Other settings by default
class EXPORT_SCENE_OT_custom_export(bpy.types.Operator):
    bl_idname = 'export_scene.fbx_custom'
    bl_label = 'Export FBX'

    def execute(self, context):
        export_obs = context.selected_objects
        if export_obs:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.export_scene.fbx(filepath=str(get_fname_path(context)), use_selection=True, object_types={'MESH'}, bake_space_transform=True, bake_anim=False)
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI panel
class VIEW3D_PT_custom_export(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_label = 'Custom Import/Export'

    def draw(self, context):
        col = self.layout
        col.prop(context.scene, 'fname')
        col.operator('import_scene.fbx_custom')
        col = self.layout
        col.operator('export_scene.fbx_custom')

##

blender_classes = [
    VIEW3D_PT_custom_export,
    IMPORT_SCENE_OT_importer,
    EXPORT_SCENE_OT_custom_export,
]

## 

def register():
    bpy.types.Scene.fname = bpy.props.StringProperty(
        name = "FBX Filename",
        subtype='FILE_PATH',
    )

    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

def unregister():
    del bpy.types.Scene.fname

    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)