import json
import os
import requests
import sys
from gabapi import gabapi

username = os.environ['GAB_USER']
password = os.environ['GAB_PW']

api = gabapi.GabAPI(username, password)
api.login()
r = api.get_notifications()

for n in r.json()['data']:
    if n['type'] == 'comment':
        print("{}: {}".format(n['actuser']['name'], n['post']['body']))
    else:
        print(n['message'])


#r = api.post_comment('TTT','img.png')
#print(r)
