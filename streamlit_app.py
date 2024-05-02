
import streamlit as st
import random

st.title("ガチャガチャアプリ")

options = ["アイテム1", "アイテム2", "アイテム3", "アイテム4", "アイテム5"]  # ガチャのアイテムリスト

if st.button("ガチャを引く"):
    result = random.choice(options)  # ランダムにアイテムを選択
    st.write("結果：", result)  # 結果を表示
