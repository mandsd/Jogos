def solve_sudoku(board):
    # Find the next empty cell
    row, col = find_empty_cell(board)

    # If there are no empty cells, the Sudoku is solved
    if row is None:
        return True

    # Try each number from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number in the empty cell
            board[row][col] = num

            # Recursively solve the rest of the board
            if solve_sudoku(board):
                return True

            # If the recursive solve failed, backtrack and try the next number
            board[row][col] = 0

    # If no number can be placed in the empty cell, the Sudoku is unsolvable
    return False


def find_empty_cell(board):
    # Find the next empty cell in the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None


def is_valid(board, row, col, num):
    # Check if the number can be placed in the cell without violating the Sudoku rules

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    if num in [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]:
        return False

    return True


# Example board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku
if solve_sudoku(board):
    # Print the solution
    for row in board:
        print(row)
else:
    print("Sudoku is unsolvable.")
