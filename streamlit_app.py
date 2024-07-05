import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import numpy as np

def main():
    st.title("集合を求める")

    # 入力フォーム
    U = st.text_input("全体集合を入力してください")
    A = st.text_input("集合Aを入力してください")
    B = st.text_input("集合Bを入力してください")

    # 空の場合は空集合として扱う
    zentaisyuugouu = set(U.split()) if U else set()
    syuugoua = set(A.split()) if A else set()
    syuugoub = set(B.split()) if B else set()

    # 結果の表示
    st.write("全体集合:", zentaisyuugouu)
    st.write("集合A:", syuugoua)
    st.write("集合B:", syuugoub)

    # ベン図の作成と表示
    if A and B:  # 集合Aと集合Bが入力されている場合のみベン図を描画する
        plt.figure(figsize=(8, 6))
        v = venn2(subsets=(len(syuugoua - syuugoua & syuugoub), len(syuugoub - syuugoua & syuugoub), len(syuugoua & syuugoub)), set_labels=('A', 'B'))
        venn2_circles(subsets=(len(syuugoua), len(syuugoub), len(syuugoua & syuugoub)))
        plt.title("venn diagram")  # ベン図のタイトルを設定

        # 注釈を追加
        plt.annotate('AandB', xy=v.get_label_by_id('10').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
                     ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
        plt.annotate('AorB', xy=v.get_label_by_id('01').get_position() - np.array([0, 0.05]), xytext=(70,-70),
                     ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.5',color='gray'))

        plt.tight_layout()

        # ベン図を画像として表示
        st.pyplot(plt)

if __name__ == "__main__":
    main()
