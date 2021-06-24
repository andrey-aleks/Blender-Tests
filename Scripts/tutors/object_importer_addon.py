bl_info = {
    "name": "Object Importer",
    "version": (1, 0),
    "blender": (2, 90, 3),
    "author": "Andrey <andrey.aleks00@gmail.com>",
    "category": "Object",
}

import bpy

class VIEW3D_PT_object_importer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_label = 'Importer'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(context.scene, 'import_path')
        col.operator('import_scene.obj_new')

class IMPORT_SCENE_OT_importer(bpy.types.Operator):
    bl_idname = 'import_scene.obj_new'
    bl_label = "--Import--"

    def execute(self, context):
        self.report(
            {'ERROR'},
            f'No code loaded from {context.scene.import_path}')
        return {'CANCELED'}

blender_classes = [
    VIEW3D_PT_object_importer,
    IMPORT_SCENE_OT_importer
]

def register():
    bpy.types.Scene.import_path = bpy.props.StringProperty(
        name = "OBJ Folder",
        subtype='DIR_PATH',
    )
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

def unregister():
    del bpy.types.Scene.import_path
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)