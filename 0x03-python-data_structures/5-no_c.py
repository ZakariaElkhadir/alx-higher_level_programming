#!/usr/bin/python3
def no_c(my_string):
    c_string = ''

    for i in my_string:
        if i == 'c' or i == 'C':
            pass
        else:
            c_string += i
    return c_string
