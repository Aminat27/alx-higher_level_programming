#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
message = "Last digit of " + f"{number} " + "is " + f"{last_digit}"
if last_digit > 5:
    print(message + " and is greater than 5")
elif last_digit == 0:
    print(message + " and is zero")
elif {last_digit > 6 and not 0}:
    print(message + " and is less than 6 and not 0")
