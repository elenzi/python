
"""

Prompt the user for a positive number 
Read the number
while number entered is less than zero run the loop
if number divisble by 2, 3, 5, or 7
print "number is disible by"
else print "I cannot accept a negative number. Goodbye."
Program finishes


"""



number = (int(input("Please enter a positive number and I will tell you what it is divisible by: ")))
print()


while number >= 0:
    if number % 2 == 0:
        print(number, "is divisible by 2")
        print()
    if number % 3 == 0:
        print(number, "is divisible by 3")
        print()
    if number % 5 == 0:
        print(number, "is divisble by 5")
        print()
    if number % 7 == 0:
        print(number, "is divisble by 7")
        print()
    number = (int(input("Please enter another number: ")))
    print()
else:
    print("I cannot accept a negative number. Goodbye.")
    










      
