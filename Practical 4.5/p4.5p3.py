net_pay = float(input("What is your net pay? "))

if net_pay <= 0:
    print ("Amount must be >= 0. Please try again.")
    
else:
    net_pay_60 = net_pay * .6
    net_pay_40 = net_pay * .4


    tax_large = 13.5 / 100 # Tax rate of 13.5%
    tax_small = 23 / 100 # Tax rate of 23%

    tax_1 = net_pay_60 * tax_large
    tax_2 = net_pay_40 * tax_small
    total_tax = tax_1 + tax_2
    gross_pay = net_pay - total_tax



                    
    print ("Your total taxes are: ", total_tax)
    print ("Your total income is: ", gross_pay)


