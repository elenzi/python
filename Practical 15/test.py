def f(n):
    if n == 2:
        return 2
    else:
        return n + f(n - 1) + 2**n-1
        for i in range(1, n+1):
            print(f(i), end =" ")
        f(n)

number = int(input("Please enter a number: "))
print(f(number), end =" ")
