import json
import os
import requests
import sys
from gabapi import gabapi

username = os.environ['GAB_USER']
password = os.environ['GAB_PW']

api = gabapi.GabAPI(username, password)
api.login()
api.post_comment('<p style="color:red">html test!</p>')
#api.post_comment('<font color="red">rrrrrr</font>','img.png')
quit()

r = api.get_notifications()
for n in r.json()['data']:
    if n['type'] == 'comment':
        print("{}: {}".format(n['actuser']['name'], n['post']['body']))
    else:
        print(n['message'])
