import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories,cutoff):
    categorial_map={}
    for i in range(len(categories)):
        if(categories.values[i]>=cutoff):
            categorial_map[categories.index[i]]=categories.index[i]
        else:
            categorial_map[categories.index[i]]="Others"
    return categorial_map

def clean_experience(x):
    if x=="More than 50 years":
        return 50
    elif x=="Less than 1 year":
        return 0.5
    return float(x)



def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    elif 'Master’s degree' in x:
        return 'Master’s degree'
    elif 'Professional degree' in x:
        return 'Post Grad'
    return 'Less then Bachelor'





@st.cache
def load_data():
    dataset=pd.read_csv("survey_results_public.csv")
    df=dataset[["Country","EdLevel","YearsCodePro","Employment","ConvertedCompYearly"]]
    df=df.rename({"ConvertedCompYearly":"Salary"},axis=1)
    df=df[df["Salary"].notnull()]
    df=df.dropna()
    df=df[df["Employment"]=="Employed, full-time"]
    df=df.drop("Employment",axis=1)


    country_map=shorten_categories(df.Country.value_counts(),400)
    df['Country']=df['Country'].map(country_map)
    df=df[df['Salary']<=250000]
    df=df[df['Salary']>=10000]
    df=df[df['Country']!='Other']


    df['YearsCodePro']=df['YearsCodePro'].apply(clean_experience)
    df['EdLevel']=df['EdLevel'].apply(clean_education)
    return df

df=load_data()

def show_explore():

    st.title("Explore Software Engineer Salaries")
    st.write(""" ### Stack Overflow Developer survey 2022""")
    data=df["Country"].value_counts()
    fig1 , ax1=plt.subplots()
    ax1.pie(data,labels=data.index,shadow=True,startangle=90)
    ax1.axis("equal")


    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)






















