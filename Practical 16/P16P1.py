"""
Program to write a recursive fucntion
define a of x to print function 
for i in range 1 to x + 1
print(f(i), end =" ")
f(x)
define f of n
if n == 1 return 2
else return n + f(n - 1)
prompt user to enter a number
a(number)
"""

def a(x):
    for i in range(1, x+1):
        print(function(i), end =" ")
    function(x)


def function(n):
    if n == 1:
        return 2
    else:
        return 2 * f(n - 1)

number = int(input("Please enter a number: "))
a(number)
