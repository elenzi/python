"""
Program to illustrate the use of the else statement on a for loop
for number in range 2 to 20
    for i in range 2 to number
        if number divisble by i equals 0
            print number, "equals", i, "*", number//i)
            break
        else
            print number, "is a prime number"
print Finished!
"""

## Looks for prime numbers in a range of integers
for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            #The break statement is used to break out of the closest enclosing while or for loop
            break
        else:
            # loop fell through without finding a factor
            print(number, "is a prime number")
print("Finished!")
