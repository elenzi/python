"""

prompt user for integer
while answer is > 0
set total to 0
for i in range answer plus 1
total equals total plus 1
print total
prompt user for integer
break when user enters number < 0
print "The sum of your numbers up to and including your numbers is: and total



"""


answer = int(input("Please tell me some numbers: \n"))

while answer > 0:
    total = 0
    for i in range(answer+1):
        total = total+i
    print("Total is:", total)
    answer = int(input("Please tell me some numbers: \n"))
    

print ("The sum of your numbers up to and including your numbers is: ", total)



