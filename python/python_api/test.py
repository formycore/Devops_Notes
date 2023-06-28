import requests
import json
import os

token = os.environ.get("GITHUB_TOKEN")
reponame = input("Enter the repo Name: ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization":"token {}".format(token)}
data = {"name": "{}".format(reponame)}

# This is post request 
# json.dump will convert the json file into a string
# data converts to json string
#r = requests.post(GITHUB_API_URL + "/user/repos" + "", data=json.dump(data),headers=headers)
r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(r)