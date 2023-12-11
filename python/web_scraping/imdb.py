# from bs4 import BeautifulSoup
# import requests
# source = requests.get('https://www.imdb.com/chart/top/')
# # here in the source we have html of the source code of https://www.imdb.com/chart/top/
# source.raise_for_status()
# # if the url have some issues raise_for_status throw an error
# # when we use request.get use raise_for_status if there are any errors


from bs4 import BeautifulSoup
import requests
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
except Exception as e:
    print(e)