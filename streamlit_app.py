import streamlit as st

import random

st.title("おみくじアプリ")

 set.button("おみくじを引く")

    results=["大吉","中吉","小吉"]

    result=random.choice(result)

    st.write(f"結果:{result}")
