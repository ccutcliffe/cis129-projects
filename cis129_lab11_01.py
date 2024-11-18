# Christopher Cutcliffe
# 11/18/2024
# Lab 11 9.1
# the main function
def main():
    # initialize variables
    message = ('Type the grades one at a time! (Enter -1 to quit.)')
    # perform function calls
    create_file(message)

# function to validate user input
def validate_input(message):
    # declare variables
    user_string = 0
    # loops until legal input is achieved
    while True:
        try:
            # prompts user for input
            user_string = int(input(message))
        # input was not a number
        except ValueError:
            print("Entry must be an integer!")
        # something else went wrong somehow
        except:
            print("Invalid Entry!")
        else:
            return user_string

# function to print output to file
def create_file(message):
    # initialize variables
    next_grade = 0
    # open file for write mode. note that this will erase existing content!
    with open('grades.txt', mode='w') as grades:
        # loop until sentinel is entered
        while next_grade != -1:
            next_grade = validate_input(message)
            # only proceed if it is not the sentinel
            if next_grade != -1:
                if next_grade < 0 or next_grade > 100:
                    # illogical grade
                    print("Out of bounds.")
                else:
                    # add it to the file
                    print(next_grade, file=grades)
    return
            
# calls main
main()
