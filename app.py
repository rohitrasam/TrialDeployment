# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:13:18 2023

@author: rasam
"""

import streamlit as st
import pandas as pd

st.title('Machine Learning Model!☕')

st.markdown('This is my 1st deployment project!✌🏾')

st.text('ML model with stream lit')

st.selectbox('Select yout city', ['Pune', 'Bengaluru', 'Mumbai'])
# st.select_slider('Age: ', range(1, 99))
st.number_input('Age: ', min_value=0, max_value=100)


df = pd.read_csv('cars1.csv')
st.line_chart(df['height'])
