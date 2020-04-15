import calc_score as csp 
import dbfunctions as dbfn 
import get_channel_id as gci 

def get_stats(user_id):
    video_urls = csp.fetch_video_urls(user_id)
    score = csp.calc_score(video_urls)

    dbfn.write_to_csv(user_id, score)
    print('Done')
    return None

get_stats('UCqTVfT9JQqhA6_Hi_h_h97Q')