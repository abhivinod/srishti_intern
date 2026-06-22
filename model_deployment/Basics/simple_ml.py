import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
st.title("🌸Iris Flower Prediction")
iris=load_iris()
x,y=iris.data,iris.target
clf=RandomForestClassifier()
clf.fit(x,y)

sepal_length=st.slider("Sepal Length",4.0,8.0,5.0)
sepal_width=st.slider("Sepal Width",2.0,4.5,3.0)
petal_length=st.slider("Petal Length",4.0,8.0,5.0)
petal_width=st.slider("Petal Width",0.1,2.5,1.0)

button=st.button("Predict")
if button:
    prediction=clf.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    st.write("Prediction:",iris.target_names[prediction][0])