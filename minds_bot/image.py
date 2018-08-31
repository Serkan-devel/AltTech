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
    run("magick convert -border 15x15 -background black -fill white -font Impact -gravity Center -size 1600x800 caption:'"+ cmd['params'].replace("'", '’') +"' " + file)

    j = api.upload_media(open(file, 'rb'), 'image/png').json()
    api.post_comment(cmd['id'], comment='@'+ cmd['from'], attachment=j['guid'])

    os.remove(file)
