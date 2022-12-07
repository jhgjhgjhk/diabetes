# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:27:29 2022

@author: lipim
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('dialog.sav','rb'))

def diabetes_prediction(input_data):
    input_data_array=np.asarray(input_data)
    input_data_reshape=input_data_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    if (prediction[0]==0):
        return 'The person is not diabetic.'
    else:
        return 'The person is diabetic.'

def main():
    
    st.title('Diabetes Prediction')
    
    
    Pregnancies=st.number_input('Pregnancies')
    Glucose=st.number_input('Glucose')
    BloodPressure=st.number_input('BloodPressure')
    SkinThickness=st.number_input('SkinThickness')
    Insulin=st.number_input('Insulin')
    BMI=st.number_input('BMI')
    DiabetesPedigreeFunction=st.number_input('DiabetesPedigreeFunction')
    Age=st.number_input('Age')
    
    
    diagnosis=''
    
    if st.button('Diabetes test'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
if __name__=="__main__":
    main()