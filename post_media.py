import magic
import sys
import mindsapi

mime = magic.from_file(sys.argv[3], mime=True)

if mime not in ['image/png', 'video/mp4']:
    print('Unsupported file type.')

api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()

if mime == "image/png":
    print('Posting image ...')
    print(api.post_image('', sys.argv[3]))

if mime == "video/mp4":
    print('Posting video ...')
    print(api.post_video('', sys.argv[3]))
