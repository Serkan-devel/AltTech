import requests
import json

class MindsAPI:
    DefaultPost = {
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
        loginUrl = 'https://www.minds.com/api/v1/authenticate'
        self.client = requests.session()
        self.client.get(loginUrl)
        c = self.client.cookies
        headers = {
            'cookie': 'loggedin=1; minds='+ c['minds'] +'; XSRF-TOKEN='+ c['XSRF-TOKEN'],
            'x-xsrf-token': c['XSRF-TOKEN']
        }
        loginData = {
            'username' : self.username,
            'password' : self.password,
            'x-xsrf-token' : c['XSRF-TOKEN']
        }
        r = self.client.post(loginUrl, data = loginData, headers = headers)
        c = self.client.cookies
        self.client.headers = {
            'cookie': 'loggedin=1; minds='+ c['minds'] +'; XSRF-TOKEN='+ c['XSRF-TOKEN'],
            'x-xsrf-token': c['XSRF-TOKEN']
        }

    def GetNotifications(self):
        return self.client.get('https://www.minds.com/api/v1/notifications/all')

    def GetChannel(self, channelName):
        return self.client.get('https://www.minds.com/api/v1/channel/'+ channelName)

    def GetPreview(self, url):
        return self.client.get('https://www.minds.com/api/v1/newsfeed/preview?url='+ url)

    def Post(self, data):
        return self.client.post('https://www.minds.com/api/v1/newsfeed', data=data)

    def PostWithPreview(self, url, message):
        j = self.GetPreview(url).json()

        data = MindsAPI.DefaultPost
        data['url'] = url
        data['message'] = message
        data['description'] = j['meta']['description'] if 'description' in j['meta'] else ""
        data['title'] = j['meta']['title'] if 'title' in j['meta'] else ""
        data['thumbnail'] = j['links']['thumbnail'][0]['href'] if 'thumbnail' in j['links'] else ""

        return self.Post(data)

    def PostCustom(self, url, message, description, title, thumbnail):
        data = MindsAPI.DefaultPost
        data['url'] = url
        data['message'] = message
        data['description'] = description
        data['title'] = title
        data['thumbnail'] = thumbnail

        return self.Post(data)
