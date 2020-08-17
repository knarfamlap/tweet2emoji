import pickle
import os
import numpy as np
from vectorizer import vect, emoji_mappings
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators



app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, "pkl_objects", "sgdc_clf.pkl"), 'rb'))

def classify(document):
    X = vect.transform([document])
    y = clf.predict(X)[0]

    proba = np.max(clf.predict_proba(X))

    return  emoji_mappings.iloc[y]['ucode'], proba

class InputForm(Form):
    input = TextAreaField('', [validators.DataRequired()])





@app.route('/')
def index():
    form = InputForm(request.form)
    return render_template('first_app.html', form=form)

@app.route('/results', methods=['POST']) 
def results():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        input = request.form['input']
        y, proba = classify(input)
        return render_template('results.html', content=input, prediction=y, probability=round(proba*100, 2))

    return render_template('first_app.html', form=form)


if __name__ == '__main__': 
    app.run()

