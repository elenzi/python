"""promt user for a positive integer to calculate cube
while number does not equal 0
use abs function for cube in range abs(number + 1)
if cube ** 3 is greater than or equal to abs(number + 1)
set cube to equal minus cube
print Cube root of number is cube
promt user for a positive integer to calculate cube
else print number, "is not a perfect cube."
promt user for a positive integer to calculate cube
when while loop is broke print Your number must not be zero

"""

number = int(input("Enter the number for which you wish to calculate the cube root:" ))

while number != 0:
    # abs() Return the absolute value of a number
    for cube in range(abs(number) + 1):
        if cube ** 3 >= abs(number):
            break
    if cube ** 3 == abs(number):
        if number < 0:
            cube = -cube
        print("Cube root of", number, "is", cube)
        number = int(input("Enter the number for which you wish to calculate the cube root:" ))
    else:
        print(number, "is not a perfect cube.")
        number = int(input("Enter the number for which you wish to calculate the cube root:" ))

print("Your number must not be zero.")
    
