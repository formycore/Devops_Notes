import requests
from pprint import pprint
import os

api_url = "https://api.github.com"
repo_name = "TestName"
payload = '{"name": "' + repo_name + '"}'
headers = {
    "Authorization": "token " + os.environ.get("GITPAT"),
    "Accept": "application/vnd.github.v3+json"
}
r = requests.post(api_url + "/user/repos", data=payload, headers=headers)

# Check for errors in the response
if r.status_code != 201:
    print("Error creating repository:")
    pprint(r.json())
else:
    print(f"Repository '{repo_name}' created successfully.")
