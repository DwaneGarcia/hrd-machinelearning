import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('Hypertension and Stroke Predictor')

st.info('Sebastian is a machine learning web application for simultaneously predicting **Hypertension and Stroke.**')

with st.expander('**Data**'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/DwaneGarcia/hrd-machinelearning/refs/heads/master/hypertension_data.csv')
  df

  st.write('**X**')
  X_raw = df.drop('target', axis=1)
  X_raw

  st.write('**Y**')
  Y = df.target
  Y

with st.expander('**Data Visualization**'):
  st.scatter_chart(data=df, x='age', y='thalach', color='target')

# Data preparation
with st.sidebar:
  st.header('Input Features')
  #Age","Sex","HighChol","CholCheck","BMI","Smoker","HeartDiseaseorAttack","PhysActivity","Fruits","Veggies","HvyAlcoholConsump","GenHlth","MentHlth","PhysHlth","DiffWalk"
  age = st.selectbox('Age', ('11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98'))
  sex = st.selectbox('Sex', ('0', '1'))
  cp = st.selectbox('Chest Pain Type', ('0', '1', '2', '3'))
  fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ('0', '1'))
  restecg = st.selectbox('Resting ECG Results', ('0', '1', '2'))
  exang = st.selectbox('Exercise Induced Angina', ('0', '1'))
  slope = st.selectbox('Slope of the peak exercise ST segment', ('0', '1', '2'))
  ca = st.selectbox('Number of major vessels (0–3) colored by flourosopy', ('0', '1', '2', '3', '4'))
  thal = st. selectbox('Thalassemia (3: Normal; 6: Fixed defect; 7: Reversable defect)', ('0', '1', '2', '3'))
  trestbps = st.slider('Resting Blood Pressure (in mm Hg)', 94, 200, 94)
  chol = st.slider('Serum Cholestoral in mg/dl', 126, 564, 126)
  thalach = st.slider('Maximum Heart Rate Achieved', 71, 202, 71)
  oldpeak = st.slider('ST depression induced by exercise relative to rest', 0.0, 6.2, 0.0)

  # Create a DataFrame for the input features
  data = {'age': age,
          'sex': sex,
          'cp': cp,
          'fbs': fbs,
          'restecg': restecg,
          'exang': exang,
          'slope': slope,
          'ca': ca,
          'thal': thal,
          'trestbps': trestbps,
          'chol': chol,
          'thalach': thalach,
          'oldpeak': oldpeak}
  input_df = pd.DataFrame(data, index=[0])
  input_disease = pd.concat([input_df, X_raw], axis=0)

with st.expander('**Input Features**'):
  st.write('**Input Disease**')
  input_df
  st.write('**Combined Disease Data**')
  input_disease

# Data Preparation
# Encode

X = input_disease[1:]
input_row = input_disease[:1]

with st.expander('**Data Preparation**'):
  st.write('**Encoded X (Input Disease)**')
  input_df
  st.write('**Encoded Y (Input Disease)**')
  Y
  
# Model Training and Inference
## Train the ML model
clf = RandomForestClassifier()
clf.fit(X, Y)

## Apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_poba(input_row)

prediction_proba
