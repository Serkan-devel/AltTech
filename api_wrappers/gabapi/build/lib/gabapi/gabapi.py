import requests
import re
from bs4 import BeautifulSoup

class GabAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        self.client = requests.session()
        r = self.client.get('https://gab.ai/auth/login')

        soup = BeautifulSoup(r.content, 'html.parser')
        xsrf = soup.find("input",{"name":"_token"})['value']
        payload = {'username':self.username, 'password':self.password, '_token':xsrf}
        reply = self.client.post('https://gab.ai/auth/login', params=payload)
        token = re.search('"id_token": "([^\"]*)"', reply.content.decode('utf8')).group(1)

        self.client.headers = {
            'authorization': 'Bearer '+token,
            'x-xsrf-token': self.client.cookies['XSRF-TOKEN']
        }

    def post_comment(self, body='', filename=None):
        post = {
          "body": "<p>"+ body +"</p>",
          "reply_to": "",
          "is_quote": "0",
          "is_html": "1",
          "nsfw": "0",
          "is_premium": "0",
          "_method": "post",
          "media_attachments": [],
          "premium_min_tier": 0
        }
        if filename != None:
            post['media_attachments'] = [self.post_media(filename)]

        return self.client.post('https://gab.ai/posts', json=post)

    def post_media(self, filename):
        image = open(filename, 'rb')
        files = { 'file': ('file', image, 'image/png') }
        r =  self.client.post('https://gab.ai/api/media-attachments/images', files=files)
        return r.json()['id']

    def get_notifications(self):
        params = {
            "type": "null",
            "all_types": "1",
            "includes": "post.conversation_parent"
        }
        return self.client.get('https://gab.ai/api/notifications', params=params)
