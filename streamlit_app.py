import streamlit as st
st.title("集合を求める")
U = st.text_input("全体集合を入力してください")
zentaisyuugouu = set(U.split())

A = st.text_input("集合Aを入力してください")
B = st.text_input("集合Bを入力してください")

syuugoua = set(A.split())
syuugoub = set(B.split())

katu = syuugoua & syuugoub   #AかつＢ
mataha = syuugoua | syuugoub #ＡまたはＢ

A_bar = zentaisyuugouu - syuugoua
B_bar = zentaisyuugouu - syuugoub

a_barkatu = A_bar & syuugoub    #ＡバーかつＢ
a_barmataha = A_bar | syuugoub  #ＡバーまたはＢ
b_barkatu = B_bar & syuugoua    #ＡかつＢバー
b_barmataha = B_bar | syuugoua  #ＡまたはＢバー
a_barkatub_bar = A_bar & B_bar  #ＡバーかつＢバー
a_barmataha_bar = A_bar | B_bar #ＡバーまたはＢバー

st.write("AかつB:", katu)
st.write("AまたはB:", mataha)
st.write("ＡバーかつＢ", a_barkatu)
st.write("ＡバーまたはＢ", a_barmataha)
st.write("ＡかつＢバー", b_barkatu)
st.write("ＡまたはＢバー", b_barmataha)
st.write("ＡバーかつＢバー", a_barkatub_bar)
st.write("ＡバーまたはＢバー", a_barmataha_bar)

