# :fire: [Tweet2Emoji](https://tweet02emoji.herokuapp.com/) :fire:

## Introduction

Tweet2Emoji is a emoji classifier. It takes your tweets and assigns an appropriate emoji. Given the text of a tweet, our machine learning model can predict the most likely assosiated emoji's. We framed the problem as multi-class classification problem. With the dataset in used, we identified the 10 most commonly used emojis. We decided to used **Logistic Regression**, **Support Vector Machines(SVM)**, and **Naive Bayes** to see which classifier preforms the best. The current baseline approach (and the approach used the web app [here](Tweet2Emoji](https://tweet02emoji.herokuapp.com/)) is Logistic Regression. We then evaluate the model using accuracy and F1 score.


## Data (TODO)


### CNN 

|      Layer     |                                                              Params                                                             | Value |
|:--------------:|:-------------------------------------------------------------------------------------------------------------------------------:|-------|
|    Embedding   | Input Dimensions <br> Output Dimensions <br> Weights <br> Maximum Sequence Length <br> Trainable<br> Embeddings Regularizer<br> |2001   |
|     Dropout    |                                                            Percentage                                                           |       |
| 1D Convolution |                        Filters<br> Kernel Size <br> Activation <br> Padding <br> Kernel Regularizer <br>                        |       |
| 1D Max Pooling | Pool Size                                                                                                                       |       |
| Flatten        | /                                                                                                                               |       |
| Dropout        | Percentage                                                                                                                      |       |
| Dense          | Classes <br> Activation                                                                                                         |       |


###  Bi-LSTM

|      Layer            |                                                              Params                                                             | Value |
|:---------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:-------:|
|Embedding              | Input Dimensions <br> Output Dimensions <br> Weights <br> Maximum Sequence Length <br> Trainable<br> Embeddings Regularizer<br> |2001   |
|1D Spatial Dropout     |                                                            Percentage                                                           |20     |
|Bi-LSTM                | Output Dimensionality                                                                                                           |64     |
|Bi-LSTM                | Output Dimensionality                                                                                                           |32     | 
|Dense                  | Classes <br> Activation                                                                                                         |20<br>softmax|



## Results


## Replicate (TODO)

If you are a complete beginner, follow these steps to replicate the results in jupyter notebook. 

Clone the repository

```
git clone https://github.com/knarfamlap/tweet2emoji.git
```

Download the GloVe vectors from [here]()

If you dont have `vitualenv` run the following line

```
pip install virtualenv
```

Inside the tweet2emoji directory, run:

```
virtualenv env
```

Activate the enviroment

```
source env/bin/activate
```

Installing the dependecies

```
pip3 install -r requirements.txt
```

Run the Jupyter Notebook

```
jupyter notebook
```

Then open `main.ipynb` 



## TODO
- [x] Clean up Jupyter notebook
- [ ] Finish README
- [ ] Clean up webpage
  - [ ] add github links to footer

## Authors
- Frank Palma Gomez  (**@knarfamlap**)