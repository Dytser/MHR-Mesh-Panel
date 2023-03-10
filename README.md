# MHR-Mesh-Panel
Adds a Blender Panel to rename Vertex Groups to their MHR counterpart. And to rotate+scale meshes to help porting of MHW meshes

It also has buttons in the panel to convert any physics bones from MHW to MHR, with choices of Breastbones or generic physics bones.
Breasts assumes the breastbones uses the first two available physics bones in MHW which is 150 for the Left Breast and 152 for the Right Breast
The generic Physics bone renaming will simply name them Physics_xx

## Installation
Simply download the code in the upper section and install the panel in the respective blender versions by doing the following
### 2.8+
"Edit>Preferences>Add-ons>Install" then navigate to the file you downloaded.
There is also the optional Pie Menu that you can install for some additional functionality. (default button is Shift+R)

### 2.79
"File>User Preferences>Add-ons>Install" then navigate to the file

# Usage
Open the panel and select the object you want to convert. Then press the button that correspond to the solution you want to use.

## 2.8+
### Activating the panel:
![Step 1: Activating the panel](https://cdn.discordapp.com/attachments/742933051897806851/1063170941875662918/Step_1.gif)

### Renaming Vertex Groups & Breast bones:
![Step 2: Renaming VgGroups](https://cdn.discordapp.com/attachments/742933051897806851/1063170942290894868/Step_2.gif)

### Scale & Rotate:
![Step 3: Resize and Rotate](https://cdn.discordapp.com/attachments/742933051897806851/1063170942706122752/Step_3.gif)

## Pie Menu:
#### Shortcut key: "Shift + R"
Additional plugin that lets you access the functions from this plugin and more stuff i found useful while working.
### "Normalize all" 
This lets you quickly normalize all without locking actives (my preferred way of using normalize as i prefer to lock weight groups manually)
### "Tris to Quads" 
Will convert tris to quads on all selected objects while respecting UV's (no more broken UVs you need to repair, like seriously how is that the default mode of blender?!
### Smoothing
Opens a menu with 4 easy and useful smoothing options. "0.5", "0.5 x 2", "1.0", "1.0 x 2"
### MHW to MHR
Opens a menu that has the key parts of the above tool, "All Transformations", "Rename Breast bones" and "rename Generic Physics"

![Pie Menu Example](https://cdn.discordapp.com/attachments/742933051897806851/1066102055762137108/image.png)

 ### Original Code by Gehenna, Edited by Dytser
