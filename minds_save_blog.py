#!/usr/bin/env python3
from mindsapi import mindsapi
import os
import sys

api = mindsapi.MindsAPI(
    os.environ['MINDS_USER'],
    os.environ['MINDS_PW'])
api.login()
r = api.get_blog(sys.argv[1])
print(r.json()['blog']['description'])
