import streamlit as st
import pandas as pd

st.title('Hypertension and Stroke Predictor')

st.info('HSP is a machine learning web application for simultaneously predicting **Hypertension and Stroke.**')

with st.expander('**Data**'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/DwaneGarcia/hrd-machinelearning/refs/heads/master/hypertension_data.csv')
  df

  st.write('**X**')
  X = df.drop('target', axis=1)
  X

  st.write('**Y**')
  Y = df.target
  Y

with st.expander('**Data Visualization**'):
  st.scatter_chart(data=df, x='age', y='thalach', color='target')

# Data preparation
with st.sidebar:
  st.header('Input Features')
  #Age","Sex","HighChol","CholCheck","BMI","Smoker","HeartDiseaseorAttack","PhysActivity","Fruits","Veggies","HvyAlcoholConsump","GenHlth","MentHlth","PhysHlth","DiffWalk"
  Age = st.selectbox('age', ('11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98'))
  Sex = st.selectbox('sex', ('0', '1'))


  
