import os
import shutil

source='/Users/setumadhavinamburu/Downloads/hi'
destination='/Users/setumadhavinamburu/Desktop'
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    if ext=='':
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + '/' + i
        if os.path.exists(path2):
            print('folder already exist and moving the files')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('making folder and moving the files')
            shutil.move(path1,path3)

