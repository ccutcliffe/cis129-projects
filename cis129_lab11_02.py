# Christopher Cutcliffe
# 11/18/2024
# Lab 11 9.2
# the main function
def main():
    # initialize variables
    total = 0  # sum of grades
    grade_counter = 0 # number of grades entered
    try:
        # begin processing grades
        with open('grades.txt', mode='r') as grades:\
            # header
            print('Grades:')
            # loop until the file is processed completely
            for grade in grades:
                grade_counter += 1
                total += int(grade)
                print(int(grade))
            if grade_counter != 0:
                # finalize readout
                print("\nTotal:")
                print(total)
                print("\nCount:")
                print(grade_counter)
                print("\nAverage:")
                print(total / grade_counter)
            # if there are no grades in the file
            else:
                print('No grades were entered!')
    # exception handling
    except FileNotFoundError:
        # grades.txt was missing
        print('Run the first program first!')
    except PermissionsError:
        # program tried to run in a sensitive location
        print('Permissions error! Try a different location!')
    except:
        # some unknown problem happened
        print('Something went wrong!')

# calls main
main()
