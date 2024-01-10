#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    top = 0
    bottom = 0
    for x in my_list:
        top += x[0] * x[1]
        bottom += x[1]
    return (top / bottom)
