import os
import shutil

new_path = os.path.join(os.getcwd(), 'test_1')
print(new_path)

for i in (os.listdir()):
    if os.path.isdir(i):
        shutil.move(i, new_path)
