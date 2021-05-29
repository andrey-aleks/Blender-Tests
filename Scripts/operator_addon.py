bl_info = {
    "name": "Object Creator",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "author": "Andrey <andrey.aleks00@gmail.com>",
    "category": "Mesh",
}
import bpy

class MESH_OT_object_creator(bpy.types.Operator):
    """Creates some object"""
    bl_idname = 'mesh.object_creator'
    bl_label = 'Object Creator'
    bl_options = {'REGISTER', 'UNDO'}

    count_x = bpy.props.IntProperty(
        name = "Count x",
        description = "Amount of obj at X-dir",
        default=1,
        min = 1, soft_max = 10,
    )

    size = bpy.props.FloatProperty(
        name = "Size",
        description = "Size of objs",
        default=1,
        min = 0, soft_max = 2,
    )

    def execute(self, context):
        for adds in range(self.count_x):
            bpy.ops.mesh.primitive_cube_add(location=(adds, 1, 1), size=self.size)

        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bpy.context.area.type == 'VIEW_3D'


def menu_func(self, context):
    self.layout.operator(MESH_OT_object_creator.bl_idname)

def register():
    bpy.utils.register_class(MESH_OT_object_creator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(MESH_OT_object_creator)
