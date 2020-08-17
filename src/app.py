import pickle
import os
import numpy as np
from vectorizer import vect, emoji_mappings
from wtforms import Form, TextAreField, validators

app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, "pkl_objects", "sgdc_clf.pkl"), 'rb'))

def classify(document):
    X = vect.transform([document])
    y = clf.predict(X)[0]

    proba = np.max(clf.predict_proba(X))

    return  emoji_mappings.iloc[y], proba


@app.route('/')
def index():
    return render_template('first_app.html')

if __name__ == '__main__': 
    app.run()

