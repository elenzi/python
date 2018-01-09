"""promt user for a positive integer to calculate square root
while number is less than 0
use abs function for square in range abs(number + 1)
if sqaure ** 2 is greater than or equal to abs(number + 1)
set square to equal minus square
print sqaure root of number is square
promt user for a positive integer to calculate square root
else print number, "is not a perfect square."
promt user for a positive integer to calculate square root
when while loop is broke print Your number is not a positive number

"""

number = int(input("Enter the number for which you wish to calculate the cube root:" ))

while number > 0:
    for square in range(abs(number) + 1):
        if square ** 2 >= abs(number):
            break
    if square ** 2 == abs(number):
        if number < 0:
            sqaure = -cube
        print("Square root of", number, "is", square)
        number = int(input("Enter the number for which you wish to calculate the square root:" ))
    else:
        print(number, "is not a perfect cube.")
        number = int(input("Enter the number for which you wish to calculate the square root:" ))

print("Your number is not a positive number.")
    
