# create a resource 

import requests
import config

url = config.get_users()
# it takes only name email status gender
name = input ("Enter the name: ")
email = input ("Enter the email: ")
status = input ("Enter the status: ")
gender = input ("Enter the gender: ")

# using dictionary we can post this
data = dict()
headers = dict()
# below line is key value pair
# {
# 'key': 'Authorization',
# 'value': 'Bearer <api_key>' # bearer space api_key
#}
headers['Authorization'] = 'Bearer ' + config.access_token() 
data['name'] = name
data['email'] = email
data['status'] = status
data['gender'] = gender 

print (data)
# make a post call 
#res = requests.post(url, data, headers) this is for post a request 
res = requests.post(url, data= data, headers = headers) 
print(res)