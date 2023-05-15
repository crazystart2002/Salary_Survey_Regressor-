from predict_page import shw_pred_page
import streamlit as st
from explore import show_explore

pages=st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if(pages=="Predict"):
    shw_pred_page()
else:
    show_explore()