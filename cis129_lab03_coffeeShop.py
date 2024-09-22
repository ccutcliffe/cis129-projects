'''This program was created by Christopher Cutcliffe
    for the class CIS129'''
# This records purchases from user as integers.
c = int(input('How many coffees would you like to purchase?'))
m = int(input('How many muffins would you like to purchase?'))
d = int(input('How many doughnuts would you like to purchase?'))
t = int(input('How many teas would you like to purchase?'))
# This calculates the customer's expenses.
cprice = c * 5
mprice = m * 4
dprice = d * 2
tprice = t * 3
tax = (cprice + mprice + dprice + tprice)*0.06
total = cprice + mprice + dprice + tprice + tax
# Now it gives the receipt.
print(
    '***************************************'
    '\nMy Coffee and Muffin Shop'
    # c and m are converted to strings to avoid automatic spacing.
    '\nNumber of coffees bought?\n' + str(c),
    '\nNumber of muffins bought?\n' + str(m),
    '\nNumber of doughnuts bought?\n' + str(d),
    '\nNumber of teas bought?\n' + str(t),
    '\n***************************************\n'
    '\n***************************************'
    '\nMy Coffee and Muffin Shop Receipt'
    # The format function with .2f ensures exactly 2 trailing zeros.
    '\n' + str(c), 'Coffee at $5 each: $', format(cprice, '.2f'),
    '\n' + str(m), 'Muffins at $4 each: $', format(mprice, '.2f'),
    '\n' + str(d), 'Doughnuts at $2 each: $', format(dprice, '.2f'),
    '\n' + str(t), 'Tea at $3 each: $', format(tprice, '.2f'),
    # The .lstrip function removes leading zero when tax < $1.
    '\n6% tax: $', format(tax, '.2f').lstrip('0'),
    '\n---------\nTotal: $', format(total, '.2f'),
    '\n***************************************'
    '\n\nThank you for purchasing! Please come again!~')
