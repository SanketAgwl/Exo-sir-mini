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
    tweets = tweepy.Cursor(api.search_tweets,q, lang="en").items(10)
    list_tweets = [tweet for tweet in tweets]
    for tweet in list_tweets:
        usernameList.append(tweet.user.screen_name)
print(usernameList)
print(len(usernameList))

def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")



db = pd.DataFrame(columns=['username',
                           'description',
                           'location',
                           'following',
                           'followers',
                           'totaltweets',
                           'retweetcount',
                           'text',
                           'hashtags'])



for i in usernameList:
    userID =i
    tweets = api.user_timeline(screen_name=userID,
                               # 200 is the maximum allowed count
                               count=10,
                               include_rts=False, )
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
        # Retweets can be distinguished by
        # a retweeted_status attribute,
        # in case it is an invalid reference,
        # except block will be executed
        try:
            text = tweet.retweeted_status.text
        except AttributeError:
            text = tweet.text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [ username, description,
                     location, following,
                     followers, totaltweets,
                     retweetcount,text, hashtext]
        db.loc[len(db)] = ith_tweet

        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i + 1
    filename = 'scraped_tweets.csv'

    # we will save our database as a CSV file.
    db.to_csv(filename)

