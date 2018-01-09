
"""
Prompt user for input as n
set fact as 1
if n is less than 0
for i in range to start at -1, end at n-1 and step at -1
print Factorial of", n, "is", fact
if n is greater than 0
for i in range to start at 1, end at n+1 and step at +1
print Factorial of", n, "is", fact
else if number equals 0 print i need a number that is not zero

"""

n = int(input("Please enter a negative number and I will give you the factorial? \n"))


fact = 1
if n < 0:
    for i in range(-1, n-1, - 1):
        fact *=i
    print("Factorial of", n, "is", fact)
elif n > 0:
    for i in range(1, n+1, + 1):
        fact *=i
    print("Factorial of", n, "is", fact)
else:
    print("I need a number that is not zero")


