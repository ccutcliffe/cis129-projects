# Module 5 Lab-5
# Christopher Cutcliffe
# 10/5/2024
# This program calculates payment for bottles.
# The main function.
def main():
    # Initialize variables.
    keep_going = 'y' # Tells the program to keep going.
    while keep_going == 'y': # Continues until told to stop.
        total_bottles = get_bottles()
        total_payout = calc_payout(total_bottles)
        print_info(total_bottles,total_payout)
        print('Do you want to enter another week’s worth of data?')
        keep_going = input('(Enter y or n):')

# This function calculates the number of bottles brought in.
def get_bottles():
    # Initialize variables.
    NBR_OF_DAYS = 7 # Adjust for shorter or longer weeks.
    total_bottles = 0 # Tracks total bottles.
    counter = 1 # Controls the loop.
    today_bottles = 0 # Tracks bottles for the day.
    # Increment counter.
    while counter <= NBR_OF_DAYS:
        today_bottles = int(input('Enter number of bottles returned for day #'
                                 + str(counter) + ':'))
        total_bottles += today_bottles
        counter += 1
    # Makes sure we actually get the value.
    return total_bottles

# Calculates payment.
def calc_payout(total_bottles):
    PAYOUT_PER_BOTTLE = .10 # Price per bottle. This can be adjusted.
    total_payout = 0 # The lab required I include this but there is no need
    # to initialize this variable since it does not iterate between loops.
    total_payout = total_bottles * PAYOUT_PER_BOTTLE
    return total_payout

# Prints properly formatted receipt.
def print_info (total_bottles,total_payout):
    print('The total number of bottles collected is',total_bottles)
    print(f'The total paid out is $ {total_payout:.1f}'.lstrip('0'))
    return

# Call main.
main()
