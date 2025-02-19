# update the available resource 
# first check the resource is available then update
# api like https://gorest.co.in/public/v2/users/ we need to append the user id 
import requests
import config

url = config.get_users() + "7706597" # we need to append the user id ,from the line no 19


#print(url) # https://gorest.co.in/public/v2/users/ (this is the output)
res = requests.get(url)
#print(res.json())
#print(type(res.json()))
headers = dict()
headers['Authorization'] = 'Bearer ' + config.access_token()

# update the user id data

data = dict()
data['name'] = 'Basanti Achari'

res = requests.put(url, data = data , headers = headers)

print(res.json()) # we get the error 404, it is expecting a userid value 
