import streamlit as st

st.title("Task 6: 레이아웃 구성")

# 1) Columns
st.header("1. Columns 예시")

col1, col2 = st.columns(2)

with col1:
    st.write("이곳은 첫 번째 컬럼입니다.")
with col2:
    st.write("이곳은 두 번째 컬럼입니다.")

# 2) Tabs
st.header("2. Tabs 예시")

tab1, tab2 = st.tabs(["탭 1", "탭 2"])

with tab1:
    st.write("탭 1 내용입니다.")
with tab2:
    st.write("탭 2 내용입니다.")

# 3) Expander
st.header("3. Expander 예시")

with st.expander("펼치기/접기"):
    st.write("여기에 추가 정보를 넣을 수 있습니다.")
