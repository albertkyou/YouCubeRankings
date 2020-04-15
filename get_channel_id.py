import requests
import json
import math
from googleapiclient.discovery import build

# Arguments that need to passed to the build function
DEVELOPER_KEY = "AIzaSyCi3tOtYwFXEsf6XzAfXJnlALcn8axqe_k"
api_service_name = "youtube"
api_version = "v3"


def get_channel_id(channel_name):
    url = f'https://www.googleapis.com/youtube/v3/channels?key={DEVELOPER_KEY}&forUsername={channel_name}&part=id'

    json_url = requests.get(url)
    data = json.loads(json_url.text)

    try:
        user_id = data['items'][0]['id']
        upload_id = 'UU'+user_id[2:]

    except KeyError:
        user_id = None
        upload_id = None

    return upload_id, user_id  # same as uploads playlist id


print(get_channel_id('cyotheking'))