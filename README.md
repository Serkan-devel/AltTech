# AltTech

## Usage Example

```
minds = MindsAPI('zippypippytippy','Obama08*')
minds.login()

groups = minds.get_top_groups(100)
for g in groups:
    j = minds.get_group(g['guid']).json()
    print(g['name'] +': '+ str(j['group']['members:count']))

channels = minds.get_top_channels(100)
for c in channels:
    j = minds.get_channel(c['username']).json()
    subs = str(j['channel']['subscribers_count']) if 'subscribers_count' in j['channel'] else "0"
    print(c['username'] + ': ' + subs)

groups = minds.get_groups(3)
for g in groups:
    j = minds.get_group(g['guid']).json()
    print(g['name'] +': '+ str(j['group']['members:count']))

j = minds.get_channel('UndeadMockingbird').json()
print('View count:', j['channel']['impressions'])
print('Subscribers:', j['channel']['subscribers_count'])

j = minds.post_with_preview('https://www.youtube.com/watch?v=K9O9yBxrzwM', 'TEST').json()
print('https://www.minds.com/newsfeed/'+ j['guid'] +'\n')

j = minds.post_custom(
    'https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file',
    'MESSAGE',
    'DESCRIPTION',
    'TITLE',
    'https://www.noao.edu/image_gallery/images/d4/J1337-29_crop1-1000.jpg').json()
print('https://www.minds.com/newsfeed/'+ j['guid'] +'\n')
```

## Installing Minds API Package

Be sure to install the Python module for the Minds API first. Go to the mindsapi directory and run:

```
python setup.py build
python setup.py install --username
```

There might be other dependencies you will have to install, preferably using "pip", such as numpy and oct2py for the calculation function.

## Useful Utility Method

```
def json_print(js):
    print(json.dumps(js, indent=4, sort_keys=True))
```
