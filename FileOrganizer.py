import shutil
import os
print(os.getcwd())
path = input("What file do you want to back up?")
listoffilesandfolders = os.listdir(path)
for item in listoffilesandfolders:
    name,ext = os.path.splitext(item)
    ext = ext[1:]
    if(ext == ""):
        continue
    if(os.path.exists(path+ "/"+ext)):
        shutil.move(path + "/"+ item, path + "/" + ext + "/" + item)
    else:
        os.mkdir(path + "/" + ext)
        shutil.move(path + "/"+ item, path + "/" + ext + "/" + item)

