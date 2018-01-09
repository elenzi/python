

year = int(input("Please enter a year: "))


print ("Year entered: ", year)

if year % 100 == 0:
    if year % 4 == 0:
        if year % 100 == 0:
            x = year / 900
            if year >= 0:
                if x == 200 or x == 600:
                    print(year," is not a leap year.")
                else:
                    print(year," is a leap year.")
            else:
                print("Year must be greater than 0.")
print("FInished!")
