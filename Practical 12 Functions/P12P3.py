

"""

Program to calculate approximate square root
define tolerance
if number is less than or equal to 0 then
print("Error: Number entered was less than or equal to 0")
else tolerence(number)

(Exhaustive Enumeration is a technique of searching for a
solution to a problem)

# Uses exhaustive enumeration to find an approximate solution

"""

def tolerence(x):
    epsilon = 0.01
    step = epsilon ** 2
    numGuesses = 0
    root = 0.0
    while abs(number - root ** 2) >= epsilon and root ** 2 <= number:
        root += step
        numGuesses += 1
        if numGuesses % 100000 == 0:
            print("Still running. Number of guesses:", numGuesses)
            print("Number of guesses:", numGuesses)
    if abs(number - root ** 2) < epsilon:
        print("The approximate square root of", number, "is", root)
    else:
        print("Failed to find a square root of", number)
        print("Finished!")

number = float(input("Enter the number for which you wish to calculate the square root: "))

if number <= 0:
    print("Error: Number entered was less than or equal to 0")
else:
    tolerence(number)
