import sys
import requests
import json

class MindsAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        loginUrl = 'https://www.minds.com/api/v1/authenticate'
        self.client = requests.session()
        self.client.get(loginUrl)
        headers = {
            'cookie': 'loggedin=1; minds='+ self.client.cookies['minds'] +'; XSRF-TOKEN='+ self.client.cookies['XSRF-TOKEN'],
            'x-xsrf-token': self.client.cookies['XSRF-TOKEN']
        }
        loginData = {
            'username' : self.username,
            'password' : self.password,
            'x-xsrf-token' : self.client.cookies['XSRF-TOKEN']
        }
        r = self.client.post(loginUrl, data = loginData, headers = headers)
        #print(r.content)

        self.headers = {
            'cookie': 'loggedin=1; minds='+ self.client.cookies['minds'] +'; XSRF-TOKEN='+ self.client.cookies['XSRF-TOKEN'],
            'x-xsrf-token': self.client.cookies['XSRF-TOKEN']
        }

    def GetNotifications(self):
        r = self.client.get('https://www.minds.com/api/v1/notifications/all', headers = self.headers)
        return json.loads(r.content)

    def GetChannel(self, channelName):
        r = self.client.get('https://www.minds.com/api/v1/channel/'+ channelName, headers = self.headers)
        return json.loads(r.content)

def JsonPrint(js):
    print(json.dumps(js, indent=4, sort_keys=True))

minds = MindsAPI('zippypippytippy','Obama08*')
minds.login()

#j = minds.GetNotifications()
#JsonPrint(j)

j = minds.GetChannel('UndeadMockingbird')
print('View count:', j['channel']['impressions'])
print('Subscribers:', j['channel']['subscribers_count'])
