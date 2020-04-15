def write_to_csv(user_id, score):
    import pandas as pd 

    df = pd.read_csv('db.csv')

    
    uploadid = 'UU'+user_id[2:]
    
    df.loc[df.index.max() + 1, 1:4] = [user_id, uploadid,score]
    df = df.sort_values(by='score',ascending=False)
    df.to_csv('db.csv',index=False)




# video_urls = fetch_video_urls(user_id)
# import calc_score as csp
# video_urls = csp.fetch_video_urls('UCgeAeUW_cb_avda0sBMUTmQ')
# score = csp.calc_score(video_urls)

score = 10000
write_to_csv('UCgeAeUW_cb_avda0sBMUTmQ',score)