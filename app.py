import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.title("car price prediction app")
pipe=pickle.load(open('pipe.pkl','rb'))

df=pd.read_csv('final_data.csv')
companies = sorted(df['company'].unique())
years = range(2000,2027)
company = st.sidebar.selectbox("select company",companies)
names = sorted(df[df['company']== company]["name"].unique())
name = st.sidebar.selectbox("select name:",names)
year = st.sidebar.selectbox("select year:",years)
km_driven = st.sidebar.number_input("enter km_driven:",value=5000,min_value=1000,max_value=200000,step=1000)
fuel = st.sidebar.selectbox("select fuel type:",["Petrol","Diesel"])

if st.sidebar.button("Predict Price:"):
    st.write("you have selected")
    st.write(f"company: {company}")
    st.write(f"Name: {name}")
    st.write(f"Year: {year}")
    st.write(f"kilo meters driven: {km_driven}")
    st.write(f"Fuel Type: {fuel}")
    
    
    myinput=[[company,name,year,km_driven,fuel]]
    columns= ['company','name','year','kms_driven','fuel_type']
    myinput=pd.DataFrame(data=myinput,columns=columns)
    
    result=pipe.predict(myinput)
    if result[0]<0:
        st.write("sorry,predicted value is negative....Please check your input values")
    else:
        st.write("Predicted Prices:",str(round(result[0][0])))