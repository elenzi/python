
EUR = 1
GBP = 0.89

amount = int(input("Please enter amount you would like to exchange:"))



if amount <= 0:
    print ("Amount must be >= 0. Please try again.")


else:
    print ("You will recieve: ", amount * GBP)

print("Finished!")
