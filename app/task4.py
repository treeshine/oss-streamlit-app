import streamlit as st

st.multiselect("선택", ["species", "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"])
st.selectbox("카테고리 선택",["전체","species", "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"])

