<<<<<<< HEAD
import os
path = input("Enter the path: ")
'''
if os.path.isfile(path):
    print(f'The given path: {path} is a file:')
else:
    print(f'The given path is : {path} is a directory')
'''
if os.path.exists(path):
    print(f'The given path : {path} exists')
    if os.path.isfile(path):
        print(f'The given path:{path} is a file')
    else:
        print(f'The given path {path} is a directory')
else:
=======
import os
path = input("Enter the path: ")
'''
if os.path.isfile(path):
    print(f'The given path: {path} is a file:')
else:
    print(f'The given path is : {path} is a directory')
'''
if os.path.exists(path):
    print(f'The given path : {path} exists')
    if os.path.isfile(path):
        print(f'The given path:{path} is a file')
    else:
        print(f'The given path {path} is a directory')
else:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(f'The given path does not exists,\nplease enter a valid path')        