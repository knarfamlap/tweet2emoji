from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import gzip
import _pickle as cPickle
import bz2


cur_dir = os.path.dirname(__file__)

emoji_mappings = cPickle.load(bz2.BZ2File(os.path.join(cur_dir, "pkl_objects", "emoji_mappings.pbz2"), 'rb'))

def tokenizer(text):
    return text.split()


vect = HashingVectorizer(decode_error='ignore', n_features=2 **
                         21, preprocessor=None, tokenizer=tokenizer)
