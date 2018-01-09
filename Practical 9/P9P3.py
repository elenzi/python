"""
3. Write a program that prompts the user for a positive integer and uses a for loop to calculate
the factorial of that number.

prompt user to input number as positive integer
set fact as 1
if number is < 0 print "Your number is not a positive number."
else for i in range 1 to number plus 1
fact equals fact multiplied by i
print "Factorial of", number, "is", fact


"""

number = int(input("Please input a postive number: "))
fact = 1

if number < 0:
    print("Your number is not a positive number.")
else:
    for i in range(1, number + 1):
        fact *=i
    print("Factorial of", number, "is", fact)
             

            
