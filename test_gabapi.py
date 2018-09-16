import os
import requests
import sys
from gabapi import gabapi

username = os.environ['GAB_USER']
password = os.environ['GAB_PW']

api = gabapi.GabAPI(username, password)
api.login()

r = api.post_comment('TTT','img.png')
print(r)
