import config
import tweepy
from twython import Twython, TwythonError 

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth) 

tweet = api.get_status(747879438981947393)
print(tweet.text) 

