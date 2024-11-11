# Christopher Cutcliffe
# 11/11/2024
# Lab 10 Check Protection
# the main function
def main():
    # initialize variables
    message = ('Type in the check amount! (Do not include $ or .)'
    '\n(The last two digits will be considered cents.)')
    test_string = ''
    # perform function calls
    test_string = validate_input(message)
    check(test_string)

# function to validate user input
def validate_input(message):
    # declare variables
    user_string = ''
    # loops until string contains only numbers
    while not user_string.isdigit():
        try:
            # prompts user for input
            user_string = input(message)
            # checks for inputs outside of legal range
            if not user_string.isdigit():
                # something went wrong, try again
                print("Invalid Entry!")
        # just in case there is an error somehow
        except:
            # something went wrong, try again
            print("Invalid Entry!")
    return user_string

# function to print output
def check(test_string):
    # initialize variables
    SPACER = '-'
    SPACER *= 8
    # converts to dollars and cents and prints
    test_string = int(test_string)/100
    print(f'{test_string:*>8,.2f}')
    print(SPACER)
    print('01234567')

# calls main
main()
