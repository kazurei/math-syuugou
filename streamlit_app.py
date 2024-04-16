# Streamlitライブラリをインポート
import streamlit as st
import numpy as np
import time

# ゲームの設定
ROWS = 20
COLS = 10
BLOCK_SIZE = 30
FPS = 5

# テトリスのブロック
blocks = [
    np.array([[1, 1], [1, 1]]),  # 四角
    np.array([[1, 1, 1, 1]]),    # 棒
    np.array([[1, 1, 0], [0, 1, 1]]),  # Z
    np.array([[0, 1, 1], [1, 1, 0]]),  # 反対Z
    np.array([[0, 1, 0], [1, 1, 1]]),  # L
    np.array([[1, 0, 0], [1, 1, 1]]),  # 反対L
    np.array([[1, 1, 1], [0, 1, 0]])   # T
]

def update_board(board, block, pos):
    rows, cols = block.shape
    for r in range(rows):
        for c in range(cols):
            if block[r, c] == 1:
                board[pos[0] + r, pos[1] + c] = 1
    return board

def create_new_block():
    return blocks[np.random.randint(len(blocks))]

def main():
    st.title("Streamlit Tetris")

    # 初期化
    board = np.zeros((ROWS, COLS))
    current_block = create_new_block()
    block_pos = [0, COLS // 2 - current_block.shape[1] // 2]

    while True:
        st.write("Score: 0")
        st.write("Use Arrow Keys to Move the Block")

        # ボードの描画
        for row in range(ROWS):
            for col in range(COLS):
                if board[row, col] == 1:
                    st.markdown('<div style="background-color: blue; width: {0}px; height: {0}px;"></div>'.format(BLOCK_SIZE), unsafe_allow_html=True)
                else:
                    st.markdown('<div style="background-color: white; width: {0}px; height: {0}px;"></div>'.format(BLOCK_SIZE), unsafe_allow_html=True)

        # ブロックの描画
        for row in range(current_block.shape[0]):
            for col in range(current_block.shape[1]):
                if current_block[row, col] == 1:
                    st.markdown('<div style="background-color: red; width: {0}px; height: {0}px;"></div>'.format(BLOCK_SIZE), unsafe_allow_html=True)

        # 一時停止して次のアクションを待機
        time.sleep(1/FPS)

        # ブロックの移動
        block_pos[0] += 1

        # ボードの更新
        board = update_board(board, current_block, block_pos)

        # 新しいブロックの生成
        if block_pos[0] + current_block.shape[0] >= ROWS:
            block_pos = [0, COLS // 2 - current_block.shape[1] // 2]
            current_block = create_new_block()

if __name__ == "__main__":
    main()
