#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    elif a_dictionary is not None:
        sort_score = sorted(a_dictionary.values())
        x = sort_score[-1]
        for key, value in a_dictionary.items():
            if value == x:
                return key
    else:
        return None
