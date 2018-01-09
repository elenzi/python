"""Program to calculate a factorial using a function
Prompt user for input as a number greater than 0
if x equals 0 return 1
else for x to show recursion
return res x by fact(x-1)
if number greater or equal to zero then
print "The factorial of", number, "is", fact(number0)
else print Error: can only calculate the factorial of a non-negative number
"""

import time



number = int(input("Enter a number greater than 0: "))

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

if number >= 0:
    start = time.time()
    print("The factorial of", number, "is", fact(number))
else:
    print("Error: can only calculate the factorial of a non-negative number")


end = time.time()
print(end - start)

