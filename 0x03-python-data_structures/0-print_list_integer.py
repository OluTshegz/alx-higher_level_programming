#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        for element in range(len(my_list)):
            print("{:d}".format(my_list[element]))
