import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data['model']
le_country = data["le_country"]
le_education = data["le_education"]


def shw_pred_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some information to predict the salary""")

    countries = ('United Kingdom of Great Britain and Northern Ireland',
                 'Netherlands', 'United States of America', 'Italy', 'Canada',
                 'Germany', 'Poland', 'France', 'Brazil', 'Sweden', 'Spain',
                 'India', 'Switzerland', 'Australia', 'Russian Federation', 'Others')

    education_data = ('Less then Bachelor', 'Master’s degree', 'Bachelor’s degree', 'Post Grad')

    country = st.selectbox("Countries", countries)
    education = st.selectbox("Education", education_data)

    experience = st.slider("Year Of Experience", 0, 50, 3)
    ok = st.button("Calculate")
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        y_pred = regressor.predict(X)
        st.subheader(f"The estimated salary is ${y_pred[0]:.2f}")
