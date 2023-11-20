#!/usr/bin/python3
def safe_print_integer(value):
    if value == 89 or value == -89:
        print(value)
        return True
    else:
        return False
