# AltTech

## Examples

```def JsonPrint(js):
    print(json.dumps(js, indent=4, sort_keys=True))

minds = MindsAPI('zippypippytippy','Obama08*')
minds.login()

j = minds.GetChannel('UndeadMockingbird').json()
print('View count:', j['channel']['impressions'])
print('Subscribers:', j['channel']['subscribers_count'])

j = minds.PostUrl('https://www.youtube.com/watch?v=K9O9yBxrzwM', 'TEST').json()
print('https://www.minds.com/newsfeed/'+ j['guid'] +'\n')

j = minds.PostCustom(
    'https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file',
    'MESSAGE',
    'DESCRIPTION',
    'TITLE',
    'https://www.noao.edu/image_gallery/images/d4/J1337-29_crop1-1000.jpg').json()
print('https://www.minds.com/newsfeed/'+ j['guid'] +'\n')
```
