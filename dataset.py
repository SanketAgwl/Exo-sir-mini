import tweepy
import random
import pandas as pd
api_key = "eaLFxqln7SellQfGri9cccKla"
api_key_secret = "3p0BmQMeoDtbfEqvrcKEvDhiACHYi865Z17y7aVprVssjqOBCE"

access_token = "1578359033920032768-gKXvw97loCpJBz5lfz1lDKlcbUOJAK"
access_token_secret = "9CJ8MiX4i4LlwRgwrDMKbBZlXVhANSHGJ35dAdB13R3L2"
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.wait_on_rate_limit= True
api.wait_on_rate_limit_notify= True
india_woeid=23424848
trend_result=api.get_place_trends(india_woeid)
query = []
try:
    for trend in trend_result[0]["trends"]:
        query.append(trend["name"])
except:
    print("Errorrrrrrrrrrrr")
usernameList=[]
for q in query:
    tweets = tweepy.Cursor(api.search_tweets,q, lang="en").items(50)
    list_tweets = [tweet for tweet in tweets]
    for tweet in list_tweets:
        usernameList.append(tweet.user.screen_name)

usernameList = [*set(usernameList)]

print(usernameList)
print(len(usernameList))


db = pd.DataFrame(columns=['username',
                           'hashtag',
                           'first tweet',
                           'last tweet',
                           'difference'])



for i in usernameList:
    userID =i
    tweets = api.user_timeline(screen_name=userID,
                               # 200 is the maximum allowed count
                               count=50,
                               include_rts=False, )
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1
    ret= {}
    # we will iterate over each tweet in the
    # list for extracting information about each tweet

    for tweet in list_tweets:
        # print(tweet.entities['hashtags'])
        for l in tweet.entities['hashtags']:
            word = l['text']
            if word in ret:
                ret[word] += [tweet]
            else:
                ret[word] = []
            # print(word)

    if len(ret) == 0:
        continue

    sum = 0

    for hashtweets in ret.items():
        c = hashtweets[1]
        if len(c) > 0:
            a = hashtweets[1][0]
            b = hashtweets[1][-1]
            # print(a.created_at)
            diff = a.created_at - b.created_at
            hashtext = hashtweets[0]

            # Here we are appending all the
            # extracted information in the DataFrame
            ith_tweet = [ userID, hashtext, a.created_at, b.created_at, diff]
            print(ith_tweet)
            db.loc[len(db)] = ith_tweet

        # Function call to print tweet data on screen
    filename = 'scraped_tweets.csv'
    df= db.drop_duplicates
    # we will save our database as a CSV file.
    db.to_csv(filename)
