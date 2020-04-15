def write_to_csv(user_id, score):
    import pandas as pd 

    df = pd.read_csv('db.csv')

    
    uploadid = 'UU'+user_id[2:]
    
    df.loc[df.index.max() + 1, :] = [user_id, uploadid,score]
    df = df.sort_values(by='score',ascending=False)
    df.to_csv('db.csv',index=False)




# video_urls = fetch_video_urls(user_id)
write_to_csv('cyoubx',11000)