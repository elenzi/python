"""
Program to write a recursive fucntion
define abc of x to print function f
for i in range 1 to x - 1
print(f(i), end =" ")
f(x)
define f of n
if n == 1 return 2
else return n + f(n - 1) + 13 * f(n-1)
prompt user to enter a number
abc(number)
"""

def f(n):
    if n == 1:
        return 2
    else:
        return n + f(n - 1) + 13 * f(n-1)

number = int(input("Please enter a number: "))
print(f(number))
