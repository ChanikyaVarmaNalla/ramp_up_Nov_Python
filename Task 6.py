def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or \
                board[i][col] == num or \
                board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for num in map(str, range(1, 10)):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", ".", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

if solve_sudoku(sudoku):
    for single_row in sudoku:
        print(single_row)
else:
    print("No solution exists.")
