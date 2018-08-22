import subprocess
import os

def run(command):
    FNULL = open(os.devnull, 'w')
    process = subprocess.Popen(command, stderr=FNULL, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out

def fortune(api, cmd):
    f = run("fortune")
    f = f.decode('utf8', 'ignore')
    f = f.replace('"', '\"')
    response = "@" + cmd['from'] + " " + f
    api.post_comment(cmd['id'], response)
