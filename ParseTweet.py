import json,os
import pandas as pd
from datetime import datetime,timedelta

def text_quarter_cik(tweet):
    item = json.load(tweet)
    text = item['text'] 
    d = datetime.strptime(item['datetime'], "%Y-%m-%d %H:%M:%S")
    quarter = (d.month-1)//3 + 1
    year = d.year
    t = str(year)+'q'+str(quarter)    
    return (t,text)

def get_text():
    t_list= ['2009q4']+[str(y)+'q'+str(q+1) for y in range(2010,2019) for q in range(4)]

    tweetpath = str(os.path.abspath(os.path.curdir))+'/Data/tweet/'
    data = []
    for file in os.listdir(tweetpath): 
        with open(tweetpath+file,'r') as tweet:
            data.append(text_quarter_cik(tweet))

    tweet_df = pd.DataFrame(data = {'t':t_list, 'text':' '},columns = ['t','text']).set_index('t')
    for t in t_list:
        for tweet in data:
            if tweet[0] == t:
                tweet_df.loc[t, 'text'] += tweet[1]
            else: pass
    return tweet_df