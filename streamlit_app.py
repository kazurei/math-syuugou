# Streamlitライブラリをインポート
import streamlit as st
import random

# シンボル
symbols = ["🍒", "🍊", "🍋", "🍉", "🍇", "🔔", "💎", "⭐"]

# リールの数
num_reels = 3

# スロットの初期設定
def initialize_slot_machine():
    return [random.choice(symbols) for _ in range(num_reels)]

# スロットを回す
def spin_slot_machine():
    return [random.choice(symbols) for _ in range(num_reels)]

# スロットマシンのUI
def slot_machine_ui():
    st.title("Streamlit Slot Machine")

    st.write("Press the button to spin the reels!")

    if st.button("Spin"):
        result = spin_slot_machine()
        st.write(result)
        if result.count(result[0]) == len(result):
            st.success("You win!")
        else:
            st.error("Try again!")

def main():
    slot_machine_ui()

if __name__ == "__main__":
    main()
