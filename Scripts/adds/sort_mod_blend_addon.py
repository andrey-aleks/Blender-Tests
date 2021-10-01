bl_info = {
    "name": "SortMod",
    "version": (1, 0, 6),
    "blender": (2, 80, 3),
    "author": "Andrey Alekseev <andrey.aleks00@gmail.com>",
    "location": "3D-viewport -> N-panel -> Tool -> Custom Import/Export",
    "description": "Allows you to import some FBX, do some changes and rewrite this FBX at one click",
    "warning": "Works only with FBX",
    "category": "Object",
}
import bpy
import random


class SORT_MOD_OT_sort_mod(bpy.types.Operator):
    bl_idname = 'mesh.sort_mod'
    bl_label = "Sort_Mod"
    bl_options = {'REGISTER', 'UNDO'}

    min_shift = bpy.props.FloatProperty(
        name = "Min shift",
        description = "Min shift on Z-axis",
        default=0.1,
        soft_min = -100, soft_max = 100,
    )

    max_shift = bpy.props.FloatProperty(
        name = "Max shift",
        description = "Max shift on Z-axis",
        default=1,
        soft_min = -100, soft_max = 100,
    )

    def execute(self, context):
        objects = bpy.context.selected_objects
        #objects.sort(reverse=True) # need iteration by names, not objs
        for obj in objects:
            obj.location[2] += random.uniform(context.scene.min_shift, context.scene.max_shift)
            mod = obj.modifiers.get("Solidify")
            if mod is None:
                mod = obj.modifiers.new("Solidify", 'SOLIDIFY')
        return {'FINISHED'}


# UI panel
class VIEW3D_PT_sort_mod(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_label = 'SortMod'

    def draw(self, context):
        col = self.layout.column()

        col.prop(bpy.context.scene, 'min_shift')
        col.prop(bpy.context.scene, 'max_shift')
        col.operator('mesh.sort_mod', text='Sort and Mod')

        

##

blender_classes = [
    SORT_MOD_OT_sort_mod,
    VIEW3D_PT_sort_mod,
]

## 

def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

    bpy.types.Scene.min_shift = bpy.props.FloatProperty(name="min_shift", default=0.1)
    bpy.types.Scene.max_shift = bpy.props.FloatProperty(name="max_shift", default=1)


def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
    del bpy.types.Scene.min_shift
    del bpy.types.Scene.max_shift