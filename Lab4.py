# Module 4 Lab-4
# Christopher Cutcliffe
# 9/29/2024
# This program calculates employee bonuses based on their monthly sales.
# The main function
def main():
    # declare local variables
    monthlySales = getSales() # monthly sales amount
    salesIncrease = getIncrease() # percent of sales increase
    storeAmount = calcStoreBonus(monthlySales) # store bonus amount
    empAmount = calcEmpBonus(salesIncrease) # employee bonus amount
    printBonus(storeAmount, empAmount)

# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Please input the monthly sales amount in dollars.'))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input('Please input the sales increase in percentage.'))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible!')

# calls main
main()
