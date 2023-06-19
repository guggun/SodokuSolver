import numpy as np

board = [
  [0, 0, 3, 0, 2, 0, 6, 0, 0],
  [9, 0, 0, 3, 0, 5, 0, 0, 1],
  [0, 0, 1, 8, 0, 6, 4, 0, 0],
  [0, 0, 8, 1, 0, 2, 9, 0, 0],
  [7, 0, 0, 0, 0, 0, 0, 0, 8],
  [0, 0, 6, 7, 0, 8, 2, 0, 0],
  [0, 0, 2, 6, 0, 9, 5, 0, 0],
  [8, 0, 0, 2, 0, 3, 0, 0, 9],
  [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

def is_possible(row, column, number):
    global board

    for i in range(0,9):
        if board[row][i] == number:
            return False
    
    for i in range(0,9):
        if board[i][column] == number:
            return False
        
    x = (column // 3) * 3 
    y = (row //3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if board[y+i][x+j] == number:
                return False 
            

    return True

def solve():
    global board
    for row in range (0,9):
        for column in range (0,9):
            if board[row][column] == 0:
                for number in range(1,10):
                    if is_possible(row, column, number):
                        board [row][column] = number
                        solve()
                        board[row][column] = 0

                return
            
    print(np.matrix(board))

solve()