# Streamlitライブラリをインポート
import streamlit as st
import random

# シンボル
symbols = ["🍒", "🍊", "🍋", "🍉", "🍇", "🔔", "💎", "⭐"]

# スロットの初期設定
def initialize_slot_machine():
    return [random.choice(symbols) for _ in range(num_reels)]

# スロットを回す
def spin_reel():
    return random.choice(symbols)

# スロットマシンのUI
def slot_machine_ui():
    st.title("Streamlit Slot Machine")

    st.write("Press the button to spin each reel!")

    reels = [st.empty() for _ in range(num_reels)]
    spin_buttons = [st.button(f"Spin Reel {i+1}") for i in range(num_reels)]

    if all(spin_buttons):
        results = [spin_reel() for _ in range(num_reels)]
        for i in range(num_reels):
            reels[i].write(results[i])
        
        if results.count(results[0]) == len(results):
            st.success("You win!")
        else:
            st.error("Try again!")

def main():
    slot_machine_ui()

if __name__ == "__main__":
    num_reels = 3
    main()
