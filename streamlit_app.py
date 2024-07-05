import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def main():
    st.title("集合を求める")

    # 入力フォーム
    U = st.text_input("全体集合を入力してください")
    A = st.text_input("集合Aを入力してください")
    B = st.text_input("集合Bを入力してください")

    # 入力された文字列を空白で分割して集合に変換
    zentaisyuugouu = set(U.split())
    syuugoua = set(A.split())
    syuugoub = set(B.split())

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
    st.write("AかつB:", katu)
    st.write("AまたはB:", mataha)
    st.write("ＡバーかつＢ:", a_barkatu)
    st.write("ＡバーまたはＢ:", a_barmataha)
    st.write("ＡかつＢバー:", b_barkatu)
    st.write("ＡまたはＢバー:", b_barmataha)
    st.write("ＡバーかつＢバー:", a_barkatub_bar)
    st.write("ＡバーまたはＢバー:", a_barmataha_bar)

    # ベン図の作成と表示
    plt.figure(figsize=(8, 6))
    venn2(subsets=(len(syuugoua - syuugoua & syuugoub), len(syuugoub - syuugoua & syuugoub), len(syuugoua & syuugoub)), set_labels=('A', 'B'))
    plt.title("venn diagram")  # ベン図のタイトルを設定
    plt.tight_layout()

    # ベン図を画像として表示
    st.pyplot(plt)

if __name__ == "__main__":
    main()
