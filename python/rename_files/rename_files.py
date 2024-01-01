import os
path = os.getcwd()
files_need_rename = []

for dir,sub_dir,files in os.walk(path):
    for file in files:
        #print(file)
        if file.endswith('.exe'):
            files_need_rename.append(os.path.join(dir,file))
    
for i in files_need_rename:
    os.rename(i,i[:-7]+'.'+i[-3:])


