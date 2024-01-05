#!/usr/bin/bash
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element == row[-1]:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()
