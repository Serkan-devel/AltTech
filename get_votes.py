#!/usr/bin/env python3
import os
import sys
from mindsapi import mindsapi

api = mindsapi.MindsAPI(os.environ['MINDS_USER'], os.environ['MINDS_PW'])
api.login()

if len(sys.argv) != 2:
    print('USAGE: minds_show_votes [POST ID]')
    quit()

post = api.get_post(sys.argv[1]).json()['activity']

for uid in post['thumbs:up:user_guids']:
    print(api.get_username_from_id(uid))
