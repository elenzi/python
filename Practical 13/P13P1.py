



"""
Program to print out the largest of two numbers entered by the user
Define function max
If a is greater than b return a
else return b
Prompt the user for two numbers as floats (number 1 and number 2)
set biggest as max of these 2 numbers
print The largest of", number1, "and", number2, "is", biggest
Print Finished


"""
def print_max(a, b):
    if a > b:
        return a
    else:
        return b
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
biggest = max(number1, number2)
print(print_max())
print("The largest of", number1, "and", number2, "is", biggest)
print("Finished!")

print(print_max())
