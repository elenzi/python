"""
Program to write a recursive fucntion
define f of n
if n == 1 return 2
else return n + f(n - 1)
prompt user to enter a number
abc(number)
"""


def f(n):
    if n == 1:
        return 2
    else:
        return n + f(n - 1)

number = int(input("Please enter a number: "))
print(f(number))
