

"""
set limit as 50 to define how far we go
set count for loop as 1
while count is less than or equal to limit
then print count
then print count squared
if count is divisible by 5 print count
print finished


"""

limit = 50

print("initial value of total is:", limit )

count = 1

while count <= limit:
    print("Number is: ", count)
    print("The square of ", count, "is ", count*count)
    if count % 5 == 0:
        print("number is divible by 5")
    print()
    count += 1

print("Finished")
