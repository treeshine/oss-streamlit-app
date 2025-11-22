import streamlit as st
import pandas as pd
import numpy as np

st.header("Task 3: Draw Chart")

data = pd.DataFrame(
    np.random.randint(1, 100, size=(10, 3)),
    columns=["A", "B", "C"]
)

st.subheader(" 선 그래프(Line Chart)")
st.line_chart(data)

st.subheader(" 막대 그래프(Bar Chart)")
st.bar_chart(data)

st.subheader(" 영역 차트(Area Chart)")
st.area_chart(data)
