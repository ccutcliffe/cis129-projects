# Christopher Cutcliffe
# 11/18/2024
# Lab 11 9.3
# imports
import csv

# the main function
def main():
    # initialize variables
    message_1 = ("Enter the student's First Name! (Input QUIT to quit.)")
    message_2 = ("Enter the student's Last Name!")
    message_3 = ("Enter the student's First Exam Score!")
    message_4 = ("Enter the student's Second Exam Score!")
    message_5 = ("Enter the student's Third Exam Score!")
    # perform function calls
    create_file(message_1, message_2, message_3, message_4, message_5)

# function to print output to file
def create_file(message_1, message_2, message_3, message_4, message_5):
    # initialize variables
    first_name = ''
    last_name = ''
    grade_1 = -1
    grade_2 = -1
    grade_3 = -1
    # open file for write mode. note that this will erase existing content!
    with open('grades.csv', mode='w', newline='') as grades:
        # create writer object
        writer = csv.writer(grades)
        # loop until sentinel is entered
        while first_name.upper() != 'QUIT':
            first_name = validate_input(message_1, str)
            # only proceed if it is not the sentinel
            if first_name.upper() != 'QUIT':
                last_name = validate_input(message_2, str)
                grade_1 = check_grades(message_3)
                grade_2 = check_grades(message_4)
                grade_3 = check_grades(message_5)
                writer.writerow([first_name, last_name, grade_1, grade_2, grade_3])
    return

# function that ensures grades are valid
def check_grades(message):
    # initiate variables
    next_grade = -1
    while next_grade < 0 or next_grade > 100:
        next_grade = int(validate_input(message, int))
        if next_grade < 0 or next_grade > 100:
            # illogical grade
            print("Out of bounds.")
    return next_grade

# function to validate user input
def validate_input(message, data_type):
    # declare variables
    user_string = ''
    # loops until legal input is achieved
    while True:
        try:
            # prompts user for input
            user_string = input(message)
            # indicates that this is meant to be a numeral            
            if data_type == int:
                if user_string.isdigit():
                    # check passed
                    return user_string
                else:
                    # invalid input
                    print("Invalid score!")
            # indicates that this is meant to be a word
            elif data_type == str:
                if user_string.isalpha():
                    # check passed
                    return user_string
                else:
                    # invalid input
                    print("Invalid name!")
        except:
            # something broke
            print("An Error Occurred!")

# calls main
main()
