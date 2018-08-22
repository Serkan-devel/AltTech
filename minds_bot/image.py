import json
import os
import requests
import subprocess
import urllib

def run(command):
    FNULL = open(os.devnull, 'w')
    process = subprocess.Popen(command, stderr=FNULL, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out

def get_image(api, cmd):
    file = 'image.png'
    run("magick convert -border 10x10 -background black -fill white -font Candice -gravity Center -size 800x400 caption:'"+ cmd['params'].replace("'", '’') +"' " + file)

    j = api.upload_media(open(file, 'rb'), 'image/png').json()
    api.post_comment(cmd['id'], comment='@'+ cmd['from'] + ' Here is your image.', attachment=j['guid'])

    os.remove(file)
