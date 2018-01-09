"""
define function findDivisors1(num1)
initialise divisors (1, num1)
set variable nvar = int(num1 // 2)
for i in range 2, nvar1 + 1 do
if num1 divisible by i then
return divisors
define function findDivisors2(num2)
initialise divisors (1, num2)
set variable nvar2 = int(num2 // 2)
for i in range 2, nvar2 + 1 do
if num2 divisible by i then
return divisors
Prompt the user for two positive integers
If the numbers entered are not positive then
print out an error message
else find the common divisors
print out the common divisors

"""

def findDivisors1(num1):
    divisors = (1, num1)
    nvar = int(num1 // 2) #// divide with integral result (discard remainder)
    for i in range(2, nvar + 1):
        if num1 % i == 0:
            divisors += (i,) #To denote the singleton tuple containing the value 1, we write (1,)

    return divisors

def findDivisors2(num2):
    divisors = (1, num2)
    nvar2 = int(num2 // 2)
    for i in range(2, nvar2 + 1):
        if num2 % i == 0:
            divisors += (i,)
    return divisors


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 <= 0:
    print("Numbers should be > 0.")
else:
    divisors = findDivisors1(number1)
    print("The common divisors of", number1, "are:", divisors)
    total = 0
    for d in divisors:
        total += d

if number2 <= 0:
    print("Numbers should be > 0.")
else:
    divisors = findDivisors2(number2)
    print("The common divisors of", number2, "are:", divisors)
    total = 0
    for d in divisors:
        total += d
