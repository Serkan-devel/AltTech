#!/usr/bin/env python3
import os
import sys
from mindsapi import mindsapi
from datetime import *
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import offline

api = mindsapi.MindsAPI(os.environ['MINDS_USER'], os.environ['MINDS_PW'])
api.login()

id = '874947004973719557'
id = '708987537296728073'
posts = api.get_personal_feed(id, limit=100)

table = '{:<20}, {:<20}, {:>10}'
data = []
for p in posts:
    created = str(datetime.fromtimestamp(int(p['time_created'])))
    print(table.format(created, p['guid'], p['impressions']))
    data.append((created, p['impressions']))

data = [go.Scatter(x=[d[0] for d in data], y=[d[1] for d in data])]
fig = go.Figure(data=data)
offline.plot(fig, filename="minds.html")
