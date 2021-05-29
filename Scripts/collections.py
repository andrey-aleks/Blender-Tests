import bpy

coll_from = bpy.data.collections['Collection 1']
coll_to = bpy.data.collections['Collection 2']

temp_coll = []

for ob in coll_from:
    try:
        coll_to.objects.link(ob)
    except RuntimeError:
        pass

    temp_coll.append(ob)

for ob in temp_coll:
    try:
        coll_from.objects.unlink(ob)
    except RuntimeError:
        pass
