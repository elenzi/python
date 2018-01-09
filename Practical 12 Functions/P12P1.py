
"""
Program to calculate a factorial using a function
Prompt user for input as a number greater than 0
define function as fact
set res as 1
for i in range to start at -1, x+1
res equals res by i
return res
if number greater or equal to zero then
print "The factorial of", number, "is", fact(number0
else print Error: can only calculate the factorial of a non-negative number



"""

import time

number = int(input("Enter a number greater than 0: "))

def fact(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res
    
while number >0:
    if number >= 0:
        start = time.time()
        print("The factorial of", number, "is", fact(number))
    else:
        print("Error: can only calculate the factorial of a non-negative number")
    number = int(input("Enter a number greater than 0: "))

end = time.time()
print(end - start)

