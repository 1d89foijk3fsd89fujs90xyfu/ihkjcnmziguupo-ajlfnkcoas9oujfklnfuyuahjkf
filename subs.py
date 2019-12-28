import requests
import json

lol = []

def canal():
    channel_id = "UCJnYvI7s9PwirJSU0okv8JA";
    api_key = os.environ["API_KEY"]
    lol = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}")
    d = json.loads(lol)
    oi = d["items"]["subscriberCount"]
    re = lol.append(oi)
    return oi
