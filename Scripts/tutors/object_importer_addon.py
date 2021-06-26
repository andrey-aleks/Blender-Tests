bl_info = {
    "name": "Object Importer",
    "version": (1, 0),
    "blender": (2, 90, 3),
    "author": "Andrey <andrey.aleks00@gmail.com>",
    "category": "Object",
}

import bpy
import pathlib


## defs

def import_files(context, import_fname):
    abspath = bpy.path.abspath(context.scene.import_path)
    import_path = pathlib.Path(abspath)        
    for import_fpath in import_path.glob(str(import_fname)):
        bpy.ops.import_scene.fbx(filepath=str(import_fpath))
        for imported_fbx in context.selected_objects:
            imported_fbx.import_fname = import_fpath.name

## PTs ##

class VIEW3D_PT_object_importer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_label = 'Importer'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(context.scene, 'import_path')
        col.operator('import_scene.fbx_new')

        col = layout.column(align=True)
        if context.object:
            col.prop(context.object, 'import_fname')
            col.operator('import_scene.fbx_reload')
        else:
            col.label(text='No active object') 

## OTs ##

class IMPORT_SCENE_OT_importer(bpy.types.Operator):
    bl_idname = 'import_scene.fbx_new'
    bl_label = "--Import--"

    def execute(self, context):
        import_files(context, '*.fbx')
        return {'FINISHED'}


class IMPORT_SCENE_OT_reloader(bpy.types.Operator):
    bl_idname = 'import_scene.fbx_reload'
    bl_label = "--Reload--"

    def execute(self, context):
        ob = context.object
        import_fname = ob.import_fname
        matrix_world = ob.matrix_world.copy()

        for collection in list(ob.users_collection):
            collection.objects.unlink(ob)

        if ob.users == 0:
            bpy.data.objects.remove(ob)
        del ob

        import_files(context, import_fname)

        for imported_ob in context.selected_objects:
            imported_ob.matrix_world = matrix_world

        return {'FINISHED'}


##

blender_classes = [
    VIEW3D_PT_object_importer,
    IMPORT_SCENE_OT_importer,
    IMPORT_SCENE_OT_reloader,
]


## 

def register():
    bpy.types.Scene.import_path = bpy.props.StringProperty(
        name = "OBJ Folder",
        subtype='DIR_PATH',
    )

    bpy.types.Object.import_fname = bpy.props.StringProperty(
        name = "OBJ File",
    )

    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

def unregister():
    del bpy.types.Scene.import_path
    del bpy.types.Object.import_fname
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)