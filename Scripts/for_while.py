import bpy

mesh = bpy.context.active_object.data

for subdivs in range(4):
    if len(mesh.vertices) <= 100000:
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action='SELECT')        
        bpy.ops.mesh.subdivide()
        bpy.ops.object.mode_set(mode = 'OBJECT')
    else:
        break
