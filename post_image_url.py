import json
import sys
from datetime import datetime
import mindsapi

# USAGE:
# post_image.py [USERNAME] [PASSWORD] [PATH TO IMAGE]
api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()
api.post_custom(sys.argv[3], ' ', ' ', ' ', sys.argv[3])
