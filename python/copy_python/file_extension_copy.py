import pathlib
import shutil
import os
new_dir = "test"
path = "/home/maanya/Downloads/Devops_Notes/python/copy_python"
# create a new directory test and move the .ipynb files to it with os.walk()
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.ipynb'):
            shutil.move(os.path.join(foldername, filename), os.path.join(foldername, 'test'))
