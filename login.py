import sys
import requests

loginUrl = 'https://www.minds.com/api/v1/authenticate'

client = requests.session()
client.get(loginUrl)

headers = {
    'cookie': 'loggedin=1; minds='+ client.cookies['minds'] +'; XSRF-TOKEN='+ client.cookies['XSRF-TOKEN'],
    'x-xsrf-token': client.cookies['XSRF-TOKEN']
}
loginData = {
    'username' : 'zippypippytippy',
    'password' : 'Obama08*',
    'x-xsrf-token' : client.cookies['XSRF-TOKEN']
}
r = client.post(loginUrl, data = loginData, headers = headers)
print(r.content)

headers = {
    'cookie': 'loggedin=1; minds='+ client.cookies['minds'] +'; XSRF-TOKEN='+ client.cookies['XSRF-TOKEN'],
    'x-xsrf-token': client.cookies['XSRF-TOKEN']
}
r = client.get('https://www.minds.com/api/v1/notifications/all', headers = headers)
print(r.content)
