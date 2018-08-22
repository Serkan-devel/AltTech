import json
from mindsapi import mindsapi
import pickle
import re
import sys
import time
import traceback

# Import command implementations.
from calculator import calc
from fortune import fortune
from soundcloud import soundcloud
from giphy import get_gif
from image import get_image

# Global configurations.
STATE_FILE = 'bot_memory.sav'
POLLING_INTERVAL = 1
USER_NAME = sys.argv[1]
PASSWORD = sys.argv[2]

print("Minds bot by Undead Mockingbird.\n")

def json_print(js):
    print(json.dumps(js, indent=4, sort_keys=True))

def parse_notification(tag):
    if tag['entity']['type'] == "comment":
        msg = tag['entity']['description']
        id = str(tag['entity']['entity_guid'])
    else:
        msg = tag['entity']['message']
        id = str(tag['entity']['guid'])

    from_user = tag['from']['username']
    match = re.search('@'+ USER_NAME +'\s+([^:]*):(.*)', msg, re.IGNORECASE)

    if match == None:
        verb = 'default'
        params = None
    else:
        verb = match.group(1).lower()
        params = match.group(2)

    return {
        'id': id,
        'from': from_user,
        'verb': verb,
        'params': params }

def help(api, cmd):
    reply  = 'I am a bot that belongs to @UndeadMockingbird.\n\n'
    reply += 'Available commands:\n'
    reply += str(list(commands.keys())[1:])
    api.post_comment(cmd['id'], reply)

def load_state(file):
    seen = set()
    try:
        seen = pickle.load(open(file, "rb"))
    except:
        print('No save state.')
    return seen

def save_state(file, seen):
    seen.add(tag['guid'])
    pickle.dump(seen, open(file, "wb"))
    return seen

commands = {
    # Keep default in the first spot, as the help output will skip it.
    'default': fortune,
    'calc': calc,
    'fortune': fortune,
    'gif': get_gif,
    'help': help,
    'image': get_image,
    'soundcloud': soundcloud
}

print('Logging into Minds ...')
api = mindsapi.MindsAPI(USER_NAME, PASSWORD)
api.login()

seen = load_state(STATE_FILE)
print('Loaded save state:', len(seen))

print('Starting to poll for tags ...')
while True:
    try:
        for tag in api.get_tags(10):
            if tag['guid'] in seen: continue
            print('Found a new tag.')

            try:
                cmd = parse_notification(tag)
                print('Command received:', cmd)

                if cmd['from'] == USER_NAME:
                    print('Skipping tag from myself.')
                    continue;

                if cmd['verb'] in commands:
                    commands[cmd['verb']](api, cmd)
                else:
                    commands['default'](api, cmd)

                print('Done processing command.')
            except:
                print(traceback.format_exc())
                api.post_comment(cmd['id'], 'I am here.')
            finally:
                seen.add(tag['guid'])
                save_state(STATE_FILE, seen)

        time.sleep(POLLING_INTERVAL)
    except KeyboardInterrupt:
        print('Received request to quit.')
        break;
    except:
        print(traceback.format_exc())
