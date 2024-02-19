'''
import requests
response = requests.get('https://media.istockphoto.com/id/1307831372/photo/browse-high-resolution-stock-images-of-lord-ganesha.jpg?s=612x612&w=0&k=20&c=ofTjQdTxrp1IR4GI3GFWshS7-mKxrjAZVIDbH9Ts7bI=')
#print(response.content)
with open("/home/maanya/Downloads/Devops_Notes/python/code_for_cause/ganesha.png", 'wb') as f:
    f.write(response.content)
'''    
# open gitapi user
