import requests
import json
import math
from googleapiclient.discovery import build

# Arguments that need to passed to the build function
# Replace with your own Developer Key
DEVELOPER_KEY = open('D:\GitHub\YouTube_Developer_Key.txt').read()
api_service_name = "youtube"
api_version = "v3"
user_id = 'UCgeAeUW_cb_avda0sBMUTmQ'

def fetch_video_urls(user_id):
    playlistId ='UU'+user_id[2:] # only used if the codeblock is used.

    ## CURRENTLY ONLY LOADING THE LAST 5 VIDEOS ##
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&order=date&maxResults=50&channelId={user_id}&quotaUser={user_id}&key={DEVELOPER_KEY}'
    json_url = requests.get(url)
    res = json.loads(json_url.text)
    print(res)
    video_urls = []
    for video in range(len(res['items'])):
        video_urls.append(res['items'][video]['id']['videoId'])

    return video_urls
''' USE THIS CODE BLOCK IF YOU WANT TO USE ALL VIDEO URLS INSTEAD

    youtube = build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
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

'''
    



def calc_score(video_urls):
    score = 0
    counter = 1.0
    for video_url in video_urls:

        # get views, likes, date published
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_url}&key={DEVELOPER_KEY}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            viewCount = int(data['items'][0]['statistics']['viewCount'])*1.0

            likeability = int(data['items'][0]['statistics']['likeCount'])/(int(data['items'][0]
                                                                                ['statistics']['likeCount'])+int(data['items'][0]['statistics']['dislikeCount']))

            score += ((likeability*math.log(viewCount))**2) * (len(video_urls)-counter)/len(video_urls)  # float
            counter += 1

        except:
            score += 0
            counter += 1

    print(score)
    return score

def write_to_csv(user_id, score):
    import pandas as pd 

    df = pd.read_csv('db.csv')

    
    uploadid = 'UU'+user_id[2:]
    
    df.loc[df.index.max() + 1, :] = [user_id, uploadid,score]

    df.to_csv('db.csv',index=False)




# video_urls = fetch_video_urls(user_id)
write_to_csv(user_id,10000)
