

C_0 = 0
C_1 = 1
n = int(input("Please enter a number: "))


while n > 0:
        n2 = n * 2
        fact2n = 1
        if n < 0:
            print("It is not possible to have a minus number.")
        else:
            for i in range(1, n2 + 1):
                fact2n *=i
            print("Factorial of", n2, "is", fact2n)               
            factn = 1
            if n < 0:
                    print("It is not possible to have a minus number.")
            else:
                for i in range(1, n + 1):
                    factn *=i
                print("Factorial of", n, "is", factn)                        
                n1 = n + 1
                factn1 = 1
                if n < 0:
                    print("It is not possible to have a minus number.")
                else:
                    for i in range(1, n1 + 1):
                        factn1 *=i
                    print("Factorial of", n1, "is", factn1)
                    n1n = factn1*factn
                    cn = fact2n / n1n
                    print(int(cn))
                    break

print("Series is: ", C_0, ", ", C_1, sep = "", end = "")
a = C_0
b = C_1
for i in range(1, n-2):
        cat = 2*(2*(i) + 1) / (i + 2)
        print(",", cat, end = "")
        a *= b
        i+=1


print("Finished!")
                

