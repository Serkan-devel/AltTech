import requests
import json
from datetime import datetime

class MindsAPI:
    default_post = {
        "wire_threshold": "",
        "message": "",
        "is_rich": 1,
        "title": "",
        "description": "",
        "thumbnail": "",
        "url": "",
        "attachment_guid": "",
        "mature": 0,
        "access_id": 2
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        login_url = 'https://www.minds.com/api/v1/authenticate'
        self.client = requests.session()
        self.client.get(login_url)
        c = self.client.cookies
        headers = {
            'cookie': 'loggedin=1; minds='+ c['minds'] +'; XSRF-TOKEN='+ c['XSRF-TOKEN'],
            'x-xsrf-token': c['XSRF-TOKEN']
        }
        login_data = {
            'username' : self.username,
            'password' : self.password,
            'x-xsrf-token' : c['XSRF-TOKEN']
        }
        r = self.client.post(login_url, data = login_data, headers = headers)
        c = self.client.cookies
        self.client.headers = {
            'cookie': 'loggedin=1; minds='+ c['minds'] +'; XSRF-TOKEN='+ c['XSRF-TOKEN'],
            'x-xsrf-token': c['XSRF-TOKEN']
        }

    def get_notifications(self):
        return self.client.get('https://www.minds.com/api/v1/notifications/all')

    def get_channel(self, name):
        return self.client.get('https://www.minds.com/api/v1/channel/'+ name)

    def get_preview(self, url):
        return self.client.get('https://www.minds.com/api/v1/newsfeed/preview?url='+ url)

    def get_post(self, id):
        return self.client.get('https://www.minds.com/api/v1/newsfeed/single/'+ id)

    def post(self, data):
        return self.client.post('https://www.minds.com/api/v1/newsfeed', data = data)

    def post_with_preview(self, url, message):
        j = self.get_preview(url).json()

        data = MindsAPI.default_post
        data['url'] = url
        data['message'] = message
        data['description'] = j['meta']['description'] if 'description' in j['meta'] else ""
        data['title'] = j['meta']['title'] if 'title' in j['meta'] else ""
        data['thumbnail'] = j['links']['thumbnail'][0]['href'] if 'thumbnail' in j['links'] else ""

        return self.post(data)

    def post_custom(self, url, message, description, title, thumbnail):
        data = MindsAPI.DefaultPost
        data['url'] = url
        data['message'] = message
        data['description'] = description
        data['title'] = title
        data['thumbnail'] = thumbnail

        return self.post(data)

    def get_group(self, id):
        return self.client.get('https://www.minds.com/api/v1/groups/group/'+ id)

    def get_channel(self, name):
        return self.client.get('https://www.minds.com/api/v1/channel/'+ name)

    def get_continuation(self, url, limit):
        groups = list()
        x = 0
        cont = ""

        while x < limit:
            r = self.client.get(url + cont)
            j = r.json()

            if 'load-next' not in j: break

            cont = j['load-next']
            x += len(j['entities'])
            groups.extend(j['entities'])

        return groups

    def get_top_groups(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/entities/trending/groups?offset=',
            limit)

    def get_top_channels(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/entities/trending/channels?offset=',
            limit)

def json_print(js):
    print(json.dumps(js, indent=4, sort_keys=True))

minds = MindsAPI('zippypippytippy','Obama08*')
minds.login()

j = minds.get_post('876578164342235136').json()
json_print(j['activity']['impressions'])