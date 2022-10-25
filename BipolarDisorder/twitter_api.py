import tweepy
import configparser
import pandas as pd


#read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = '@CalculatingMind'
limit = 300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)


data = []
for tweet in tweets:
    data.append([tweet.full_text])

df = pd.DataFrame(data)

print(df)

df.to_csv('tweets.csv')

# keywords = 'I have bipolar'
# limit = 300

# tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=200, tweet_mode='extended').items(limit)

# for tweet in tweets:
#     print(tweet.full_text)
# tweets = api.user_timeline(count=200)
# tweets_extended = api.user_timeline(tweet_mode='extended', count=200)
 
# # Show one tweet's JSON
# tweet = tweets[0]
# tweet._json


# public_tweets = api.home_timeline()

# columns = ['Time', 'User', 'Tweet']
# data = []
# for tweet in tweets:
#     data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

# df = pd.DataFrame(data, columns=columns)

# print(df)

# df.to_csv('tweets.csv')


