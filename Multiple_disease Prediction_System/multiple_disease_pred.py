import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("C:/Users/Pragati/Desktop/Multiple_disease Prediction_System/saved_models/diabetes_model.sav",'rb'))

heart_diesase_model = pickle.load(open("C:/Users/Pragati/Desktop/Multiple_disease Prediction_System/saved_models/heart_disease_model.sav",'rb'))

parkinsons_model = pickle.load(open("C:/Users/Pragati/Desktop/Multiple_disease Prediction_System/saved_models/parkinsons_model.sav",'rb'))

# sidebar for navigation

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"],default_index = 0)


# Diabetes prediction page
if (selected == "Diabetes Prediction"):
    # page title
    st.title("Diabetes Prediction using ML")

if (selected == "Heart Disease Prediction"):
    st.title("Heart Disease Prediction using ML")

if (selected == "Parkinsons Prediction"):
    st.title("Parkinsons Prediction using ML")







