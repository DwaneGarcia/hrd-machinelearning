import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title('Hypertension, Stroke, and Diabetes Predictor')

st.info('HSD is a machine learning web application for simultaneously predicting **Hypertension, Stroke, and Diabetes.**')

st.sidebar.header('User Input Parameters')

def user_input_features():
  Age = st.sidebar.slider('**Age** /13-level age category (1 = 18-24 9 = 60-64 13 = 80 or older)', 1, 13, 1)
  Sex = st.sidebar.slider('**Sex** /Patient's gender (0=female, 1=Male).', 0, 1, 0)
  HighChol = st.sidebar.slider('**High Cholesterol** (0=no, 1=yes)', 0, 1, 0)
  CholCheck = st.sidebar.slider('**Cholesterol Check** /In 5 years (0=no, 1=yes)', 0, 1, 0)
  BMI = st.sidebar.slider('**Body Mass Index**', 12, 98, 12)
  Smoker = st.sidebar.slider('**Smoking Background** /Have you smoked at least 100 cigarettes in your entire life? (0=no, 1=yes)', 0, 1, 0)
  HeartDiseaseorAttach = st.sidebar.slider('**Coronary Heart Disease (CHD) or Myocardial Infarction** (0=no, 1=yes)', 0, 1, 0)
  PhysActivity = st.sidebar.slider('**Physical Activity** /In the past 30 days - not including job (0=no, 1=yes)', 0, 1, 0)
  Fruits = st.sidebar.slider('**Fruits** /Consume Fruit 1 or more times per day (0=no, 1=yes)', 0, 1, 0)
  Veggies = st.sidebar.slider('**Vegetables** /Consume Vegetables 1 or more times per day (0=no, 1=yes)', 0, 1, 0)
  HvyAlcoholConsump = st.sidebar.slider('**Heavy Alcohol Consumption** /Adult men >=14 drinks per week and adult women>=7 drinks per week (0=no, 1=yes)', 0, 1, 0)
  GenHlth = st.sidebar.slider('**General Health** /Would you say that in general your health is: scale 1-5 (1 = excellent 2 = very good 3 = good 4 = fair 5 = poor)', 1, 5, 1)
  MentHlth = st.sidebar.slider('**Mental Health** /Days of poor mental health scale 1-30 days', 0, 30, 0)
  PhysHlth = st.sidebar.slider('**Physical Health** /Physical illness or injury days in past 30 days scale 1-30', 0, 30, 0)
  DiffWalk = st.sidebar.slider('**Difficulty in Walking** /Do you have serious difficulty walking or climbing stairs? (0=no, 1=yes)', 0, 1, 0)
  data = {'Age': Age,
          'Sex': Sex,
          'HighChol': HighChol,
          'CholCheck': CholCheck,
          'BMI': BMI,
          'Smoker': Smoker,
          'HeartDiseaseorAttack': HeartDiseaseorAttack,
          'PhysActivity': PhysActivity,
          'Fruits': Fruits,
          'Veggies': Veggies,
          'HvyAlcoholConsump': HvyAlcoholConsump,
          'GenHlth': GenHlth,
          'MentHlth': MentHlth,
          'PhysHlth': PhysHlth,
          'DiffWalk': DiffWalk}
  features = pd.DataFrame(data, index=[0])
  return features

df = user_input_features()

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
