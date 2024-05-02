import streamlit as st

import random

st.title("おみくじ")

if st.button("おみくじを引く"):

    results=["大吉","中吉","小吉"]

    result=random.choice(results)

    st.write(f"結果:{result}")
