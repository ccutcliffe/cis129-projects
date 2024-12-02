# Christopher Cutcliffe
# 12/1/2024
# Lab 12
# main module
def main():
    # initialize variables
    inputName = ''
    inputType = ''
    inputAge = 0
    # create a Pet object
    animal = Pet()

    # set pet name
    print("Enter a pet name:")
    inputName = validate_input(str)
    animal.setName = inputName

    # set pet type
    print("Enter a pet type:")
    inputType = validate_input(str)
    animal.setType = inputType

    # set pet age
    print("Enter a pet age:")
    inputAge = validate_input(int)
    animal.setAge = inputAge

    # get pet values
    print("The pet name is:", animal.getName)
    print("The pet type is:", animal.getType)
    print("The pet age is:", animal.getAge)

# function to validate user input
def validate_input(data_type):
    # declare variables
    user_string = ''
    # loops until legal input is achieved
    while True:
        try:
            # prompts user for input
            user_string = input()
            # indicates that this is meant to be a numeral
            if data_type == int:
                if user_string.isdigit():
                    # check passed
                    return user_string
                else:
                    # invalid input
                    print("Please input a number!")
            # indicates that this is meant to be a word
            elif data_type == str:
                if user_string.isalpha():
                    # check passed
                    return user_string
                else:
                    # invalid input
                    print("Please input a word!")
        except:
            # something broke
            print("An Error Occurred!")

# defines the Pet class
class Pet:
    # Constructor
    def __init__(self):
      	self._name = ''
      	self._type = ''
      	self._age = 0

    # Getters
    @property
    def getName(self):
        # return the name
        return self._name

    @property
    def getType(self):
        # return the type
        return self._type

    @property
    def getAge(self):
        # return the age
        return self._age

  	# Setters
    @getName.setter
    def setName(self, value):
        # set the name
        self._name = value

    @getType.setter
    def setType(self, value):
        # set the type
        self._type = value

    @getAge.setter
    def setAge(self, value):
        # set the age
        self._age = value

# calls main
main()
