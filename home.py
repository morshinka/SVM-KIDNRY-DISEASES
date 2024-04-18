import streamlit as st 
from web_function import load_data
from Tabs import accuracy

Tabs = {
    "Accuracy" : accuracy,
}

st.sidebar.title("SVM KIDNEY DISEASES")

page = st.sidebar.radio("Page",list(Tabs.keys()))

df, x, y = load_data()

if page in ["Accuracy"]:
    st.sidebar.subheader(page)
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()