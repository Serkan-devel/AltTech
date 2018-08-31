import json
import os
import requests
import subprocess
import urllib
import random

def run(command):
    FNULL = open(os.devnull, 'w')
    process = subprocess.Popen(command, stderr=FNULL, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out

def get_gif(api, cmd):
    giphyKey = "LL0WcNfyviD3fsQR40CQpw2IgDBEzOUP"
    giphy_api  = 'https://api.giphy.com/v1/gifs/search?api_key=' + giphyKey
    giphy_api += '&limit=20&rating=R&q='+ urllib.parse.quote(cmd['params'])
    j = requests.get(giphy_api).json()

    choice = random.choice(j['data'])
    url = choice['images']['original']['url']
    id = choice['id']
    file = id + ".gif"
    run("wget "+ url +" -O "+ file)

    j = api.upload_media(open(file, 'rb'), 'image/gif').json()
    api.post_comment(cmd['id'], comment='@'+ cmd['from'], attachment=j['guid'])

    os.remove(file)
