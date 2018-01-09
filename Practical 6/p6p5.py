

#set password as "elena"
#start program with input equals answer
#if answer equals elena print "you may enter :)"
#else print "Please enter your password: "
#set answer2, answer3, answer4 as new inputs
#if answer2,3,4 equals password print "You may enter"
#else print "access denied"



password = "elena"



answer = input("Please enter your password: ")


if answer == "elena":
    print("You may enter :)")

else:
    print("That is incorrect. Please enter password 3 times")
    

    answer2 = input("Please enter your password again: ")
    answer3 = input("Please enter your password again: ")
    answer4 = input("Please enter your password again: ")

    if answer2 == "elena" and answer3 == "elena" and answer4 == "elena":
        print("You may enter")

    else:
        print("Access denied.")

    


