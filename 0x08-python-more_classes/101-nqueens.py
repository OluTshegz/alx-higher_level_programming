#!/usr/bin/python3
"""ALX_Holberton Software Engineering Curriculum
    Python Higher-Level Programming
    (0X08-python-more_classes) Task 10. - N Queens
    The N queens puzzle is the challenge of placing
    N non-attacking queens on an NxN chessboard.
    Write a program that solves the N queens problem.
    Resource: Wikipedia - Queen, Backtracking
    Usage: nqueens N; where: nqueens is name of the file, N is the number
"""

import sys


def is_valid(board, row, col, N):
    # Check if the current position is valid
    for i in range(row):
        if board[i] == col or \
           board[i] == col - (row - i) or \
           board[i] == col + (row - i):
            return False
    return True


def solve_nqueens(board, row, N):
    # Base case: all queens are placed
    if row == N:
        print_solution(board, N)
        return

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_valid(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def print_solution(board, N):
    # Print the positions of the queens on the chessboard
    for i in range(N):
        row = ["." for _ in range(N)]
        row[board[i]] = "Q"
        print(" ".join(row))
    print()


def main():
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
