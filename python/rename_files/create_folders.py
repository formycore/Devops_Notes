"""
first create three folders
go inside the every folder and create a file with name "test_rc.exe"
"""

# import os
# folder_list = """ test testa testb"""
# for i in folder_list.split():
#     # os.mkdir(i)
import os
path = os.getcwd()
new_path = []
for dir,sub_dir,files in os.walk(path):
    new_path.append(dir)
for directory in new_path:
    os.chdir(directory)
    print(f"Now the folder is {os.getcwd()}")
    # print(f"The contents in the folder {os.listdir()}")
    with open('lenovo.txt','w'):
        pass
    

          
    

    