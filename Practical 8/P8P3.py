
"""
prompt user for size of the table
read table
i = 1
while i is less than 20
print i
print empthy line
increment i
finish



"""

table = int(input("Please nter the size of the table you would like me to generate: "))

i = 0
while i <= 20:
        print(i, " ", end = "")
        print(table*i, " ")
        i += 1
