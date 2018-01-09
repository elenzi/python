"""
Prompt user for integer input
if n equals 0 then print The number 0 is Catalan 1
else if n equals 1 then print The number 1 is Catalan 1
else
set a =1
print a
let i = 1
while i is less than or equal to n-2
let b = 2*(2*(i) + 1) / (i + 2)
print(int(a * b))
a *= b
i+=1

"""


n = int(input("Choose number of catalan numbers : "))

if n == 0:
    print("The number 0 is Catalan 1")
elif n == 1:
    print("The number 1 is Catalan number 1")
else:
    a = 1
    print(a)
    print(a)
    i = 1
    while i <= n-2:
        b = 2*(2*(i) + 1) / (i + 2)
        print(int(a * b))
        a *= b
        i+=1
