import os

BASE_URL = 'https://gorest.co.in/'
BASE_PATH = 'public/' # / is must
VERSION = 'v2/'

USERS = 'users/'
POSTS = 'posts/'

def get_users():
	return BASE_URL + BASE_PATH + VERSION + USERS


def access_token():
	return os.environ.get('TOKEN')
	 