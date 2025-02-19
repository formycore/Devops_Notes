import requests
import config

url = config.get_users()
res = requests.get(url)

print(res)