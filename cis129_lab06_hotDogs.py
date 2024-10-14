# Module 6 Lab-6
# Christopher Cutcliffe
# 10/14/2024
# This program calculates the hotdogs needed for a cookout.
# The main function
def main():
    # Initialize variables and call functions.
    total_hot_dogs = 0
    total_hot_dogs = get_total_hot_dogs()
    show_results(total_hot_dogs)

# Gets necessary hotdog related information.
def get_total_hot_dogs():
    # Initialize variables
    attendees = 0
    hot_dogs = 0
    # This loop ensures a valid input was used.
    while True:
        try:
            # Ask how many people are coming..
            attendees = int(input("How many people will be coming?"))
        except ValueError:
            # Loop until appropriate input.
            print("Please input a valid number.")
            continue
        if attendees < 1:
            # A party of none makes the calculator sad.
            print("Please input a valid number.")
            continue
        else:
            # Success! Exit loop.
            break
    # This loop ensures a valid input was used.
    while True:
        try:
            # Ask how many hotdogs to give them.
            hot_dogs = int(input("How many hotdogs will each person get?"))
        except ValueError:
            # Oops! Wrong input.
            print("Please input a valid number.")
            continue
        if hot_dogs < 1:
            # You have to feed them something.
            print("Please input a valid number.")
            continue
        else:
            # Success! Exit loop
            break
    total = attendees * hot_dogs
    return total

# Calculates the catering and prints it.
def show_results(total):
    # Initialize variables.
    DOGS = 10
    BUNS = 8
    dogs_left = 0
    buns_left = 0
    min_dogs = 0
    min_buns = 0
    # Perform calculations.
    dogs_left = (DOGS - total % DOGS) % DOGS
    # Floor division is used to ensure only whole numbers.
    min_dogs = (total // DOGS) + (0 ** (0 ** dogs_left))
    buns_left = (BUNS - total % BUNS) % BUNS
    # The last bit ensures one extra package if there are leftovers.
    min_buns = (total // BUNS) + (0 ** (0 ** buns_left))
    # Display results.
    print("Minimum packages of hot dogs needed:", min_dogs)
    print("Minimum packages of hot dog buns needed:", min_buns)
    print("Hot dogs remaining:", dogs_left)
    print("Hot dog buns remaining:", buns_left)
    return

# Initiates program.
main()
