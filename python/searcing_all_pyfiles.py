import glob
import os
# print(glob.glob('**/*.py',
#                 root_dir=os.getcwd(),
#                 recursive=True))

for i in glob.glob('**/*.py',root_dir="/home/maanya/Downloads/Devops_Notes/python",recursive=True):
    print(i)