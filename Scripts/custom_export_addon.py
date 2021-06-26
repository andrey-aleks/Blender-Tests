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

def import_files(context, import_fname):
    abspath = bpy.path.abspath(context.scene.import_path)
    import_path = pathlib.Path(abspath)        
    for import_fpath in import_path.glob(str(import_fname)):
        bpy.ops.import_scene.fbx(filepath=str(import_fpath))
        for imported_fbx in context.selected_objects:
            imported_fbx.import_fname = import_fpath.name

class IMPORT_SCENE_OT_importer(bpy.types.Operator):
    bl_idname = 'import_scene.fbx_custom'
    bl_label = "Import FBX"

    def execute(self, context):

        abspath = bpy.path.abspath(context.scene.export_fname)
        export_path = pathlib.Path(abspath)        
        bpy.ops.import_scene.fbx(filepath=str(export_path))
        return {'FINISHED'}


class EXPORT_SCENE_OT_custom_export(bpy.types.Operator):
    bl_idname = 'export_scene.fbx_custom'
    bl_label = 'Export FBX'

    def execute(self, context):

        export_obs = context.selected_objects
        if export_obs:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            abspath = bpy.path.abspath(context.scene.export_fname)
            export_path = pathlib.Path(abspath) 
            bpy.ops.export_scene.fbx(filepath=str(export_path), use_selection=True, object_types={'MESH'}, bake_space_transform=True, bake_anim=False)
            return {'FINISHED'}
        else:
            return {'CANCELLED'}





class VIEW3D_PT_custom_export(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_label = 'Im/Ex'

    def draw(self, context):
        col = self.layout
        col.prop(context.scene, 'export_fname')
        col.operator('import_scene.fbx_custom')
        col = self.layout
        col.operator('export_scene.fbx_custom')



blender_classes = [
    VIEW3D_PT_custom_export,
    IMPORT_SCENE_OT_importer,
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
        subtype='FILE_PATH',
    )

    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

def unregister():
    del bpy.types.Scene.export_path
    del bpy.types.Scene.export_fname

    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)