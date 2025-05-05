import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title('Hypertension, Stroke, and Diabetes Predictor')

st.info('HSD is a machine learning web application for simultaneously predicting **Hypertension, Stroke, and Diabetes.**')

st.sidebar.header('User Input Parameters')

with st.expander('**Data**'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/DwaneGarcia/hrd-machinelearning/refs/heads/master/diabetes_data.csv')
  df

  st.write('**X**')
  X = df.drop('Stroke', axis=1)
  X

  st.write('**y**')
  y = df.Stroke
  y
