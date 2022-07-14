<<<<<<< HEAD
# Python program to explain os.mkdir() method 
import os
#Directory
directory="geekforgeek"
#Parent directory path
parent_dir="/mnt/c/Users/lakshmi"
# path
path=os.path.join(parent_dir,directory)
#Directory
directory="alzoret"
#Parent directory path
parent_dir="/mnt/c/Users/lakshmi"
#path
path=os.path.join(parent_dir,directory)
#mode
mode=0o666
os.mkdir(path,mode)
=======
# Python program to explain os.mkdir() method 
import os
#Directory
directory="geekforgeek"
#Parent directory path
parent_dir="/mnt/c/Users/lakshmi"
# path
path=os.path.join(parent_dir,directory)
#Directory
directory="alzoret"
#Parent directory path
parent_dir="/mnt/c/Users/lakshmi"
#path
path=os.path.join(parent_dir,directory)
#mode
mode=0o666
os.mkdir(path,mode)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print("Directory '%s' created" %directory)