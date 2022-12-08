from pymxs import runtime as rt
import os
import shutil
import json


#define folders

maxFolder = r"<drive letter>:\<path>"
thumbN = r"<drive letter>:\<shared drive name>\<pathtojpg>"
gFolder = r"<drive letter>:\<shared drive name>\<path>"

# Find any .max files in the folder specified and export to .fbx
def export_files(nameText, dateText):
    for file in os.listdir(maxFolder):
        if file.endswith((".max", ".MAX")):
            fPath = os.path.join(maxFolder, file)
            fPath = fPath.replace('\\', '\\\\')

            fPathExport = fPath.replace('.max', '').replace('.MAX', '')
            rt.loadMaxFile(fPath, quiet=True, prompt=False, useFileUnits=False)

            fPathExport = fPathExport + '.fbx'

            rt.exportFile(fPathExport, rt.Name('noPrompt'), selectedOnly=False)
    
    #grab .jpg from a google drive folder
    for file in os.listdir(thumbN):
        
        #check if dir is empty, if not, move file (.jpg)
        if len(os.listdir(thumbN)) == 0:
            continue
        elif file.endswith((".jpg", ".JPG")):
            shutil.move(os.path.join(thumbN, file), os.path.join(maxFolder, file))
        else:
            continue
    
    #write the name and date to a.json file
    os.chdir(maxFolder)
    aDict = {"name":nameText, "date":dateText}
    jString = json.dumps(aDict)
    jFile = open(nameText + ".json", "w")
    jFile.write(jString)
    jFile.close()
    
    #rename all files to <name>.<extension>
    for file in os.listdir(maxFolder):
        split = os.path.splitext(file)

        #check if file exists, else continue
        if os.path.isfile(nameText + split[1]):
            continue
        else:
            os.rename(os.path.join(maxFolder, file), 
                os.path.join(maxFolder, nameText + split[1]))

    #move all files into the google drive folder
    for file in os.listdir(maxFolder):

        #check if dir is empty, if not, move files
        if len(os.listdir(maxFolder)) == 0:
            continue
        else:
            shutil.move(os.path.join(maxFolder, file), os.path.join(gFolder, file))
    
    print("Finished")

    
    