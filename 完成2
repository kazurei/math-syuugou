import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def main():
    st.title("集合を求める")

    # 入力フォーム
    st.write("全角と半角を混同して使用しないでください")
    U = st.text_input("全体集合を入力してください")
    A = st.text_input("集合Aを入力してください")
    B = st.text_input("集合Bを入力してください")

    # 空の場合は空集合として扱う
    zentaisyuugouu = set(U.split()) if U else set()
    syuugoua = set(A.split()) if A else set()
    syuugoub = set(B.split()) if B else set()

    # 集合演算
    katu = syuugoua & syuugoub   # AかつB
    mataha = syuugoua | syuugoub # AまたはB
    a_barkatu = (zentaisyuugouu - syuugoua) & syuugoub    # AバーかつB
    a_barmataha = (zentaisyuugouu - syuugoua) | syuugoub  # AバーまたはB
    b_barkatu = (zentaisyuugouu - syuugoub) & syuugoua    # AかつBバー
    b_barmataha = (zentaisyuugouu - syuugoub) | syuugoua  # AまたはBバー
    a_barkatub_bar = (zentaisyuugouu - syuugoua) & (zentaisyuugouu - syuugoub)  # AバーかつBバー
    a_barmataha_bar = (zentaisyuugouu - syuugoua) | (zentaisyuugouu - syuugoub)  # AバーまたはBバー

    # 結果の表示
    z = ("AかつB:", (katu))
    x = ("AまたはB:", mataha)
    c = ("ＡバーかつＢ:", a_barkatu)
    v = ("ＡバーまたはＢ:", a_barmataha)
    n = ("ＡかつＢバー:", b_barkatu)
    m = ("ＡまたはＢバー:", b_barmataha)
    k = ("ＡバーかつＢバー:", a_barkatub_bar)
    l = ("ＡバーまたはＢバー:", a_barmataha_bar)
    if katu == set() :
        z = st.write("AかつB:","空集合")
    if mataha == set() :
        x = st.write("AまたはB:","空集合")
    if a_barkatu == set() :
        c = st.write("ＡバーかつＢ:","空集合")
    if a_barmataha  == set() :
        v = st.write("ＡバーまたはＢ:","空集合")
    if b_barkatu == set() :
        n = st.write("ＡかつＢバー:","空集合")
    if b_barmataha == set() :
        m = st.write("ＡまたはＢバー:","空集合")
    if a_barkatub_bar == set() :
        k = st.write("ＡバーかつＢバー:","空集合")
    if a_barmataha_bar == set() :
        l = st.write("ＡバーまたはＢバー:","空集合")
    st.write(z)
    st.write(x)
    st.write(c)
    st.write(n)
    st.write(m)
    st.write(k)
    st.write(l)
    # ベン図の作成と表示
    plt.figure(figsize=(8, 6))
    venn2(subsets=(syuugoua, syuugoub), set_labels=('A', 'B'))
    plt.title("venn diagram")  # ベン図のタイトルを設定
    plt.tight_layout()

    # ベン図を画像として表示
    st.pyplot(plt)
    st.write("このベン図は各集合の中にある要素の数を表しています")

if __name__ == "__main__":
    main()
