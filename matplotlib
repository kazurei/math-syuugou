import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# ページのタイトル（なくてもいい）
st.title('My first Streamlit app')
# ファイルアップローダーの準備
uploaded_file = st.file_uploader("CSVファイルのアップロード", type="csv")

# uploadファイルが存在するときだけ、csvファイルの読み込みがされる。
if uploaded_file is not None:
    # CSVファイルからデータを抽出
    month, average_temperature = np.loadtxt(uploaded_file, comments='#', delimiter=',', usecols=(0, 1), unpack=True)

    # matplotlibで図を用意する
    fig = plt.figure()
    plt.plot(month, average_temperature, marker='.', markersize=10)
    plt.xlim(0.5, 12.5)
    plt.ylim(0, 40)
    plt.title('Average Temperature at Kyoto in 2018', fontsize=15)
    plt.xlabel('month', fontsize=10)
    plt.ylabel('average temperature (deg)', fontsize=10)

    # streamlit plot
    st.pyplot(fig)
