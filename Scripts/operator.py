import bpy

class MESH_OT_object_creator(bpy.types.Operator):
    """Creates some object"""
    bl_idname = 'mesh.object_creator'
    bl_label = 'Object Creator'

    def execute(self, context):
        for adds in range(20):
            bpy.ops.mesh.primitive_cube_add()

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(MESH_OT_object_creator.bl_idname)

def register():
    bpy.utils.register_class(MESH_OT_object_creator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(MESH_OT_object_creator)

if __name__ == '__main__':
    register()
