#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
if nb_print is not None:
    print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
if nb_print is not None:
    print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
if nb_print is not None:
    print("nb_print: {:d}".format(nb_print))
