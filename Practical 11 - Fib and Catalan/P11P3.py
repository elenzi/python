
"""
Prompt the user for the number of terms to calculate
Read limit
while number > 0
if limit == 1 then print Error: Number entered was less than or equal to 0
else if limit == 2 then print Series is: ", f_0, ", ", f_1, sep = ""
else print Series is: ", f_0, ", ", f_1, sep = "", end = ""
let a = 0
let b = 1
for i in rage 2 to number
fib = b + a Print fib
a = b
b = fib
let b = fib
print()
Prompt the user for the number of terms to calculate
Print Finished



"""
f_0 = 0
f_1 = 1
number = int(input("Please enter a number: "))

while number > 0:
    if number <= 0:
        print("Error: Number entered was less than or equal to 0")
    elif number == 1:
        print("Series is:", f_0)
    elif number == 2:
        print("Series is: ", f_0, ", ", f_1, sep = "")
    else:
        #sep to separate the arguments, and end after the last argument.
        print("Series is: ", f_0, ", ", f_1, sep = "", end = "")
        a = f_0
        b = f_1
        for i in range(2, number):
            fib = b + a
            print(",", fib, end = "")
            a = b
            b = fib
    print()
    number = int(input("Please enter a number: "))
print()
print("Finished")
