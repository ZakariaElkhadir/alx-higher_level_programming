#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#positive number % 10
#negativ number abs(num) % 10
str1 = "Last digit of"
str2 = "and not 0"
lastDigit = abs(number) % 10

if (lastDigit > 5):
    print(str1 + f"{number:5} is {lastDigit:d}" + " and is greater than 5")
elif (lastDigit == 0):
    print(str1 + f"{number:d} is {lastDigit:d}" + "and is 0")
elif (lastDigit < 6 and lastDigit != 0):
    print(str1 + f"{number:d} is {lastDigit:d}" + "and is less than 6 and not 0")
