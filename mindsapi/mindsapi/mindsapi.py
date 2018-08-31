import requests

class MindsAPI:
    default_post = {
        "wire_threshold": "",
        "message": "",
        "is_rich": 1,
        "title": " ",
        "description": " ",
        "thumbnail": " ",
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

        if ('meta' in j):
            data['description'] = j['meta']['description'] if 'description' in j['meta'] else ""
            data['title'] = j['meta']['title'] if 'title' in j['meta'] else ""
            data['thumbnail'] = j['links']['thumbnail'][0]['href'] if 'thumbnail' in j['links'] else ""
        else:
            data['title'] = url

        return self.post(data)

    def post_with_attachment(self, guid, message):
        data = MindsAPI.default_post
        data['attachment_guid'] = guid
        data['message'] = message
        return self.post(data)

    def post_custom(self, url='', message='', description='', title='', thumbnail=''):
        data = MindsAPI.default_post
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

    def get_continuation(self, url, limit, array):
        groups = list()
        x = 0
        cont = ""
        while x < limit:
            r = self.client.get(url + cont)
            try:
                j = r.json()
            except:
                return groups
            if 'load-next' not in j: break

            cont = j['load-next']
            x += len(j[array])
            groups.extend(j[array])
        return groups

    def get_top_groups(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/entities/trending/groups?offset=', limit, 'entities')

    def get_top_channels(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/entities/trending/channels?offset=', limit, 'entities')

    def get_top_posts(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/newsfeed/top?offset=', limit, 'activity')

    def upload_media(self, image, type):
        files = { 'file': ('file', image, type) }
        return self.client.post('https://www.minds.com/api/v1/media', files = files)

    def post_image(self, message, filename):
        j = self.upload_media(open(filename, 'rb'), 'image/png').json()
        return self.post_with_attachment(j['guid'], message)

    def post_video(self, message, filename):
        j = self.upload_media(open(filename, 'rb'), 'video/mp4').json()
        return self.post_with_attachment(j['guid'], message)

    def post_page_view(self, url):
        data = {
            "url": "/newsfeed/878320253628096512",
            "referrer": ""}
        return self.client.post(
            'https://www.minds.com/api/v2/analytics/pageview',
            data = data).json();

    def post_activity(self, id):
        url = 'https://www.minds.com/api/v2/analytics/views/activity/'+ id
        return self.client.post(url).json()

    def remind(self, id, message):
        data = {
            "message": message
        }
        return self.client.post(
            'https://www.minds.com/api/v2/newsfeed/remind/'+ id,
            data = data
        ).json()

    def vote_up(self, id):
        return self.client.put('https://www.minds.com/api/v1/thumbs/'+ id +'/up').json()

    def delete_post(self, id):
        return self.client.delete('https://www.minds.com/api/v1/newsfeed/'+ id).json()

    def get_notifications(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/notifications/all?limit='+str(limit)+'?offset=',
            limit,
            'notifications')

    def get_tags(self, limit):
        return self.get_continuation(
            'https://www.minds.com/api/v1/notifications/tags?limit='+str(limit)+'?offset=',
            limit,
            'notifications')

    def post_comment(self, id, comment="", thumbnail="", title="", url="", attachment=""):
        data  = {
            "is_rich": 0,
            "title": title,
            "description": "",
            "thumbnail": thumbnail,
            "url": url,
            "attachment_guid": attachment,
            "mature": 0,
            "access_id": 2,
            "comment": comment}
        return self.client.post('https://www.minds.com/api/v1/comments/'+ id, data=data)

    def get_creation_time(self, username):
        r = self.client.get('https://www.minds.com/api/v1/channel/'+ username + '?').json()
        if 'channel' not in r:
            return None
        return r['channel']['time_created']

    def get_channel_info(self, username):
        return self.client.get('https://www.minds.com/api/v1/channel/'+ username + '?')

    def get_username_from_id(self, id):
        r = self.client.get('https://www.minds.com/api/v1/wire/rewards/'+ id + '?limit=1').json()
        return r['username']
        #return r['username']

    def get_wires(self, id):
        return self.client.get('https://www.minds.com/api/v1/wire/sums/overview/'+ id +'?merchant=0')
