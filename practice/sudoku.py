import random

def create_board():
    board = [[0]*9 for i in range(9)]
    return board

def fill_board(board):
    numbers = [1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
        if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
            return False
    return True

def remove_numbers(board, difficulty):
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)
    for row, col in cells:
        temp = board[row][col]
        board[row][col] = 0
        temp_board = [row[:] for row in board]
        solutions = []
        solve(temp_board, solutions)
        if len(solutions) != 1:
            board[row][col] = temp
        if difficulty == 1 and len(cells) > 30:
            cells.remove((row, col))
        elif difficulty == 2 and len(cells) > 40:
            cells.remove((row, col))
        elif difficulty == 3 and len(cells) > 50:
            cells.remove((row, col))
        else:
            break

def solve(board, solutions):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board, solutions):
                            solutions.append([row[:] for row in board])
                            board[i][j] = 0
                        else:
                            board[i][j] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

board = create_board()
fill_board(board)
remove_numbers(board, 1)
print_board(board)
