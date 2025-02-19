# update the available resource 
# first check the resource is available then update
# api like https://gorest.co.in/public/v2/users/ we need to append the user id 
import requests
import config

url = config.get_users()


#print(url)
res = requests.get(url)
#print(res.json())
#print(type(res.json()))

for i in res.json():
    print(i)