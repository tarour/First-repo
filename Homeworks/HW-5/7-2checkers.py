import numpy as np

def checkerboard():

    board = np.zeros((8,8))

    board[0::2, 0::2] = 1
    board[1::2, 1::2] = 1

    return board

print(checkerboard())






