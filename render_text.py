#!/usr/bin/env python3
import os
import sys
import subprocess
import random
from os import listdir
from os.path import isfile, join
from mindsapi import mindsapi
from gabapi import gabapi

BACKGROUNDS = 'backgrounds'
FONTS = 'fonts'
IMG_URL = None
if len(sys.argv) > 1:
    IMG_URL = sys.argv[1]

def run(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return result.stdout.readline().decode('utf8')

def get_post_text():
    text = ""
    for line in sys.stdin:
        if (line == ".\n"): break
        text += line
    text = text.strip()
    text = text.replace("\t", r"    ")
    text = text.replace("\"", r"\"")
    return text

def download_image(url, file):
    run("wget --quiet {} -O {}".format(url, file))

def get_image_size(file):
    return run('identify -format "%wx%h" {}'.format(file))

def render_text(file, text, out, font):
    size = get_image_size(file)
    width = str(int(size.split('x')[0]) * 0.9)
    height = str(int(size.split('x')[1]) * 0.9)
    run("convert {} -set option:modulate:colorspace hsb -modulate 50,120 -size {} -fill white -gravity center -background transparent -font {} label:\"{}\" -composite {}".format(file, width+"x"+height, font, text, out))

text = get_post_text()
out = "image_text.jpg"

if IMG_URL == None:
    images = [f for f in listdir(BACKGROUNDS) if isfile(join(BACKGROUNDS, f))]
    file = BACKGROUNDS +'/'+ random.choice(images)
else:
    file = "img.jpg"
    download_image(IMG_URL, file)

fonts = [f for f in listdir(FONTS) if isfile(join(FONTS, f))]
font = FONTS +'/'+ random.choice(fonts)

print(file)
print(font)

render_text(file, text, out, font)

username = os.environ['MINDS_USER']
password = os.environ['MINDS_PW']

api = mindsapi.MindsAPI(username, password)
api.login()
api.post_image('', out)

username = os.environ['GAB_USER']
password = os.environ['GAB_PW']

api = gabapi.GabAPI(username, password)
api.login()
api.post_comment('', out)