# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import pprint
api_token = "ATATT3xFfGF0XCPwjBk58u5B1k2cwCVJpgWhxjRXySuG9OM-gYzp_C8HP5QR9dWTKy_hctfGZCehfHdqSwBfiMgNxig2ZJ5Ys-IWhXuWhmm04R1kH6sFfATztAnjpoV4ek7AupUF0ZljjvsnykjXJx65csDxkvXIIrvfQTinCdMm3t1l_awdAKY=C8B60F49"

url = "https://mcadevopstopics.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("mcadevopstopics@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

#name = output[0]["name"]
#print(name)

# for project in output:
#     name = project["name"]
#     print(name)
#print(output)

for project in output:
    name = project["name"]
    print(name)