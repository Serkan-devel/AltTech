import sys
from mindsapi import mindsapi

api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()

id = sys.argv[3]

j = api.remind(id, 'TEST')
#print(j)

rid = j['guid']
#print(rid)
j = api.vote_up(rid)
#print(j)

print(api.delete_post(rid))
