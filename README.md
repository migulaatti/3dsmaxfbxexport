# 3dsmaxfbxexport

Exports a .max file as an .fbx file, grabs a .jpg from a different folder/shared drive folder, prints the name and date to a .json, renames all files to name.extension, and moves all the files to the specified folder (like a shared drive location)

Includes a small UI

![3dsmax_NlmhuRGfMA](https://user-images.githubusercontent.com/56063583/206461724-aae1e578-987a-4cfa-94fa-9b1a4197c710.png)


running the script:

select scripting in the 3dsmax toolbar > maxscript listener > select python

import sys <br />
sys.path.append(r'<path>\tool')           | e.g sys.path.append(r'c:\users\<user>\desktop\tool') <br />
press enter <br />

import tool.ui <br />
dialog = tool.ui.PyMaxDialog() <br />
dialog.show() <br />
press enter
