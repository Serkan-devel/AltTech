import glob
import os
import re
import subprocess
import traceback

def run(command):
    FNULL = open(os.devnull, 'w')
    process = subprocess.Popen(command, stderr=FNULL, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out

def formula(api, cmd):
    formula = cmd['params']
    formula = "\n".join([r'\resizebox{\hsize}{!}{$' + ll.rstrip() + r'$}\\' for ll in formula.splitlines() if ll.strip()])
    tex = r'''\documentclass[preview]{standalone}
        \usepackage{graphicx}
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage[vcentering]{geometry}
        \geometry{papersize={2000px,1000px},showcrop}
        \begin{document}
        \begin{align*}'''
    tex += formula
    tex += r'''
        \end{align*}
        \end{document}'''

    tex_file = open("input.tex", "w")
    tex_file.write(tex)
    tex_file.close()

    reply = "@"+ cmd['from'] +" I'm Mr. Meeseeks! Look at me!"

    try:
        file = "formula.png"
        run("pdflatex -halt-on-error input.tex")
        run("convert -bordercolor white -border 15x15 input.pdf "+ file)

        j = api.upload_media(open(file, 'rb'), 'image/png').json()
        api.post_comment(cmd['id'], reply, attachment=j['guid'])
    except:
        print(traceback.format_exc())
        api.post_comment(cmd['id'], reply)
    finally:
        for filename in os.listdir('.'):
            if re.search(r'\.png$', filename, re.IGNORECASE):
                os.remove(filename)
            if re.search(r'\.pdf$', filename, re.IGNORECASE):
                os.remove(filename)
