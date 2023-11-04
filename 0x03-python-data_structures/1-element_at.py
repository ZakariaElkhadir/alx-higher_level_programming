#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > my_list[-1]:
        return None
    for idx in my_list:
        return my_list[idx]
