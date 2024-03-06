import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write(
    """
    #Iris Flower Prediction App
    
    This app predicts the Iris Flower App
    """
)

st.sidebar.header('User Input Paramters')

def user_input_features():
    sepal_length=st.sidebar.slider('sepal length',4.1,8.2,5.1)
    st.sidebar.write(f"Sepal length selected is {sepal_length}")
    sepal_width=st.sidebar.slider('sepal_width',2.9,4.6,3.1)
    st.sidebar.write(f"Sepal width selected is {sepal_width}")
    petal_width=st.sidebar.slider('petal width',5.9,7.9,1.0)
    st.sidebar.write(f"Petal width selected is {petal_width}")
    petal_length=st.sidebar.slider('Petal Length',4.0,8.0,4.0)
    st.sidebar.write(f"Petal Length selected is {petal_length}")

    data={
        'sepal length':sepal_length,
        # f"Sepal length selected is {sepal_length}":0,
        'sepal width':sepal_width,
        'petal width':petal_width,
        'petal length':petal_length
    }


    features=pd.DataFrame(data,index=[1])
    print(features)
    return features


f=user_input_features()
st.subheader("User Input Parameters")
st.write(f)

iris=datasets.load_iris()
X=iris.data
Y=iris.target

clf=RandomForestClassifier()
clf.fit(X,Y)

prediction=clf.predict(f)
prediction_probe=clf.predict_proba(f)

st.subheader('Class Labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probablity')
st.write(prediction_probe)
