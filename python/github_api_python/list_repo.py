'''
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/users/USERNAME/repos

'''
import requests
import os
import json

data = {"type": "all",
        "sort": "full_name",
        "direction": "asc"}

username = input ("Enter the github username: ")
output = requests.get("https://api.github.com/users/{}/repos".format(username),data = json.dumps(data))
output = json.loads(output.text)
#print(output)

for reponame in output:
	#print(reponame)
	print(reponame['name'])
