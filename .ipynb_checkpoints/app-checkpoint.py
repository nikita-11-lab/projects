import pickle
import streamlit as st
pickle.dump(pipe,open("pipe.pkl", "wbt"))
st.title("car price prediction app")