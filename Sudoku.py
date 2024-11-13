import numpy as np
import random

def generate_board():
    """
    Generates a partially filled Sudoku board using a simple backtracking algorithm.
    This function does not guarantee a unique solution, which is generally hard and computationally intensive to generate.
    """
    board = np.zeros((9, 9), dtype=int)
    for _ in range(15):  # Put 15 numbers on the board to start.
        row, col = np.random.randint(0, 9, size=2)
        num = np.random.randint(1, 10)
        if valid(board, num, (row, col)):  # Re-use the valid function from previous examples.
            board[row, col] = num
    return board

def print_board(board):
    """Prints the Sudoku board."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """Finds an empty space on the board, returns the row and column as a tuple."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


def solve(board):
    """Solves the Sudoku board using a backtracking algorithm."""
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, num, pos):
    """Checks if placing the number 'num' at position 'pos' on the 'board' is valid."""
    row, col = pos
    # Check row and column
    if num in board[row] or num in board[:, col]:
        return False
    # Check box
    box_x = col // 3 * 3
    box_y = row // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_y + i][box_x + j] == num:
                return False
    return True

def main():
    while True:
        board = generate_board()
        print("New Sudoku board:")
        print_board(board)
        input("Press Enter to solve this puzzle...")
        if solve(board):
            print("Solution:")
            print_board(board)
        else:
            print("No solution possible.")
        if input("Generate another puzzle? (yes/no) ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
