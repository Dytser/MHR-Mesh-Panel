bl_info = {
    "name": "MHR Mesh Panel",
    "author": "Gehenna, Dytser",
    "version": (2, 0),
    "blender": (2, 93, 3),
    "location": "View3D > Tool Shelf > My Tab",
    "description": "Adds a MHR Panel to rename Vertex Groups to their MHR counterpart. And to rotate+scale meshes to help porting of MHW meshes",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }

import bpy

def main(context):
    ob = bpy.context.active_object
    ob.scale = ( 0.010, 0.010, 0.010 )
    ob.rotation_euler = (1.5708,0,0)

def main2(context):
    name_list = [
    ['BoneFunction.001','Spine_00'],
    ['BoneFunction.002','Spine_01'],
    ['BoneFunction.003','Neck_00'],
    ['BoneFunction.004','Head_00'],
    ['BoneFunction.005','L_Arm_00'],
    ['BoneFunction.006','L_Arm_01'],
    ['BoneFunction.007','L_Arm_02'],
    ['BoneFunction.008','L_Arm_03'],
    ['BoneFunction.009','R_Arm_00'],
    ['BoneFunction.010','R_Arm_01'],
    ['BoneFunction.011','R_Arm_02'],
    ['BoneFunction.012','R_Arm_03'],
    ['BoneFunction.013','Waist_00'],
    ['BoneFunction.013','Waist_00'],
    ['BoneFunction.014','L_Leg_00'],
    ['BoneFunction.015','L_Leg_01'],
    ['BoneFunction.016','L_Leg_02'],
    ['BoneFunction.017','L_Leg_03'],
    ['BoneFunction.018','R_Leg_00'],
    ['BoneFunction.019','R_Leg_01'],
    ['BoneFunction.020','R_Leg_02'],
    ['BoneFunction.021','R_Leg_03'],
    ['BoneFunction.031','L_Finger_00'],
    ['BoneFunction.032','L_Finger_01'],
    ['BoneFunction.033','L_Finger_02'],
    ['BoneFunction.034','L_Finger_03'],
    ['BoneFunction.035','L_Finger_04'],
    ['BoneFunction.036','L_Finger_05'],
    ['BoneFunction.037','L_Finger_06'],
    ['BoneFunction.038','L_Finger_07'],
    ['BoneFunction.039','L_Finger_08'],
    ['BoneFunction.040','L_Finger_09'],
    ['BoneFunction.041','L_Finger_10'],
    ['BoneFunction.042','L_Finger_11'],
    ['BoneFunction.043','L_Finger_12'],
    ['BoneFunction.044','L_Finger_13'],
    ['BoneFunction.045','L_Finger_14'],
    ['BoneFunction.046','L_Finger_15'],
    ['BoneFunction.048','R_Finger_00'],
    ['BoneFunction.049','R_Finger_01'],
    ['BoneFunction.050','R_Finger_02'],
    ['BoneFunction.051','R_Finger_03'],
    ['BoneFunction.052','R_Finger_04'],
    ['BoneFunction.053','R_Finger_05'],
    ['BoneFunction.054','R_Finger_06'],
    ['BoneFunction.055','R_Finger_07'],
    ['BoneFunction.056','R_Finger_08'],
    ['BoneFunction.057','R_Grip_00'],
    ['BoneFunction.058','R_Finger_09'],
    ['BoneFunction.059','R_Finger_10'],
    ['BoneFunction.060','R_Finger_11'],
    ['BoneFunction.061','R_Finger_12'],
    ['BoneFunction.062','R_Finger_13'],
    ['BoneFunction.063','R_Finger_14'],
    ['BoneFunction.070','L_Arm_00_W'],
    ['BoneFunction.071','L_Arm_01_W'],
    ['BoneFunction.072','R_Arm_00_W'],
    ['BoneFunction.073','R_Arm_01_W'],
    ['BoneFunction.074','L_Leg_00_W'],
    ['BoneFunction.075','L_Leg_01_W'],
    ['BoneFunction.076','R_Leg_00_W'],
    ['BoneFunction.077','R_Leg_01_W'],
    ['BoneFunction.080','L_Arm_01_T'],
    ['BoneFunction.082','R_Arm_01_T']
    ]
    v_groups = bpy.context.active_object.vertex_groups
    for n in name_list:
        if n[0] in v_groups:
            v_groups[n[0]].name = n[1]

def main3(context):
    name_list = [
    ['BoneFunction.150','L_Boob_00'],
    ['BoneFunction.152','R_Boob_00']
    ]
    v_groups = bpy.context.active_object.vertex_groups
    for n in name_list:
        if n[0] in v_groups:
            v_groups[n[0]].name = n[1]

def main4(context):
    name_list = [
    ['BoneFunction.150','Physics_00'],
    ['BoneFunction.152','Physics_01'],
    ['BoneFunction.154','Physics_02'],
    ['BoneFunction.156','Physics_03'],
    ['BoneFunction.158','Physics_04'],
    ['BoneFunction.160','Physics_05'],
    ['BoneFunction.162','Physics_06'],
    ['BoneFunction.164','Physics_07'],
    ['BoneFunction.166','Physics_08'],
    ['BoneFunction.168','Physics_09'],
    ['BoneFunction.170','Physics_10'],
    ['BoneFunction.172','Physics_11'],
    ['BoneFunction.174','Physics_12'],
    ['BoneFunction.176','Physics_13'],
    ['BoneFunction.178','Physics_14'],
    ['BoneFunction.180','Physics_15'],
    ['BoneFunction.182','Physics_16'],
    ['BoneFunction.184','Physics_17'],
    ['BoneFunction.186','Physics_18'],
    ['BoneFunction.188','Physics_19'],
    ['BoneFunction.190','Physics_20'],
    ['BoneFunction.192','Physics_21'],
    ['BoneFunction.194','Physics_22'],
    ['BoneFunction.196','Physics_23'],
    ['BoneFunction.198','Physics_24']
    ]
    v_groups = bpy.context.active_object.vertex_groups
    for n in name_list:
        if n[0] in v_groups:
            v_groups[n[0]].name = n[1]

class ScaleRotate(bpy.types.Operator):
    """Scales and Rotate MHW to match MHR pose"""
    bl_idname = "myops.scalerotate"
    bl_label = "Scale & Rotate"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

class RenameVG(bpy.types.Operator):
    """Renames Vertex Groups to MHR counterpart"""
    bl_idname = "myops.renamevg"
    bl_label = "Rename VG"

    def execute(self, context):
        main2(context)
        return {'FINISHED'}
    
class RenameBreasts(bpy.types.Operator):
    """Renames Vertex Groups to MHR counterpart"""
    bl_idname = "myops.renamebreasts"
    bl_label = "Rename Breasts"

    def execute(self, context):
        main3(context)
        return {'FINISHED'}

class RenameGenericPhysics(bpy.types.Operator):
    """Renames Vertex Groups to MHR counterpart"""
    bl_idname = "myops.renamegenericphysics"
    bl_label = "Rename Generic Physics"

    def execute(self, context):
        main4(context)
        return {'FINISHED'}


class MHRPanel(bpy.types.Panel):
    """Creates a Panel in the Tool Shelf"""
    bl_label = "General"
    bl_idname = "DAZ_PT_General"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MHRise Tools"

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.operator("myops.scalerotate")
        col.operator("myops.renamevg")
        col.separator()
        col.separator()
        col.operator("myops.renamebreasts")
        col.operator("myops.renamegenericphysics")
        col.separator()


classes = (
    ScaleRotate,
    RenameVG,
    MHRPanel,
    RenameBreasts,
    RenameGenericPhysics,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.myops.scalerotate()
    # bpy.ops.myops.renamevg()
    # bpy.ops.myops.combinefeet()
    # bpy.ops.myops.combinefingers()
    # bpy.ops.myops.cleanup()
    # bpy.ops.myops.addbutt()
    # bpy.ops.myops.renamecombined()