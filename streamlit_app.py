import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def main():
    st.title("集合を求める")

    st.write("全角と半角を混同して使用しないでください")
    U = st.text_input("全体集合を入力してください")
    A = st.text_input("集合Aを入力してください")
    B = st.text_input("集合Bを入力してください")

    zentaisyuugouu = set(U.split()) if U else set()
    syuugoua = set(A.split()) if A else set()
    syuugoub = set(B.split()) if B else set()

    katu = syuugoua & syuugoub   # AかつB
    mataha = syuugoua | syuugoub # AまたはB
    a_barkatu = (zentaisyuugouu - syuugoua) & syuugoub    # AバーかつB
    a_barmataha = (zentaisyuugouu - syuugoua) | syuugoub  # AバーまたはB
    b_barkatu = (zentaisyuugouu - syuugoub) & syuugoua    # AかつBバー
    b_barmataha = (zentaisyuugouu - syuugoub) | syuugoua  # AまたはBバー
    a_barkatub_bar = (zentaisyuugouu - syuugoua) & (zentaisyuugouu - syuugoub)  # AバーかつBバー
    a_barmataha_bar = (zentaisyuugouu - syuugoua) | (zentaisyuugouu - syuugoub)  # AバーまたはBバー

    if katu == set():
        st.write("AかつB:", "空集合")
    else:
        st.write("AかつB:", katu)

    if mataha == set():
        st.write("AまたはB:", "空集合")
    else:
        st.write("AまたはB:", mataha)

    if a_barkatu == set():
        st.write("ＡバーかつＢ:", "空集合")
    else:
        st.write("ＡバーかつＢ:", a_barkatu)

    if a_barmataha == set():
        st.write("ＡバーまたはＢ:", "空集合")
    else:
        st.write("ＡバーまたはＢ:", a_barmataha)

    if b_barkatu == set():
        st.write("ＡかつＢバー:", "空集合")
    else:
        st.write("ＡかつＢバー:", b_barkatu)

    if b_barmataha == set():
        st.write("ＡまたはＢバー:", "空集合")
    else:
        st.write("ＡまたはＢバー:", b_barmataha)

    if a_barkatub_bar == set():
        st.write("ＡバーかつＢバー:", "空集合")
    else:
        st.write("ＡバーかつＢバー:", a_barkatub_bar)

    if a_barmataha_bar == set():
        st.write("ＡバーまたはＢバー:", "空集合")
    else:
        st.write("ＡバーまたはＢバー:", a_barmataha_bar)

    plt.figure(figsize=(8, 6))
    venn2(subsets=(syuugoua, syuugoub), set_labels=('A', 'B'))
    plt.title("venn diagram") 
    plt.tight_layout()

    st.pyplot(plt)
    st.write("このベン図は各集合の中にある要素の数を表しています")

if __name__ == "__main__":
    main()
