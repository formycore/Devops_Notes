import requests
import config

# to which we make a get request 
url = config.get_users()
res = requests.get(url)

#print(res.json())
#print(type(res.json()))
#if we use res.text it will be in the string format 
# if we use the for loop the output will be in the single line

for i in res.json():
    print(i["name"])