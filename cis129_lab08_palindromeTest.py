# Christopher Cutcliffe
# 10/28/2024
# Lab 8 Palindrome Testing
# regex will be used to speed the process along
import re
# the main function
def main():
    # initialize variables
    message = 'Type in a word or phrase!'
    test_string = ''
    # perform function calls
    test_string = validate_input(message)
    print(palindrome_test(test_string))

# function to validate user input
def validate_input(message):
    # declare variables
    user_string = ''
    # loops until string contains a letter or number
    while not re.search('[a-zA-Z0-9]', user_string):
        try:
            # prompts user for input
            user_string = input(message)
            # checks for inputs outside of legal range
            if not re.search('[a-zA-Z0-9]', user_string):
                # something went wrong, try again
                print("Invalid Entry!")
        # just in case there is an error somehow
        except:
            # something went wrong, try again
            print("Invalid Entry!")
    return user_string

# function to check if the string is the same forward and backward
def palindrome_test(test_string):
    # declare variables
    my_stack = []
    # make sure it's case insensitive
    test_string = test_string.upper()
    # convert the whole thing into a stack
    for x in test_string:
        # push only alphanumeric characters
        if re.search('[a-zA-Z0-9]',x):
            my_stack.append(x)
    # return true if it's the same backwards, false otherwise.
    return (my_stack == my_stack[::-1])

# calls main
main()
