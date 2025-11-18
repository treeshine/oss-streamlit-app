import streamlit as st
st.set_page_config(
    page_title = 'streamlit tutorial',
    page_icon = ':shart')

st.header("Task 1. 기본 UI 컴포넌트")
st.text_input("이름을 입력하세요")
st.slider("나이",10,80)
st.selectbox("좋아하는 색",("빨강","파랑","노랑"))
st.checkbox("이용 약관에 동의합니다.")
st.button("제출")
