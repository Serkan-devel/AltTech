#!/usr/bin/env python

import sys
import json
import math
import pickle
from mindsapi import mindsapi
from datetime import datetime
from igraph import *

def jp(s):
    print (json.dumps(s, indent=4, sort_keys=True))

def to_date(i):
    return datetime.fromtimestamp(int(i)).strftime('%Y-%m-%d %H:%M')

def token_to_int(token):
    return int(int(token) / 1000000000000000000)

def id_to_user(id):
    if id not in ID2INFO: return None
    return ID2INFO[id]['username']

def load_state(file):
    state = { 'id2info': {}, 'likes': {} }
    try: state = pickle.load(open(file, "rb"))
    except: print('No save state.')
    return state

def save_state(file, seen):
    pickle.dump(seen, open(file, "wb"))

def print_channel(channel):
    table = "{:>4} {:>4} {:>8} {:>8} {:>8} {:>8} {:>4} {:>30}"
    print(table.format(
        to_date(channel['time_created']),
        channel['verified'],
        token_to_int(channel['tokens']),
        channel['tokens_count'],
        channel['subscribers_count'],
        channel['subscriptions_count'],
        channel['language'],
        channel['username']))

def label(id):
    return id_to_user(id) + " ("+ str(token_to_int(ID2INFO[id]['tokens'])) +")"

def color(id):
    return {0: "white", 1: "blue"}[ID2INFO[id]['verified']]

def plot_likes():
    g = Graph(directed=True)
    edges = [(x, y) for x in LIKES for y in LIKES[x] if x in ID2INFO and y in ID2INFO][:]
    ids = [i for i in set([x for (x,y) in edges] + [y for (x,y) in edges])]
    g.add_vertices(ids)
    g.add_edges(edges)
    g.vs["color"] = [color(id) for id in ids]
    g.vs["label"] = [label(id) for id in ids]

    area = math.sqrt(len(g.vs)) * 64
    visual_style = {
        "margin": (100,100,100,100),
        "edge_width": 0.2,
        "bbox": (area,area),
        "edge_arrow_size": 0.5,
        "edge_color": "grey",
        "vertex_label_color": "red",
        "vertex_size": 5,
        "vertex_label_dist": 1,
        "vertex_label_size": 8,
        "layout": g.layout_fruchterman_reingold(repulserad=(len(g.vs)/3)**3)
    }
    file = str(datetime.now()) +'_minds.svg'
    print('Plotting graph to file: '+ file)
    plot(g, file, **visual_style)
    print('Plotted graph with nodes: '+ str(len(g.vs)))

def print_dates():
    table = "{:>4}, {:>2}, {:>30}"
    print(table.format('time', 'verified', 'username'))
    for id in STATE['user_mapping']:
        print(table.format(
            to_date(ID2INFO[id]['time_created']),
            ID2INFO[id]['verified'],
            ID2INFO[id]['username']))

def print_stats():
    table = "{:>14}, {:>14}, {:>14}, {:>14}, {:>30}, {:>14}"
    print(table.format('tokens', 'wires', 'subscribers', 'subscriptions', 'username', 'verified'))
    for id in ID2INFO:
        print(table.format(
            token_to_int(ID2INFO[id]['tokens']),
            ID2INFO[id]['tokens_count'],
            ID2INFO[id]['subscribers_count'],
            ID2INFO[id]['subscriptions_count'],
            ID2INFO[id]['username'],
            ID2INFO[id]['verified']))

def add_vote(id, on):
    if id not in LIKES:
        LIKES[id] = set()
    LIKES[id].add(on)

def add_info(id, values):
    global ID2INFO
    if id not in ID2INFO:
        ID2INFO[id] = dict()
    ID2INFO[id] = { **ID2INFO[id], **values }

SEED_FILE = 'seed_posts.txt'
STATE_FILE = 'user_graph.sav'
STATE = load_state(STATE_FILE)
ID2INFO = STATE['id2info']
LIKES = STATE['likes']
SEEDS = open(SEED_FILE, 'r')

if len(sys.argv) == 2:
    if sys.argv[1] == 'graph': plot_likes()
    if sys.argv[1] == 'dates': print_dates()
    if sys.argv[1] == 'stats': print_stats()
    quit()

api = mindsapi.MindsAPI(sys.argv[1], sys.argv[2])
api.login()

try:
    for post_id in SEEDS:
        rsp = api.get_post(post_id.strip()).json()
        if 'activity' not in rsp: continue
        post = rsp['activity']
        oid = post['owner_guid']

        # Collect info on owner of the post.
        if oid not in ID2INFO:
            owner_name = post['ownerObj']['username']
            wires = api.get_wires(oid).json()
            info = api.get_channel_info(owner_name).json()
            add_info(oid, wires)
            add_info(oid, info['channel'])

        # Collect info on users having voted on post.
        for uid in post['thumbs:up:user_guids']:
            add_vote(uid, oid)
            if uid in ID2INFO: continue

            name = api.get_username_from_id(uid)
            if name == None: continue
            info = api.get_channel_info(name).json()
            if 'channel' not in info: continue
            wires = api.get_wires(uid).json()

            add_info(uid, info['channel'])
            add_info(uid, wires)
            print_channel(ID2INFO[uid])
except KeyboardInterrupt:
    print('Received request to quit.')
finally:
    save_state(STATE_FILE, STATE)
    print('State saved.')
