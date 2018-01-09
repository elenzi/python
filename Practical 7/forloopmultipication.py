table = int(input("Please enter the size of the table:\n"))

for i in range(1, table + 1):
    for j in range (1, i +1):
            print(i*j, " ", end = " ")
    print()
