import bpy

class PropGroup(bpy.types.PropertyGroup):
    my_int: bpy.props.IntProperty()
    my_float: bpy.props.FloatProperty()

def register():
    bpy.utils.register_class(PropGroup)


if __name__ == '__main__':
    register()


#class OT
    #bl

    #props

    #execute

#class PT
    #bl

    #draw


#reg

#unreg