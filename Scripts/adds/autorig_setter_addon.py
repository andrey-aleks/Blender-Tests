bl_info = {
    "name": "Bones Constraints AutoSetter",
    "version": (1, 0, 0),
    "blender": (2, 90, 3),
    "author": "Andrey Alekseev",
    "location": "3D-viewport -> N-panel -> Tool -> BonesConstraintsAutoSetter",
    "description": "Tool automatically sets \"Target\" for all bones constraints at one click. It works only for constraints: COPY_LOCATION, COPY_ROTATION, COPY_SCALE, COPY_TRANSFORMS",
    "category": "Animation",
}
import bpy

# Main operator 
class Bones_Constraints_AutoSetter_OT(bpy.types.Operator):
    bl_idname = 'mesh.bones_constraints_autosetter'
    bl_label = 'BonesConstraintsAutoSetter'
    bl_description = "Set Source Rig as \"Target\" for bones constraints"
    bl_options = {'REGISTER', 'UNDO'}

    # list of available constraints
    constraints = [
        "COPY_LOCATION",
        "COPY_ROTATION",
        "COPY_SCALE",
        "COPY_TRANSFORMS",
    ]

    def execute(self, context):
        obj = bpy.context.active_object
        for bone in obj.pose.bones:
            for constraint in bone.constraints:                
                if any(constraint.type in _constraint for _constraint in self.constraints):
                    constraint.target = context.scene.source_rig

        return {'FINISHED'}


# UI panel
class VIEW3D_PT_Bones_Constraints_AutoSetter(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_label = 'BonesConstraintsAutoSetter'

    def draw(self, context):
        col = self.layout.column()

        col.prop(context.scene, "source_rig")
        col.operator('mesh.bones_constraints_autosetter', text="Set \"Target\"")

        

##

blender_classes = [
    Bones_Constraints_AutoSetter_OT,
    VIEW3D_PT_Bones_Constraints_AutoSetter,
]

## 

def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)
    bpy.types.Scene.source_rig = bpy.props.PointerProperty(type=bpy.types.Object, name="Source Rig Object")


def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
    del bpy.types.Scene.source_rig