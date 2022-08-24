# -*- coding: utf-8 -*-
"""
language translator web based application

Spyder Editor

Opera Browser

This is a temporary script file.

This code is for language translator web based
application where we convert one language into
other specified language

Aditya Kumar
Roll no- 20223007
MCA 4TH SEM
ADM TERM PROJECT
"""

import streamlit as st 
#streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

import googletrans
#googletrans is a free and unlimited python library that implemented Google Translate API. 

#create an instance of Translator to use Google Translate ajax API
translator = googletrans.Translator()

#generating key-value pair for eg. key = 'hi' & value = 'hindi' for hindi language
def get_key(val):
    for key, value in googletrans.LANGUAGES.items():
         if val == value:
                return key
    return "key doesn't exist"

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

st.write('LANGUAGE TRANSLATOR PROJECT')

#select destination language 
option=st.selectbox('Select Language',tuple(googletrans.LANGUAGES.values()))

#enter sentence
text=st.text_area('Input the text')

#source language is translated into destination language
translated = translator.translate(text, dest=get_key(option))

#show result in destination language
st.write(translated.text)

st.write('Aditya Kumar ADM Project')
