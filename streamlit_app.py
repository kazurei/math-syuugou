# Streamlitライブラリをインポート
import streamlit as st
import random

# シンボル
symbols = ["🍒", "🍊", "🍋", "🍉", "🍇", "🔔", "💎", "⭐"]

# スロットを回す
def spin_reel():
    return random.choice(symbols)

# スロットマシンのUI
def slot_machine_ui():
    st.title("Streamlit Slot Machine")

    st.write("Press the button to spin each reel!")

    reels = [st.empty() for _ in range(num_reels)]
    spin_buttons = [st.button(f"Spin Reel {i+1}") for i in range(num_reels)]

    results = []

    for i in range(num_reels):
        if spin_buttons[i]:
            result = spin_reel()
            reels[i].write(result)
            results.append(result)
    
    if all(results) and results.count(results[0]) == len(results):
        st.success("You win!")
    elif results:
        st.error("Try again!")

def main():
    slot_machine_ui()

if __name__ == "__main__":
    num_reels = 3
    main()
