#!/usr/bin/python3
for tens_digit in range(10):
    for units_digit in range(10):
        if tens_digit == 8 and units_digit == 9:
            print("{}{}".format(tens_digit, units_digit))
        elif tens_digit < units_digit and tens_digit != units_digit:
            print("{}{}".format(tens_digit, units_digit), end=", ")
