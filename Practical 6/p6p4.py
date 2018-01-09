
""""
store password as "elena"
input "Please enter your password: "
if answer equals elens print "That is correct. You may successfully enter."
else "You have attempted your password 3 times. Come back when you remember"
repeat if/else statement twice "You have attempted your password 3 times. Come back when you remember"x
else


"""

password = "elena"

answer2 = input("Please enter your password: ")

if answer2 == "elena":
    print("That is correct. You may successfully enter.")
else:
    answer2 = input("That is incorrect. Please enter your password again: ")
    
    if answer2 == "elena":
        print("That is correct. You may successfully enter.")
    else:
        answer2 = input("That is incorrect. Please enter your password again: ")

        if answer2 == "elena":
            print("That is correct. You may successfully enter.")

        else:
            print("You have attempted your password 3 times. Come back when you remember")


    







