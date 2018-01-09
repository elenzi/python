
"""Function that returns the factorial of its argument
Assumes that its argument is a non-negative integer
Uses a recursive definition
"""

x = input("Please enter a number: ")
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)
