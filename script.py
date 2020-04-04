"""
Script that talks to twitter api to fetch tweet text. 
Converts txt files to csv
"""
import csv
import config
import tweepy
from tweepy import TweepError
import pandas as pd
import numpy as np
import re
import preprocessor as p


def to_single_annotation(files):
    # delete lines that contain more than one emoji .
    for text_file in files.keys():
        with open(text_file, "r") as f:
            lines = f.readlines()
            with open(text_file, "w") as f_w:
                for line in lines:
                    if (',' not in line.strip('\n').split('\t')[1]):
                        f_w.write(line)


def tab_to_comma(files):
    for text_file in files.keys():
        with open(text_file, "r") as f:
            lines = f.readlines()
            with open(text_file, "w") as f_w:
                for line in lines:
                    f_w.write(line.replace("\t", ","))


def txt_to_csv(files):
    for text_file, csv_file in files.items():
        with open(text_file, "r") as f:
            lines = f.readlines()
            with open(csv_file, "w") as f_w:
                for line in lines:
                    f_w.write(line)


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def get_tweet_text(tweet_id):
    return api.get_status(tweet_id).text


def fetch_tweet_text(files):
    for csv_file in files.values():
        print('--------- Fetching Tweets for: ', csv_file)
        df = pd.read_csv(csv_file)
        id_text = []
        for tweet_id in df['id']:
            try:
                tweet_text = deEmojify(p.clean(get_tweet_text(tweet_id)))
                print(tweet_text)
                id_text.append(tweet_text)
            except TweepError:
                print('Adding NaN for: ', tweet_id)
                id_text.append(np.NaN)
        df['id_text'] = id_text
        print(df)
        df.to_csv(csv_file, index=False)


auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth)


# files
balanced_test_plaintext = './datasets/twemoji/balanced_test_plaintext.txt'
full_test_plaintext = './datasets/twemoji/full_test_plaintext.txt'
full_train_plaintext = './datasets/twemoji/full_train_plaintext.txt'
full_valid_plaintext = './datasets/twemoji/full_valid_plaintext.txt'

files = {
    balanced_test_plaintext: './datasets/twemoji/balanced_test_plaintext.csv',
    full_test_plaintext: './datasets/twemoji/full_test_plaintext.csv',
    full_train_plaintext: './datasets/twemoji/full_train_plaintext.csv',
    full_valid_plaintext: './datasets/twemoji/full_valid_plaintext.csv'
}

# tweet = api.get_status(743539483279122432)
# print(tweet.text)

print('--------------------- DELETING LINES WITH MORE THAN ONE ANNOTATION')
# delete lines that contain more than one emoji .
to_single_annotation(files)

# replcae tabs with commas
print('--------------------- REPLACING TABS WITH COMMAS')
tab_to_comma(files)

# covert txt files to csv
print('--------------------- CONVERTING TEXT FILES TO CSV FILES')
txt_to_csv(files)

# fetching tweet text
print('--------------------- FETCHING TWEET TEXT')
fetch_tweet_text(files)
