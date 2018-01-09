

"""
prompt user to input number as of todays toppings
set factn as 1
if n is < 0 print "It is not possible to have minus toppings."
else for i in range 1 to n plus 1
factn equals factn multiplied by i
print "Factorial of", number, "is", factn" to show how program works

prompt user to input number as of stanard toppings
set factk as 1
if k is < 0 print "It is not possible to have minus toppings."
else for i in range 1 to k plus 1
factk equals factk multiplied by i
print "Factorial of", number, "is", factk" to show how program works

set factnk as 1
if number n and k < 0 
else for i in range 1 to nk plus 1
factnk equals factnk multiplied by i
set below as factk multiplied by factnk
set combo as factn divided by below
print The possible number of toppings today is: ", combo



"""

n = int(input("How many toppings on the pizza today? \n"))

factn = 1
if n < 0:
    print("It is not possible to have minus toppings.")
else:
    for i in range(1, n + 1):
        factn *=i
    print("Factorial of", n, "is", factn)


k = int(input("How many standard toppings on the pizza? \n"))

factk = 1
if k < 0:
    print("It is not possible to have minus toppings.")
else:
    for i in range(1, k + 1):
        factk *=i
    print("Factorial of", k, "is", factk)

factnk = 1
if n < 0 and k < 0:
    print()
else:
    nk = n-k
    for i in range(1, nk + 1):
        factnk *=i

below = factk * factnk
combo = factn / below
print("The possible number of toppings today is: ", combo)




