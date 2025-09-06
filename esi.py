# ESI is the eve's official API. https://developers.eveonline.com/api-explorer#/operations/GetCharactersCharacterIdTitles
import requests
import json
from evesso import SSO # Necessary for Auth https://developers.eveonline.com/docs/services/sso/
from dotenv import load_dotenv # Cred manager from .env file
import os

# Load .env (create and fill it first in the same directory)
load_dotenv()

# Load .env to sso
# sso = SSO()

# Checks. Works!
my_variable = os.getenv('CHARACTER_ID')
another_key = os.getenv('CALLBACK_URL')
print(f'{my_variable}, {another_key}')

# auth_link = 'https://login.eveonline.com/v2/oauth/token'


#
# a = requests.post(url=auth_link, params=token)
# r = requests.get(url=f'{link}{character_id}/orders', params=token)
# print(r)