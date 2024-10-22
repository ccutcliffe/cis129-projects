# Christopher Cutcliffe
# 10/21/2024
# Lab 7 Theater Seating
# the main function
def main():
    # initialize dictionaries. add more as needed following pattern.
    # note: treat capitalized entries as constants
    # sales initialized to -1 to serve as pseudo-sentinels
    A = {
        "SECTION": "Section A", # name of the section
        "TICKETS": 300, # max number of section A tickets
        "PRICE": 20, # price of section A tickets
        "sales": -1 # section A tickets sold
    }
    B = {
        "SECTION": "Section B", # name of the section
        "TICKETS": 500, # max number of section B tickets
        "PRICE": 15, # price of section B tickets
        "sales": -1 # section B tickets sold
    }
    C = {
        "SECTION": "Section C", # name of the section
        "TICKETS": 200, # max number of section C tickets
        "PRICE": 10, # price of section C tickets
        "sales": -1 # section C tickets sold
    }
    # add additional entries in this tuple as needed
    seating_data = (A,B,C)
    # perform function calls
    welcome_message(seating_data)
    purchase_tickets(seating_data)
    give_total(seating_data)

# welcome message. do not adjust when adding sections.
def welcome_message(seating_data):
    print("Welcome to the Theater! Here are the available options!")
    # loops once for every section
    for x in seating_data:
        # prints number of seats in the section
        print("Seats available in", str(x["SECTION"]) + ":",
              x["TICKETS"])
        # prints the prices for tickets in the section
        print("Ticket pricing for", str(x["SECTION"]) + ":",
              "$" + str(x["PRICE"]) + "\n")
    return

# tracks purchases
def purchase_tickets(seating_data):
    # message to be printed when prompting user
    message = "How many tickets did you sell?"
    # loops once for every section
    for x in seating_data:
        print("Welcome to", str(x["SECTION"]) + "!")
        # asks user for ticket sales and tracks the purchase
        x["sales"] = validate_input(message, x["TICKETS"])
        # calls function for subtotal
        give_subtotal(seating_data)
    return

# ensures user input is valid
def validate_input(message, bound):
    # this variable will hold our input
    value = -1
    # loops until the value is sensible
    while value < 0 or value > bound:
        try:
            # prompts user for input
            value = int(input(message))
            # checks for inputs outside of legal range
            if value < 0 or value > bound:
                # something went wrong, try again
                print("Invalid Entry!")
        except:
            # something went wrong, try again
            print("Invalid Entry!")
    return value

# provides subtotal
def give_subtotal(seating_data):
    subtotal = 0 # tracks current iteration's subtotal
    # loops once for every section
    for x in seating_data:
        # skip any sections that the user hasn't reached
        if x["sales"] >= 0:
            # prints purchases for that section
            print(x["sales"], "tickets sold in",
                str(x["SECTION"]) + ": $" + str(x["sales"] * x["PRICE"]))
            # accumulates total value
            subtotal += x["sales"] * x["PRICE"]
    # prints current earnings
    print("Current Subtotal: $" + str(subtotal) + "\n")
    return
    
# provides total
def give_total(seating_data):
    total = 0 # tracks all purchases
    print("Final Sales:")
    # loops once for every section
    for x in seating_data:
        # prints seats available for each section
        print(x["TICKETS"], "seats available in", x["SECTION"])
        # prints purchases for that section
        print(x["sales"], "tickets bought for",
              str(x["SECTION"]) + ": $" + str(x["sales"] * x["PRICE"]))
        # accumulates total value
        total += x["sales"] * x["PRICE"]
    # prints final value
    print("Total: $" + str(total))
    return

# calls main
main()
