

year = int(input("Please enter a year: "))


print ("Year entered: ", year)

x = 900 // 200
y = 900 // 600

if year >= 0:
    if (year % 4 ==0 not % 100 == 0) and year != x and year != y:
        print(year," is a leap year.")
    else:
        print(year," is not a leap year.")
else:
    print("Year must be greater than 0.")

print("FInished!")
