#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
str = "Last digit of"
if (number >= 0):
    if (lastDigit > 5):
        print(f"{str} {number:d} is {lastDigit:d}" + " and is greater than 5")
    elif (lastDigit == 0):
        print(f"{str} {number:d} is {lastDigit:d}" + " and is 0")
    elif (lastDigit < 6 and lastDigit != 0):
        print(f"{str} {number:d} is {lastDigit}" + " and is less than 6 and not 0")
elif (number < 0):

    if (number < 0 or lastDigit < 6 and lastDigit != 0):
    
        print(f"{str} {number:d} is {lastDigit*-1}" + " and is less than 6 and not 0")
