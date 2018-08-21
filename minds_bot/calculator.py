from oct2py import octave

def calc(api, cmd):
    result = octave.eval(cmd['params'])
    reply = 'Beep boop ... ' + cmd['params'] + ' = ' + str(result)
    api.post_comment(cmd['id'], reply)
