import json
import sys
from datetime import datetime
import mindsapi

# USAGE:
# post_image.py [USERNAME] [PASSWORD] [PATH TO IMAGE]
api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()

def json_print(js):
    print(json.dumps(js, indent=4, sort_keys=True))

posts = api.get_top_posts(35)

table = "{:>4} {:>20} {:>20} {:>7} {:>4} {:>4} {:>50}"
print(table.format('Rank', 'User', 'Time Posted', 'Views', 'Up', 'Down', 'Link'));
rank = 0
for post in posts[:35]:
    #json_print(post)
    rank += 1
    print(table.format(
        rank,
        post['ownerObj']['username'],
        datetime.fromtimestamp(int(post['time_created'])).strftime('%Y-%m-%d %H:%M:%S'),
        post['impressions'],
        post['thumbs:up:count'],
        post['thumbs:down:count'],
        'https://www.minds.com/newsfeed/'+ post['guid']))
