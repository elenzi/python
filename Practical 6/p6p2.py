

#input first number and store in first
#input second number and store in second
#input third number and store in third
#check whether first second third are odd or the highest
#assign 0 to highest and change once each number is input





first = int(input("Please give me your first number: "))
second = int(input("Please give me your second number: "))
third = int(input("Please give me your second number: "))
highest = 0



if first % 2 == 1:
    highest = first

if second % 2 == 1 and second > highest:
    highest = second

if third % 2 == 1 and third > highest:
    highest = third
    
if highest == 0:
        print("None of these are odd, please try again.")

else:
    print("The highest odd number is ", highest)






