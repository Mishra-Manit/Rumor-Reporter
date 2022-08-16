import pickle

from flask import Flask
from flask import render_template
from flask import Response
from flask import request, redirect
import os

import pandas as pd   
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import spacy
import wordcloud
import os 
import sys
pd.options.mode.chained_assignment = None 

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spacy.lang.en.stop_words import STOP_WORDS
nltk.download('wordnet')
nltk.download('punkt')

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
import en_core_web_md
text_to_nlp = en_core_web_md.load()

import pickle

# Create the Flask App
app = Flask(__name__)

#Load the pickle model
model = pickle.load(open("model.pkl", "rb"))
tfidfModel = pickle.load(open("tfidfvectorizer.pkl", "rb"))

@app.route("/",)
def Home():
    return render_template("index.html")

@app.route("/input")
def userInputPage():
    return render_template("input.html")

@app.route("/predict", methods=["POST"])
def predict():
    textGivenByUser = request.form['text']

    prediction = predictUsingMethod(textGivenByUser)

    sentiment = sentimentAnalysis(textGivenByUser)

    return render_template("input.html", prediction=prediction, sentiment=sentiment)


def predictUsingMethod(text):
    review = text.lower()
    review = review.split()
    review = ' '.join(review)
    
    review_vect = tfidfModel.transform([review]).toarray()
    
    a=model.predict(review_vect)[0]
    
    prediction = " "
    
    if a == "FAKE":
        prediction = "Fake"
    if a == "REAL":
        prediction = "Real"

    return prediction

def tokenize(text):
    clean_tokens = []
    for token in text_to_nlp(text):
        if (not token.is_stop) & (token.lemma_ != '-PRON-') & (not token.is_punct):  
            clean_tokens.append(token.lemma_)
    return clean_tokens

logregModel = pickle.load(open('logreg.pkl', 'rb'))
bowTransformer = pickle.load(open('bowTransformer.pkl', 'rb'))

def sentimentAnalysis(text):
    example_review = text
    prediction = logregModel.predict(bowTransformer.transform([example_review]))

    review = " "

    if prediction:
      review = "Positive"
    else:
      review = "Negative"

    return review

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5000)