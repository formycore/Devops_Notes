import os
path = os.getcwd()
os.listdir(path)

for i in os.listdir(path):
    if i.endswith(".png"):
        os.remove(i)