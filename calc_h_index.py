import requests
import json
import math

from googleapiclient.discovery import build

# Arguments that need to passed to the build function
DEVELOPER_KEY = "AIzaSyCi3tOtYwFXEsf6XzAfXJnlALcn8axqe_k"
api_service_name = "youtube"
api_version = "v3"
channel_name = 'cyoubx'


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

    return upload_id, user_id # same as uploads playlist id




def fetch_video_urls(playlistId):
    youtube = build(api_service_name,api_version,developerKey=DEVELOPER_KEY)

    res = youtube.playlistItems().list(part="snippet",playlistId=playlistId,maxResults="50").execute()

    nextPageToken = res.get('nextPageToken')
    while ('nextPageToken' in res):
        nextPage = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults="50",
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']

        if 'nextPageToken' not in nextPage:
            res.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']

    video_urls = []
    for video in range(len(res['items'])):
        video_urls.append(res['items'][video]['snippet']['resourceId']['videoId'])
        
    return video_urls





def get_stats(video_urls):
    score = 0
    for video_url in video_urls:
    

        # get views, likes, date published
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_url}&key={DEVELOPER_KEY}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            viewCount = int(data['items'][0]['statistics']['viewCount'])*1.0

            likeability = int(data['items'][0]['statistics']['likeCount'])/(int(data['items'][0]['statistics']['likeCount'])+int(data['items'][0]['statistics']['dislikeCount']))

            score+=(likeability*math.log(viewCount))**2 # float

        except:
            score+=0

    print(score)
    return score


playlistId,_ = get_channel_id('cyoubx')
video_urls = fetch_video_urls(playlistId)
get_stats(video_urls)