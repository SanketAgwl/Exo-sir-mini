import pandas as pd
from datetime import datetime as dt , timedelta as td
from datetime import time as t
# avg_time = td(days=0, hours=12, minutes=0,seconds=0) # average time
# print(avg_time)
filename = pd.read_csv('scraped_tweets.csv')
df = pd.DataFrame(filename, columns=['difference'])
diff_in_sec = []
for i in df.index:
   # print(df.loc[i].difference)
   #print(type(df.loc[i].difference))
   #print(type(pd.to_timedelta(df.loc[i].difference)))
   temp=pd.to_timedelta(df.loc[i].difference)
   temp2=temp.total_seconds();
   diff_in_sec.append(temp2);
   #squared_error.append(pd.to_timedelta(df.loc[i].difference)-avg_time).total_seconds()*(pd.to_timedelta(df.loc[i].difference)-avg_time).total_seconds()
filename['Diff in seconds']=diff_in_sec
print(diff_in_sec)

filename.to_csv('scraped_tweets.csv',index=False)
# print(df)
# print(len(df.index))

#calculate standard mean from error
df2=pd.DataFrame(filename,columns=['Diff in seconds'])
standard_mean_error=df2.sem(axis=0)
print(standard_mean_error)

