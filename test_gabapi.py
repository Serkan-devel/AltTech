import json
import os
import requests
import sys
from gabapi import gabapi

username = os.environ['GAB_USER']
password = os.environ['GAB_PW']

api = gabapi.GabAPI(username, password)
api.login()
#api.post_comment('This is a message.','img.png')

r = api.get_notifications()
for n in r.json()['data']:
    if n['type'] == 'comment':
        print("{}: {}".format(n['actuser']['name'], n['post']['body']))
    else:
        print(n['message'])
