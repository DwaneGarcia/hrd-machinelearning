import streamlit as st
import pandas as pd

st.title('Hypertension, Stroke, and Diabetes Predictor')

st.info('HSD is a machine learning web application for simultaneously predicting **Hypertension, Stroke, and Diabetes.**')

with st.expander('**Data**'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/DwaneGarcia/hrd-machinelearning/refs/heads/master/diabetes_data.csv')
  df

  st.write('**X**')
  X = df.drop('Stroke', axis=1)
  X

  st.write('**Y**''**Z**''**A**')
  Y = df.Stroke
  Z = df.HighBP
  A = df.Diabetes
  Y
  Z
  A
