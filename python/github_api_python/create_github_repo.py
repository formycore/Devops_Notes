'''

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/repos \
  -d '{"name":"Hello-World","description":"This is your first repo!","homepage":"https://github.com","private":false,"is_template":true}'

'''  

import requests
import os
import json # provide the data in json 
# github token is stored as PAT 
# export PAT="enter the token here"
token = os.environ.get("PAT")
reponame=input("Enter the repo name: ")
GITHUB_API_URL = "https://api.github.com/" # here / is must
headers = {"Authorization": "token {}".format(token)} # token is getting from the env variable
data = {"name": "{}".format(reponame)} # from the above example -d is data
# for posting we need authorization for that we are using the headers

r = requests.post(GITHUB_API_URL + "user/repos" + "", data=json.dumps(data),headers=headers)
print(r)


