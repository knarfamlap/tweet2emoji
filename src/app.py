import pickle
import os
import numpy as np
from vectorizer import vect, emoji_mappings
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import bz2
import _pickle as cPickle
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences


app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
cnn = tf.keras.models.load_model(os.path.join(cur_dir, 'tf_models', 'cnn'))
# clf = cPickle.load(bz2.BZ2File(os.path.join(cur_dir, "pkl_objects", "cmprs.pbz2"), 'rb'))

class_ids = [186,  830, 1056, 1107, 1138, 1210, 1380, 1381, 1384, 1389, 1392,
             1393, 1394, 1397, 1403, 1420, 1424, 1446, 1447, 1620]


sequence_length = 60


def classify(document):
    X = pad_sequences(vect.tokenizer.texts_to_sequences([document]), sequence_length)
    preds = cnn.predict(X)

    
    top_k_values, top_k_indices = tf.nn.top_k(preds, k=3)

    top_k_values = np.array(top_k_values).flatten()
    top_k_indices = np.array(top_k_indices).flatten()

    # arr of tuples with top 3 emojis and probas
    # (emoji, proba)
    res = [(emoji_mappings.iloc[class_ids[top_k_indices[i]]]['ucode'], round(top_k_values[i]*100, 2) ) for i in range(3)]

    return res[0], res[1], res[2]


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
        pred1, pred2, pred3 = classify(input)
        return render_template('results.html', content=input, pred1=pred1, pred2=pred2, pred3=pred3)

    return render_template('first_app.html', form=form)


if __name__ == '__main__':
    app.run()
