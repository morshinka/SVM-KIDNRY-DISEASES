import numpy as np 
import pandas as pd
from sklearn import svm
import streamlit as st

@st.cache()
def load_data():
    df = pd.read_csv('fixed_data.csv')
    x = df[["bp","sg","al","su","rbc","pc","pcc","ba","bgr","bu","sc","sod","pot","hemo","pcv","wc","rc","htn","dm","cad","appet","pe","ane"]]
    y = df[["classification"]]
    
    return df, x, y

@st.cache_data()
def train_model(x,y):
    model = svm.SVC(kernel='linear')
    model.fit(x,y)
    score = model.score(x,y)
    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)
    prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction, score