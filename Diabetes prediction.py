# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 13:44:57 2025

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 16:11:15 2025

@author: user
"""

import streamlit as st
import pickle
import requests
import os

# Download the model file from GitHub
url = "https://github.com/Noorenmariyam/Diabetes-disease-prediction/raw/main/trained_model%20%282%29.sav"  # Replace with actual raw link
response = requests.get(url, stream=True)
with open("trained_model.sav", "wb") as f:
    f.write(response.content)

# Load the model
loaded_model = pickle.load(open("trained_model.sav", "rb"))

# Continue with your Streamlit app logic...
st.title("Diabetes Prediction App")
# Add your input fields, prediction logic, etc.

import numpy as np
import pickle
import streamlit as st



# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
