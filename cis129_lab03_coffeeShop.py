# This records purchases from user as integers.
c = int(input('How many coffees would you like to purchase?'))
m = int(input('How many muffins would you like to purchase?'))
# This calculates the customer's expenses.
cprice = c * 5
mprice = m * 4
tax = (cprice + mprice)*0.06
total = cprice + mprice + tax
# Now it gives the receipt.
print(
    '***************************************'
    '\nMy Coffee and Muffin Shop'
    # c and m are converted to strings to avoid automatic spacing.
    '\nNumber of coffees bought?\n' + str(c),
    '\nNumber of muffins bought?\n' + str(m),
    '\n***************************************\n'
    '\n***************************************'
    '\nMy Coffee and Muffin Shop Receipt'
    # The format function with .2f ensures exactly 2 trailing zeros.
    '\n' + str(c), 'Coffee at $5 each: $', format(cprice, '.2f'),
    '\n' + str(m), 'Muffins at $4 each: $', format(mprice, '.2f'),
    # The .lstrip function removes leading zero when tax < $1.
    '\n6% tax: $', format(tax, '.2f').lstrip('0'),
    '\n---------\nTotal: $', format(total, '.2f'),
    '\n***************************************')
