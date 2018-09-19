#!/usr/bin/env python3
from mindsapi import mindsapi
import os
import json
import sys

def read_stdin():
    return '\n'.join(sys.stdin.readlines())

username = os.environ['MINDS_USER']
password = os.environ['MINDS_PW']

api = mindsapi.MindsAPI(username, password)
api.login()

body = read_stdin()
id = sys.argv[1]
r = api.update_blog(id, body)
print(json.dumps(r.json(),indent=4))
