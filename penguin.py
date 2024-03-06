import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

penguins = pd.read_csv('penguins_cleaned.csv')
df = penguins.copy()
target = 'species'
encode = ['sex', 'island']

# Set 'max_columns' option explicitly


for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    print(dummy)
    df = pd.concat([df, dummy], axis=1)
    print(df)
    del df[col]
    print(df)

target_mapper={'Adelie':0,'Chinstrap':1,'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species']=df['species'].apply(target_encode)
pd.set_option('display.max_columns', None)
print(df)
pd.reset_option('display.max_columns')
X=df.drop('species',axis=1)
print(X)
y=df['species']
print(y)

clf=RandomForestClassifier()
clf.fit(X,y)



import pickle
pickle.dump(clf, open('penguin_clf.pkl', 'wb'))
