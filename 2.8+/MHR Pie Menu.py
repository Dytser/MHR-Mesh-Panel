bl_info = {
    "name": "MHR Pie Menu",
    "author": "Dytser",
    "version": (1, 0),
    "blender": (2, 93, 3),
    "location": "Shift + R",
    "description": "Adds a pie menu for all MHR Editing in easy to access. Shift+R to open the menu by default.",
    "warning": "",
    "wiki_url": "",
    "category": "MHR",
    }

import bpy
import MHR_Mesh_Panel
from bpy.types import Menu

def draw(self, context):
    self.layout.label(text="Only available in weight paint mode")

def draw2(self, context):
    self.layout.label(text="Only available in Edit mode")

def main(context):
    bpy.ops.object.vertex_group_normalize_all(lock_active=False)

def main2(context):
    if context.weight_paint_object:
        bpy.ops.object.vertex_group_smooth(group_select_mode='ALL', factor=0.5, repeat=1)
    else:
        bpy.context.window_manager.popup_menu(draw, title="Warning", icon='INFO')

def main3(context):
    if context.weight_paint_object:
        bpy.ops.object.vertex_group_smooth(group_select_mode='ALL', factor=0.5, repeat=2)
    else:
        bpy.context.window_manager.popup_menu(draw, title="Warning", icon='INFO')


def main4(context):
    if context.weight_paint_object:
        bpy.ops.object.vertex_group_smooth(group_select_mode='ALL', factor=1.0, repeat=1)
    else:
        bpy.context.window_manager.popup_menu(draw, title="Warning", icon='INFO')

def main5(context):
    if context.weight_paint_object:
        bpy.ops.object.vertex_group_smooth(group_select_mode='ALL', factor=1.0, repeat=2)
    else:
        bpy.context.window_manager.popup_menu(draw, title="Warning", icon='INFO')

def main6(context):
    if context.edit_object:
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.tris_convert_to_quads(uvs=True)
        bpy.ops.mesh.select_all(action='DESELECT')
    else:
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.tris_convert_to_quads(uvs=True)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.editmode_toggle()


class Normalize_All(bpy.types.Operator):
    """Normalizes all and make sure lock is inactive"""
    bl_idname = "myops.normalize_all"
    bl_label = "Normalize All"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

class Smooth_Half(bpy.types.Operator):
    """Applies a smoothness of 0.5, 1 iteration"""
    bl_idname = "myops.smooth_half"
    bl_label = "Smooth 0.5"

    def execute(self, context):
        main2(context)
        return {'FINISHED'}

class Smooth_Half_Double(bpy.types.Operator):
    """Applies a smoothness of 0.5, 2 iterations"""
    bl_idname = "myops.smooth_half_double"
    bl_label = "Smooth 0.5 x 2"

    def execute(self, context):
        main3(context)
        return {'FINISHED'}
    
class Smooth_Full(bpy.types.Operator):
    """Applies a smoothness of 1.0, 1 iteration"""
    bl_idname = "myops.smooth_full"
    bl_label = "Smooth 1.0"

    def execute(self, context):
        main4(context)
        return {'FINISHED'}
    
class Smooth_Full_Double(bpy.types.Operator):
    """Applies a smoothness of 1.0, 2 iterations"""
    bl_idname = "myops.smooth_full_double"
    bl_label = "Smooth 1.0 x 2"

    def execute(self, context):
        main5(context)
        return {'FINISHED'}
class Tris_to_Quads(bpy.types.Operator):
    """Tris to Quads while Preserving UV's"""
    bl_idname = "myops.tris_to_quads_but_not_shit"
    bl_label = "Tris to Quads"

    def execute(self, context):
        main6(context)
        return {'FINISHED'}
    
class MHR_Pie_Menu(Menu):
    bl_idname = "MHR_pie_menu"
    # label is displayed at the center of the pie menu.
    bl_label = "MHR Pie Menu"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Left
        pie.operator("myops.tris_to_quads_but_not_shit", text="Tris To Quads", icon='PIVOT_BOUNDBOX')
        # Right
        pie.menu("PIE_smooth", text="Smoothing", icon='MOD_SMOOTH')
        # Bottom
        pie.menu("PIE_mhr", text="MHW to MHR", icon='OUTLINER_OB_ARMATURE')
        # Top
        pie.operator("myops.normalize_all", text="Normalize All", icon='MOD_VERTEX_WEIGHT')
        
class PIE_MHR(Menu):
    bl_idname = "PIE_mhr"
    bl_label = "MHW to MHR"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        box.operator("myops.all_transforms", icon='OUTLINER_OB_ARMATURE')
        box.separator()
        box.operator("myops.renamebreasts", icon='MESH_UVSPHERE')
        box.operator("myops.renamegenericphysics", icon='PHYSICS')

class PIE_Smooth(Menu):
    bl_idname = "PIE_smooth"
    bl_label = "Smooth Options"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        box.operator("myops.smooth_half", icon='MOD_SMOOTH')
        box.operator("myops.smooth_half_double", icon='SMOOTHCURVE')
        box.separator()
        box.operator("myops.smooth_full", icon='MOD_SMOOTH')
        box.operator("myops.smooth_full_double", icon='SMOOTHCURVE')
        
classes = (
    Normalize_All,
    Smooth_Half,
    Smooth_Full,
    MHR_Pie_Menu,
    Tris_to_Quads,
    PIE_MHR,
    PIE_Smooth,
    Smooth_Full_Double,
    Smooth_Half_Double,
    )
addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # Views numpad
        km = wm.keyconfigs.addon.keymaps.new(name='3D View Generic', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'R', 'PRESS', shift=True)
        kmi.properties.name = "MHR_pie_menu"
        addon_keymaps.append((km, kmi))

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

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