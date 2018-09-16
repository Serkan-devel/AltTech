import sys
import mindsapi

# USAGE:
# post_image.py [USERNAME] [PASSWORD] [PATH TO VIDEO]
api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()
print(api.post_video('', sys.argv[3]))
