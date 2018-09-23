import sys
import mindsapi

api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()

id = sys.argv[3]

j = api.post_page_view("/newsfeed/"+ id)
print(j)

j = api.post_activity(id)
print(j)
