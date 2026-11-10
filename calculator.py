"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    return b / a

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "Cannot calculate logarithm of non-positive numbers"

def exponent(a, b):
    return a ** b

def log(a, b): # use math library + raise ValueError
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b


# print(div(13,0))
