
"""

Prompt the user for the number of terms to calculate
Read limit
if limit == 1 then print Error: Number entered was less than or equal to 0
else if limit == 2 then print Series is: ", f_0, ", ", f_1, sep = ""
else print Series is: ", f_0, ", ", f_1, sep = "", end = ""
let a = 0
let b = 1
let i = 2
while i < limit do
fib = b + a Print fib
let a = b
let b = fib
Increment i

"""

f_0 = 0
f_1 = 1
limit = int(input("Enter the number of terms you want to calculate (an int > 0): "))
if limit <= 0:
    print("Error: Number entered was less than or equal to 0")
elif limit == 1:
    print("Series is:", f_0)
elif limit == 2:
    print("Series is: ", f_0, ", ", f_1, sep = "")
else:
    print("Series is: ", f_0, ", ", f_1, sep = "", end = "")
    a = f_0
    b = f_1
    i = 2
    while i < limit:
        fib = b + a
        print(",", fib, end = "")
        a = b
        b = fib
        i += 1
print()
print("Finished!")
