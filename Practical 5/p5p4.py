#Programming Practical 5  by Elena Lanigan 5/10/17




amount = int(input("Please tell me a number and I will repeat what you say:  "))


if amount == 0:
    print ("Your number is equal to 0.")

elif amount > 0 and amount <= 20:
    print ("Your number is ", amount, "and it is greater than 0 and less than or equal to 20")

elif amount > 20 and amount <= 40:
    print ("Your number is ", amount, "and it is greater than 20 and less than or equal to 40")

elif amount > 40 and amount <= 60:
    print ("Your number is ", amount, "and it is greater than 40 and less than or equal to 60")

elif amount > 60 and amount <= 80:
    print ("Your number is ", amount, "and it is greater than 60 and less than or equal to 80")

elif amount > 80 and amount <= 100:
    print ("Your number is ", amount, "and it is greater than 80 and less than or equal to 100")

else:
    print ("Your number is greater than 100")
