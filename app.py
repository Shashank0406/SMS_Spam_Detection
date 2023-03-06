import string
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_msg(msg):
    msg = msg.lower()
    msg = nltk.word_tokenize(msg)
    y = []
    for i in msg:
        if i.isalnum():
            y.append(i)

    msg = y[:]
    y.clear()

    for i in msg:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    msg = y[:]
    y.clear()

    for i in msg:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('mnbmodel.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")
input_sms = st.text_input("Enter the message")

if st.button('Predict'):

    # 1. Preprocess
    transform_sms = transform_msg(input_sms)
    # 2. Vectorize
    vector_inp = tfidf.transform([transform_sms])
    # 3. Predict
    result = model.predict(vector_inp)
    # 4. Display

    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
