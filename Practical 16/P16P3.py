"""
Recursive function that takes as its single argument an integer ≥ 1 
and prints out that number of terms from the above series.

Prompt user for a number
If number is less than 0, exit
wrap i for loop to find factors of i
check if j is factor of i
factors.append(j)
sum_of_factors equals sum(factors)
if sum_of_factors equals i then
print i is a perfect number with factors
"""


number = int(input('Enter a positive number: '))

if number < 0:
    print('You entered a negative number')
    exit()

for i in range(1, number + 1):
    factors = [] #[] is an empty list
    for j in range(1, i):
        if i%j == 0:
        	#Add an item to the end of the list; equivalent to a[len(a):] = [x].
            factors.append(j)
    sum_of_factors = sum(factors)
    if sum_of_factors == i:
        print(i, 'is a perfect number, with factors', factors)
 
