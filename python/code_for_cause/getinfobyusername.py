import requests
import json
username = input("Enter the user name: ")
url = "https://api.github.com/users/{}".format(username)

resposne = requests.get(url)

#print(resposne.text)
#print(dir(resposne))
output = json.loads(resposne.text)
#print(output["avatar_url"])
response_images = requests.get(output["avatar_url"])

with open ("/home/maanya/Downloads/Devops_Notes/python/code_for_cause/{}.png".format(username), "wb") as f:
    f.write(response_images.content)