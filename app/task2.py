import streamlit as st
import pandas as pd
import numpy as np

st.title("Task 2: Display a dataframe")
st.header("dataframe")
np.random.seed(42)
data = {
    'A': [0, 1],
    'B': [np.random.uniform(-1, 0), np.random.uniform(-1, 0)],
    'C': [np.random.uniform(-1, 0), np.random.uniform(-1, 0)],
    'D': [np.random.uniform(-1, 0), np.random.uniform(-1, 0)]
}
df = pd.DataFrame(data).set_index(0) 
df.index.name = None
df.columns = ['A', 'B', 'C', 'D'] 
df = pd.DataFrame(
    np.random.uniform(-1, 0, size=(2, 3)), 
    columns=['A', 'B', 'C'],
    index=[0, 1]
)
df = df.round(4)
st.dataframe(df)
