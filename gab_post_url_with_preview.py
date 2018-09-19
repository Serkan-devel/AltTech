import json
import sys
from datetime import datetime
from gabapi import gabapi

# USAGE:
# post_image.py [USERNAME] [PASSWORD] [PATH TO IMAGE]
api = gabapi.GabAPI(sys.argv[1], sys.argv[2])
api.login()
api.post_comment(sys.argv[3])
