"""
Initialise counters
Prompt the user for numbers
Read the numbers
while answer is more that 0
if answer equals 0
increment zero by 1
elif answer > than 0 and <= 20
increment number1 by 1
elif answer > than 20 and <= 40
increment number2 by 1
elif answer > than 40 and <= 60
increment number3 by 1
elif answer > than 60 and <= 80
increment number4 by 1
elif answer > than 80 and <= 100
increment number4 by 1
elif answer > than 100 
increment number6 by 1
else
Print “"\n You entered a negative number, here is your output:"”
Prompt the user for another grade
Read the counters
Print out the results
Program finishes


"""


zero=0
number1=0
number2=0
number3=0
number4=0
number5=0
number6=0

answer = int(input("Please tell me some numbers: \n"))

while answer >= 0:
    if answer == 0:
        zero += 1
    elif answer > 0 and answer <= 20:
        number1 += 1
    elif answer > 20 and answer <= 40:
        number2+=1
    elif answer > 40 and answer <= 60:
        number3 += 1
    elif answer > 60 and answer <= 80:
        number4 += 1
    elif answer > 80 and answer <= 100:
        number5 += 1
    elif answer > 100:
        number6 += 1
    answer = int(input("Please tell me some more numbers: \n"))

print("\nYou entered a negative number, here is your output: \n")
print(zero, "numbers equal to 0")
print(number1, "numbers between 1 and 20")
print(number2, "numbers between 21 and 40")
print(number3, "numbers between 41 and 60")
print(number4, "numbers between 61 and 80")
print(number4, "numbers between 81 and 100")
print(number5, "numbers greater than 100")
print(number6, "is less than 0")
print()
print("Finished!")








