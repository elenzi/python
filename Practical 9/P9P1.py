"""


1. Write a program that prompts the user for an integer and uses a while loop to calculate the
sum of the integers up to and including that number.
Save this program as p9p1.py.


Pcode:
set total as 0
set count as 0
prompt user for integer
total is the sum of total + count
count equals count plus 1
print "The sum of the integers up to your number and your number is: ", total

"""


integer = int(input("Please enter a positive integer: \n"))


count = 0
total = 0



if integer <= 0:
    print("That is not a positive integer.")
else:
    while count <= integer:
        total = total + count
        count = count + 1
    
    print("The sum of the integers up to your number and your number is: ", total)

    
