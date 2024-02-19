import requests
from pprint import pprint
import os
#token = os.environ.get("PAT")
#print(token)
# set the token as environmental variable 
# echo PAT="<123456789>" >> ~/.bashrc
# source ~/.bashrc
# curl -i -u <username>:$PAT https://api.github.com/users/<username>
#https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-a-repository-for-the-authenticated-user <to create repo for auth user>
api_url = "https://api.github.com"
repo_name = "TestingName"
payload = '{"name": "' + repo_name + '"}'
#payload = '{name: "TestName"}'
#payload = '{"name":"name_of_the_repo"}'
headers = {
    "Authorization": "token" + os.environ.get("GITPAT"),
    "Accept": "application/vnd.github+json"
}
r = requests.post(api_url+"/users/repos", data=payload, headers=headers)
# parse the response using json
pprint(r.json())