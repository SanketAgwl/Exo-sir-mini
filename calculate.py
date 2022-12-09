import pandas as pd
from datetime import datetime as dt , timedelta as td
from datetime import time as t
avg_time = td(days=0,hours=12, minutes=0,seconds=0) # average time
print(avg_time)
filename = pd.read_csv('scraped_tweets.csv')
df=pd.DataFrame(filename, columns=['difference'])
squared_error = []
l=len(df.index)
for i in df.index:
   # print(df.loc[i].difference)
   #print(type(df.loc[i].difference))
   #print(type(pd.to_timedelta(df.loc[i].difference)))
   temp=pd.to_timedelta(df.loc[i].difference)-avg_time
   temp2=temp.total_seconds();
   squared_error.append(temp2*temp2);
   #squared_error.append(pd.to_timedelta(df.loc[i].difference)-avg_time).total_seconds()*(pd.to_timedelta(df.loc[i].difference)-avg_time).total_seconds()
filename['Squared_error']=squared_error
print(squared_error)

filename.to_csv('scraped_tweets.csv',index=False)
# print(df)
# print(len(df.index))

