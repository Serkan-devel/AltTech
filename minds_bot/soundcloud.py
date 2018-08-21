import requests
import urllib

def soundcloud(api, cmd):
    sc_api  = 'https://api-v2.soundcloud.com/search/tracks?'
    sc_api += 'client_id=tt7zncXYsXxrz4a2z7gZRo7STNHGWGc5&q='
    sc_api += urllib.parse.quote(cmd['params'])
    track = requests.get(sc_api).json()['collection'][0]

    if track['artwork_url'] == None:
        thumb = track['user']['avatar_url'].encode('utf8')
    else:
        thumb = track['artwork_url'].encode('utf8')

    title = track['title'].encode('utf8')
    url = track['permalink_url'].encode('utf8')

    api.post_comment(cmd['id'], "@"+ cmd['from'] +" Here is the song you asked for.", thumb, title, url)
