#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    
    cp = my_list.copy()
    if idx < 0:
        return cp
    if idx >= len(my_list):
        return cp
    cp[idx] = element
    return cp
