import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("C:/Users/Pragati/Desktop/Multiple_disease Prediction_System/saved_models/diabetes_model.sav",'rb'))

heart_disease_model = pickle.load(open("C:/Users/Pragati/Desktop/Multiple_disease Prediction_System/saved_models/heart_disease_model.sav",'rb'))

parkinsons_model = pickle.load(open("C:/Users/Pragati/Desktop/Multiple_disease Prediction_System/saved_models/parkinsons_model.sav",'rb'))

# sidebar for navigation

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
    ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"],
    icons = ['activity','heart','person'],
    default_index = 0)


# Diabetes prediction page
if (selected == "Diabetes Prediction"):
    # page title
    st.title("Diabetes Prediction using ML")

    #getting the input data from the user
    # colums for input  fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')



# code for Prediction
diab_diagnosis = ''

# creating  a button gor Prediction

if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    if (diab_prediction(0)==1):
        diab_diagnosis = 'The person is Diabetic'
    else:
        diab_diagnosis = 'The person is not Diabetic'
st.success(diab_diagnosis)



# Diabetes prediction page

if (selected == "Heart Disease Prediction"):
    st.title("Heart Disease Prediction using ML")

    #getting the input data from the user
    # colums for input  fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain Type')

    with col1:
        trestbps = st.text_input('Resting   Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        temp = st.text_input('temperature')
        

heart_disease = ''

# creating  a button gor Prediction

if st.button('Heart Disease Test Result'):
    heart_disease = heart_disease_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    if (heart_disease(0)==1):
        heart_disease = 'The person is having heart disease'
    else:
        heart_disease = 'The person is not having heart Disease'
st.success(heart_disease)

if (selected == "Parkinsons Prediction"):
    st.title("Parkinsons Prediction using ML")







