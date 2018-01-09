

"""

set total as 0
set count as 0
set limit as 10000
print the initial value of total
while count is less than or equal to limit
if count is divisible by 3 or 5
count equals total plus count
print total amount


"""

total = 0
limit = 10000

print("initial value of total is:", total)

count = 0

while count <= limit:
     count += 1
     if (count % 3 == 0 or count % 5 == 0):
        total += count
    
print("Total is ", total)
print("Finished")
