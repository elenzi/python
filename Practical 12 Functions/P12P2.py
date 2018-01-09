"""

Program to calculate a fib series using a function

Read limit
defin fib as function x
let f_0 = 0
let f_0 = 1
if x equals 1 then
print Series is: f_0
else if x equals 1 then print series is f_0, ", ", f_1, sep = ""
else for i in rage 2 to x
print Series is: f_0, f_1, sep = "", end = ""
fib = b + a Print fib
a = b
b = fib
let b = fib
print()
Prompt the user for a positive number to calculate as limit
if limit is less than or equal to 0 then
print Error
else fib(limit)


"""
f_0 = 0
f_1 = 1
def fib(x):
    if x == 1:
        print("Series is:", f_0)
    elif x == 2:
        print("Series is: ", f_0, ", ", f_1, sep = "")
    else:
        print("Series is: ", f_0, ", ", f_1, sep = "", end = "")
        a = f_0
        b = f_1
        for i in range(2, x):
            fib = b + a
            print(",", fib, end = "")
            a = b
            b = fib
limit = int(input("Enter the number of you want to calculate (a positive number): "))

if limit <= 0:
    print("Error: Number entered was less than or equal to 0")
else:
    fib(limit)

    


