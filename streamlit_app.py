import streamlit as st
import pandas as pd

st.title('Hypertension, Stroke, and Diabetes Predictor')

st.info('HSD is a machine learning web application for simultaneously predicting Hypertension, Stroke, and Diabetes.')

with st.expander('Data'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/DwaneGarcia/hrd-machinelearning/refs/heads/master/diabetes_data.csv')
  df
