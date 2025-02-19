import requests
import os
import pprint
BASE_URL = 'https://gorest.co.in/'
BASE_PATH = 'public/' # / is must
VERSION = 'v2/'

USERS = 'users/'
POSTS = 'posts/'

def get_users():
    return BASE_URL + BASE_PATH + VERSION + USERS

res = requests.get(get_users())

#print(res)
#print("--------------------------------")
#print(res.status_code)
# print("----------------------------------------In the text format---------------------------------------")
# print(res.text)

# this is in the list output
#print(res.text)
texta = res.text

for item in texta:
    print(item)