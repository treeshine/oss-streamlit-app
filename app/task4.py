import streamlit as st
import pandas as pd

st.title("Task 4: 인터랙티브 필터")

df = pd.read_csv("./data/penguins.csv")

columns = [
    "species",
    "island",
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
]

selected_category = st.selectbox("카테고리 선택", ["전체"] + columns)

if selected_category == "전체":
    result = df
else:
    result = df[[selected_category]]

st.subheader("필터 결과")
st.dataframe(result)


# 숫자 타입일 때만 bar_chart 가능
if selected_category in [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]:
    st.subheader("차트")
    st.bar_chart(result)
else:
    st.info("이 컬럼은 숫자 타입이 아니라 차트를 그릴 수 없습니다.")
