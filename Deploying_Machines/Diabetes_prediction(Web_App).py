# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 
import streamlit as st

try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()


#creating a function 
def diabetes_prediction(input_data):
    input_as_numpy_Array=np.asarray(input_data)

#reshaping the array as the model thinks that we will give another 768 rows of input whereas we are just using one instance/row to predict
    input_reshaped=input_as_numpy_Array.reshape(1,-1)
 
    prediction=loaded_model.predict(input_reshaped)

    if(prediction[0]==0):
        return "The person is not diabetic!"
    else:
        return"The person is diabetic!"

def main():
    #giving a title
    st.title('Diabetes Prediction Web App')
    #getting the input data
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Enter the GLucose level')
    BloodPressure=st.text_input('Enter the BloodPressure')
    SkinThickness=st.text_input('Enter the SkinThickness')
    Insulin=st.text_input('Enter the Insulin level')
    BMI=st.text_input('BMI no.')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    Age=st.text_input('Enter the age')
                
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
if __name__ =='__main__':
    main()
        
