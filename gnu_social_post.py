import requests
import os
import sys
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

class GnuApi:
    def __init__(self, user, pw):
        self._base_url = 'https://freezepeach.xyz'
        self._client = requests.session()
        self._client.auth = HTTPBasicAuth(user, pw)

    def post_status(self, status):
        return self._client.post(
            self._base_url+'/api/qvitter/statuses/update.json',
            params={"status": status})

    def upload_image(self, path):
        return self._client.post(
            self._base_url+'/api/statusnet/media/upload',
            files={'media': ('media', open(path, 'rb'), 'image/png')})

    def post_image(self, path):
        r = self.upload_image(path).content.decode('utf8')
        xml = ET.fromstring(r)
        url = xml.findall('mediaurl')[0].text
        return self.post_status(url)

if len(sys.argv) > 3:
    user = sys.argv[1]
    pw = sys.argv[2]
    status = sys.argv[3]
else:
    user = os.environ['GNU_USER']
    pw = os.environ['GNU_PW']
    status = '\n'.join(sys.stdin.readlines())

api = GnuApi(user, pw)
api.post_status(status)

#r = api.post_image('img.png')
#print(r.content)
