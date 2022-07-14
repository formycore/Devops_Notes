<<<<<<< HEAD
import os
import sys
path = input ("Enter the path: ")
if os.path.exists(path):
    os.listdir(path)
else:
    print("Please enter the valid path: ")
    sys.exit()
list_f_d=os.listdir(path)    
for f_d in os.listdir(path):
    f_d_p=os.path.join(path,f_d)
    if os.path.isfile(f_d_p):
        print(f"{f_d_p} is a file")
    else:
=======
import os
import sys
path = input ("Enter the path: ")
if os.path.exists(path):
    os.listdir(path)
else:
    print("Please enter the valid path: ")
    sys.exit()
list_f_d=os.listdir(path)    
for f_d in os.listdir(path):
    f_d_p=os.path.join(path,f_d)
    if os.path.isfile(f_d_p):
        print(f"{f_d_p} is a file")
    else:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
        print(f"{f_d_p}is a directory")    