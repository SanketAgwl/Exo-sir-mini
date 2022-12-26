import tweepy
import random
api_key = "eaLFxqln7SellQfGri9cccKla"
api_key_secret = "3p0BmQMeoDtbfEqvrcKEvDhiACHYi865Z17y7aVprVssjqOBCE"

access_token = "1578359033920032768-gKXvw97loCpJBz5lfz1lDKlcbUOJAK"
access_token_secret = "9CJ8MiX4i4LlwRgwrDMKbBZlXVhANSHGJ35dAdB13R3L2"
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.wait_on_rate_limit= True
api.wait_on_rate_limit_notify= True

def get_avg():
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
        tweets = tweepy.Cursor(api.search_tweets,
                               q, lang="en").items(20)
        list_tweets = [tweet for tweet in tweets]
        for tweet in list_tweets:
            usernameList.append(tweet.user.screen_name)



    print(usernameList)
    print(len(usernameList))



    randomlist = random.sample(range(0, len(usernameList)), 500)
    totalavgsum= 0

    userAvg = []
    validUsers =0

    for i in randomlist:
        userID= usernameList[i]
        tweets = api.user_timeline(screen_name=userID,
                                   # 200 is the maximum allowed count
                                   count=1000,
                                   include_rts = False,)
        ret= {}

        for tweet in tweets:
            # print(tweet.entities['hashtags'])
            for l in tweet.entities['hashtags']:
                word= l['text']
                if word in ret:
                    ret[word] += [tweet]
                else:
                    ret[word] = [tweet]
                # print(word)

        # if len(ret) == 0:
        #     continue

        sum = 0

        for hashtweets in ret.items():
            c= hashtweets[1]
            a= hashtweets[1][0]
            b= hashtweets[1][-1]
            # print(a.created_at)
            diff = a.created_at - b.created_at
            # print(diff.total_seconds())
            sum += diff.total_seconds()
            # print(sum)

        validUsers += 1

        if len(tweets) > 0:
            avg = sum / len(tweets)
            totalavgsum += avg
            userAvg.append(avg)

    avg = totalavgsum/validUsers
    print(avg)
    print(userAvg)
    print(validUsers)
    return avg


sum= 0
for i in range(1, 10):
    sum+= get_avg()
sum/= 10

print("Our Final answer")
print(sum)



# t = datetime.strptime("0 days 00:00:00"," %H:%M:%S"
