#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = [x for x in my_list]
    copy_list[idx] = element;
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        return copy_list
