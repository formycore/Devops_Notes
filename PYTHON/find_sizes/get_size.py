import os
for root,dirs,files in os.walk("/home/maanya/Downloads/from_ubuntu/Devops_Notes/PYTHON"):
	for name in dirs:
		print(os.path.join(root,name))
        
# find the size of the directory
# Path: get_size.py
