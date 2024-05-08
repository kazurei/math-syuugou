import streamlit as st

st.title("bmi")
st.write("体重を入力してください")

weight = st.number_input("体重を入力してください",min_value=1)

height = st.number_input("身長を入力してください",min_value=1)

BMI = weight/height**2

st.write("BMIは"+str(BMI)+"です")

