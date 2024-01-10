#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        num = 0
        for i in set(my_list):
            num += i
        return num
