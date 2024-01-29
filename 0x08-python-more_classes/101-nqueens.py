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


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.pathexit(1)

    try:
        N = int(sys.argv[1])
        if (N < 4):
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main__":
    main()
