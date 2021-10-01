bl_info = {
    "name": "RandomHeigher",
    "version": (1, 0, 6),
    "blender": (2, 80, 3),
    "author": "Andrey Alekseev <andrey.aleks00@gmail.com>",
    "location": "3D-viewport -> N-panel -> Tool -> RandomHeigher",
    "description": "Adds different value on Z-axis to selected objects (SO); adds Solidify to SO",
    "category": "Object",
}
import bpy
import random


class Random_Heigher_OT(bpy.types.Operator):
    bl_idname = 'mesh.random_heigher'
    bl_label = "RandomHeigher"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objects = bpy.context.selected_objects
        for obj in objects:
            obj.location[2] += random.uniform(context.scene.min_shift, context.scene.max_shift)
            mod = obj.modifiers.get("Solidify")
            if mod is None:
                mod = obj.modifiers.new("Solidify", 'SOLIDIFY')
        return {'FINISHED'}


# UI panel
class VIEW3D_PT_Random_Heigher(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_label = 'RandomHeigher'

    def draw(self, context):
        col = self.layout.column()

        col.prop(bpy.context.scene, 'min_shift')
        col.prop(bpy.context.scene, 'max_shift')
        col.operator('mesh.random_heigher', text='RandomHeigher')

        

##

blender_classes = [
    Random_Heigher_OT,
    VIEW3D_PT_Random_Heigher,
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