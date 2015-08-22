import tweepy
from config import *

# get specific user tweets
def get_user_tweets(screen_name):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth)

    ans = []
    for p in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=200, include_rts=True).pages():
        for t in p:
            ans.append(t)
    return ans


