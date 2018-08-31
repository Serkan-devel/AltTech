import glob
import os
import re

from oct2py import octave

rs = ""
def stream_handler(line):
    global rs
    rs += line + "\n"

def calc(api, cmd):
    global rs
    rs = ""
    plot = "plot"

    try:
        result = octave.eval(
            cmd['params'],
            stream_handler=stream_handler,
            plot_width=1200,
            plot_height=600,
            plot_dir=".",
            plot_format='PNG',
            plot_name=plot)
    except Exception as e:
        rs = str(e)

    reply = "@"+ cmd['from'] + "\n" + rs
    file = plot + '001.PNG'

    try:
        j = api.upload_media(open(file, 'rb'), 'image/png').json()
        api.post_comment(cmd['id'], reply, attachment=j['guid'])
    except:
        api.post_comment(cmd['id'], reply)

    for filename in os.listdir('.'):
        if re.search(r'\.png$', filename, re.IGNORECASE):
            os.remove(filename)
