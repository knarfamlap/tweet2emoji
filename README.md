# :fire: [Tweet2Emoji](https://tweet02emoji.herokuapp.com/) :fire:

Tweet2Emoji is a emoji classifier. It takes your tweets and assigns an appropriate emoji. Given the text of a tweet, our machine learning model can predict the most likely assosiated emoji's. We framed the problem as multi-class classification problem. 

With the dataset in used, we identified the 20 most commonly used emojis. We decided to used **Logistic Regression**, **Support Vector Machines(SVM)**, and **Naive Bayes** to see which classifier preforms the best. The current baseline approach is **SVM**. The baseline model preforms poorly in the multiclass problem with 20 different emojis. It reaches a F1 score of 1 with low accuracy. 

Moreover, neural networks preformed better than the baseline model. Using a **Bi-LSTM** and a **CNN**  reached F1 scores of 15 and 18 respectively. Both **Bi-LSTM** and **CNN** used **trainable GloVe embeddings**. 

[main.ipynb](main.ipynb) contains all data exploration and code to reproduce results. 

[Here](https://tweet02emoji.herokuapp.com/) is the webapp. Load times might be a bit long. 

The dataset for this project can be found in its Kaggle page [here](https://www.kaggle.com/knarfamlap/tweet2emoji/)

<!-- ## Data

The dataset used can be found [here](). 


### CNN 

|     Layer      |                                                             Params                                                              | Value |
| :------------: | :-----------------------------------------------------------------------------------------------------------------------------: | ----- |
|   Embedding    | Input Dimensions <br> Output Dimensions <br> Weights <br> Maximum Sequence Length <br> Trainable<br> Embeddings Regularizer<br> | 2001  |
|    Dropout     |                                                           Percentage                                                            |       |
| 1D Convolution |                        Filters<br> Kernel Size <br> Activation <br> Padding <br> Kernel Regularizer <br>                        |       |
| 1D Max Pooling |                                                            Pool Size                                                            |       |
|    Flatten     |                                                                /                                                                |       |
|    Dropout     |                                                           Percentage                                                            |       |
|     Dense      |                                                     Classes <br> Activation                                                     |       |


###  Bi-LSTM

|       Layer        |                                                             Params                                                              |     Value     |
| :----------------: | :-----------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|     Embedding      | Input Dimensions <br> Output Dimensions <br> Weights <br> Maximum Sequence Length <br> Trainable<br> Embeddings Regularizer<br> |     2001      |
| 1D Spatial Dropout |                                                           Percentage                                                            |      20       |
|      Bi-LSTM       |                                                      Output Dimensionality                                                      |      64       |
|      Bi-LSTM       |                                                      Output Dimensionality                                                      |      32       |
|       Dense        |                                                     Classes <br> Activation                                                     | 20<br>softmax |



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
  - [ ] add github links to footer -->

## Authors
- Frank Palma Gomez  (**@knarfamlap**)