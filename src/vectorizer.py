from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle

cur_dir = os.path.dirname(__file__)

emoji_mappings = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'emoji_mappings.pkl'), 'rb'))

def tokenizer(text):
    return text.split()


vect = HashingVectorizer(decode_error='ignore', n_features=2 **
                         21, preprocessor=None, tokenizer=tokenizer)
