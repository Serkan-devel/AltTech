#import memegen
import requests
import os
import json
import uuid

def jp(str):
    print(json.dumps(str, indent=4, sort_keys=True))

def meme(api, cmd):
    args = cmd['params'].split('|')
    meme = args[0].strip()
    text0 = text1 = ''

    # params := meme|text0|text1
    if len(args) == 2:
        text0 = args[1].strip()
        text1 = ''
    elif len(args) >= 3:
        text0 = args[1].strip()
        text1 = args[2].strip()

    print(meme, text0, text1)
    key = r'7bbd8812-8347-4ae1-87b9-29bb1c545695'
    j = requests.get('http://version1.api.memegenerator.net/Generators_Search', params={
        'q': meme,
        'apiKey': key,
        'pageSize': 25
    }).json()

    r = j['result'][0]
    # Search results are not very good. See if there is a better one, containing all terms.
    terms = meme.split(' ')
    for ir in j['result']:
        all = True
        for t in terms:
            all = all and t.lower() in ir['displayName'].lower()
        if all:
            r = ir

    gid = r['generatorID']
    iid = r['imageID']

    if text0 == '' and text1 == '':
        url = r['imageUrl']
    else:
        r = requests.get('http://version1.api.memegenerator.net/Instance_Create', params={
            'languageCode': 'en',
            'generatorID': gid,
            'imageID': iid,
            'text0': text0,
            'text1': text1,
            'apiKey': key,
        });
        url = r.json()['result']['instanceImageUrl']

    file = str(uuid.uuid4())
    r = requests.get(url)
    with open(file, 'wb') as outfile:
        outfile.write(r.content)

    reply = "@"+ cmd['from']
    j = api.upload_media(open(file, 'rb'), 'image/jpg').json()
    api.post_comment(cmd['id'], reply, attachment=j['guid'])

    os.remove(file)
