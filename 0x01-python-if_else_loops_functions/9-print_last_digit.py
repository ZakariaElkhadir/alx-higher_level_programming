#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    elif number < 0:
         last_digit = (-anumber % 10)
    return last_digit
