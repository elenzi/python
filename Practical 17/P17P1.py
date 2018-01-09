"""
define function findDivisors(num)
initialise divisors (1, num)
set variable nvar = int(num // 2)
for i in range 2, nvar + 1 do
if num divisible by i then
return divisors
Prompt the user for a positive integer
If the number entered is not positive then
print out an error message
else find the common divisors
print out the common divisors

Revise the solution on Pages 14–17 of the slides to include these optimisations.


"""

def findDivisors(num):
	"""Finds the common divisors 
	Returns a tuple containing the common divisors of num"""
    divisors = (1, num)
    #// divide with integral result (discard remainder)
    nvar = int(num // 2)
    for i in range(2, nvar + 1):
        if num % i == 0:
        	#To denote the singleton tuple containing the value 1, we write (1,)
            divisors += (i,)
    return divisors


number1 = int(input("Enter another positive integer: "))
if number1 <= 0:
    print("Numbers should be > 0.")
else:
	#call function #finddevisors
    divisors = findDivisors(number1)
    #sums them and prints the total
    total = 0
    for d in divisors:
        total += d
     print("The common divisors of", number1, "are:", divisors)


