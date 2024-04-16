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

    results = []

    for i in range(num_reels):
        if st.button(f"Spin Reel {i+1}"):
            result = spin_reel()
            results.append(result)
            st.write(f"Reel {i+1} Result: {result}")

    if results:
        if len(set(results)) == 1:
            st.success("You win!")
        else:
            st.error("Try again!")

def main():
    slot_machine_ui()

if __name__ == "__main__":
    num_reels = 3
    main()
