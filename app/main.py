import streamlit as st

# Task 페이지 등록
task1 = st.Page("task1.py", title="Task 1 - 기본 UI")
task2 = st.Page("task2.py", title="Task 2 - 데이터프레임")
task3 = st.Page("task3.py", title="Task 3 - 차트")
task4 = st.Page("task4.py", title="Task 4 - 필터링")
task5 = st.Page("task5.py", title="Task 5 - CSV 업로드")
task6 = st.Page("task6.py", title="Task 6 -  업로드")

# 네비게이션 설정
pg = st.navigation([task1, task2, task3, task4, task5, task6])

# 선택된 페이지 실행
pg.run()
