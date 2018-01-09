
"""

prompt user for size of the table
read table
i = 0
while i is greater than table do
j = 0
while j is less than table
print i * j
increment j
print empthy line
increment i
finish

"""

table = int(input("Please nter the size of the table you would like me to generate: "))

i = 1
while i <= table:
    j = 1
    while j <= i:
        print(i * j, " ", end = "")
        j += 1
    print()
    i += 1
