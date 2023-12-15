# use os.walk () method
# os.walk discover everything under it's path
"""
.
└── os_files
    ├── 1.txt
    ├── 2.txt
    ├── 3.txt
    └── Folder_1
        ├── Folder1_1.txt
        ├── Folder1_2.txt
        ├── Folder1_3.txt
        └── Folder_1_subfolder_1
            ├── subfolder_1_1.txt
            ├── subfolder_1_2.txt
            └── subfolder_1_3.txt

3 directories, 9 files
"""
import os
path = ("/home/maanya/Downloads/other_github/python_pathlib_demo")
for dirpath,dirnames,filenames in os.walk(path):
    print(f"Root {dirpath}\n"
         f"Sub-directories {dirnames}\n"
         f"Files {filenames}")
