"""

Question 4: Write a program that prompts the user for a series of positive integers and, for each of the
numbers entered, uses a while loop to calculate the factorial of that number. The program
should stop when a negative number is entered.

Pseudocode:

prompt user to input an integer as answer "Please tell me some numbers:"
set count as 0
while answer is greater or equal to 0
set fact as 1
set count2 as 1
while count2 is less than or equal to answer
fact equals fact multiplied by count2
increment count2 by 1
print "Factorial of", answer, "is", fact)
prompt user to input an integer as answer "Please tell me some numbers:"
break when user inputs number less than 0 



"""

answer = int(input("Please tell me some numbers: \n"))
count = 0

while answer >= 0:
    fact = 1
    count2 = 1
    while (count2 <= answer):
        fact = fact * count2
        count2 += 1
    print("Factorial of", answer, "is", fact)
    answer = int(input("Please tell me some numbers: \n"))
print("That is not a positive number")





