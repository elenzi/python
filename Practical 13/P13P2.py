



"""
Program to print out the largest of two numbers entered by the user
Define function max
If a is greater than b return a
else return b
Prompt the user for two numbers as floats (number 1 and number 2)
print The largest of, number1 and number2 is max of number 1 and number 2
Print Finished


"""
def print_max():

    def max(a, b):
        if a > b:
            return a
        else:
            return b
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    print("The largest of", number1, "and", number2, "is", max(number1, number2))
    return

print(print_max)

