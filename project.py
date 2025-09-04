import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

model=pkl.load(open("final_model.pkl","rb"))

st.header("Medical Insurance Predictor")

age=st.slider("Age:",18,100,30)
sex=st.selectbox("sex:",["male","female"])
bmi= st.number_input("BMI:",10.0,50.0,25.0)
children= st.slider("Number of Children:",0,5,1)
smoker=st.selectbox("Smoker:",["yes","no"])
region=st.selectbox("Which region belongs to :",["southwest","southeast","northwest","northeast"])

if sex=="female":
    sex=0
else :
    sex=1

if smoker=="yes":
    smoker=0
else:
    smoker=1


if region=="northeast":
   region=0
elif region=="northwest":
    region=1
elif region=="southeast":
    region=2
else:
    region=3

input_data=(age,sex,bmi,children,smoker,region)
input_data=np.array(input_data)
input_data=input_data.reshape(1,-1)

if st.button("Predict"):
    Medical_insurance=model.predict(input_data)

    display_string="Insurance will be "+str(round(Medical_insurance[0],2))+" rs"

    st.markdown(display_string)

