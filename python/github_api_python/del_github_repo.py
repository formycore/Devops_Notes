'''
curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO

'''
import requests
import os
import json

token = os.environ.get("PAT")
reponame = input("Enter the repo name to delete:" )
username = input ("Enter the username: ")
GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

r = requests.delete("https://api.github.com/repos/{}/{}".format(username,reponame), headers = headers)
print(r)

	