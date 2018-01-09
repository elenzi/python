"""

IF YEAR IS DIVISIBLE BY 4 THEN IT IS A COMMON YEAR
ELSE IF IT IS NOT DIVISBLE BY 100 THEN IT IS A LEAP YEAR
ELSE THERE IS AN ERROR


"""

year = int(input("Please enter a year: "))



if (year % 4 != 0):
     print("It's a common year")
elif (year % 100 != 0):
     print("It's a leap year")
else:
     print("There is an error")



     
