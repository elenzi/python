"""
Prompt user to Enter a string and press enter to Finish
while string is not empty
set vowels to equal 0
for i in string
if i = a, e, i , o or u
set vowels to equal vowels to vowels plus 1
Prompt user to Enter a string and press enter to Finish
break while loop when user presses enter
"""



string = input("Enter a string (Press 'Enter' to finish): ")


while string != "":
    vowels=0
    for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    print("Number of vowels:", vowels)
    string = input("Enter a string (Press 'Enter' to finish): ")

print("You need to enter a word.")

