num = int(input('Enter a positive number: '))

# Ensure that the number is positive; otherwise, exit.
if num < 0:
    print('You entered a negative number')
    exit()

for i in range(1, num + 1):
    # Finding the factors of i
    factors = []
    for j in range(1, i):
        if i%j == 0:
            # If we are here, then it means that
            # j is a factor of i.
            factors.append(j)

    # Sum factors of i
    sum_of_factors = sum(factors)

    # Check if the sum of those factors equal the number.
    if sum_of_factors == i:
        # We've found a perfect number!!
        print(i, 'is a perfect number, with factors', factors)
    else:
        # print(i, 'is not a perfect number, with factors', factors)
        pass