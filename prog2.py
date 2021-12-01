# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

def seperation():
    print("\n\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")

def checkPassword(password):

    SpecialSym = ['"', "'", '[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':', ']', '`', '+', '=', '-', '.', ',', ':', ';', '~', "'\'"]
    val = True

    if len(password) < 15:
        print ("\33[3mThe character must be \33[1mgreater than 15.\33[0m")
        val = False

    if not any(char.isupper() for char in password):
        print("\33[3mPassword should have at least \33[1mone capital letter.\33[0m")
        val = False

    if not any(char.isdigit() for char in password):
        print("\33[3mPassword should have at least \33[1mone number.\33[0m")
        val = False

    if not any(char in SpecialSym for char in password):
        print("\33[3mPassword should at least \33[1mone special character !@#$%^&*()_+ etc.\33[0m")
        val = False

    if val:
        return val

def main():
    seperation()
    print("\n\33[1m\33[37m\t     ++\33[4m\33[33mPassword Validator\33[0m\33[1m\33[37m++\33[0m")
    seperation()
    password = input("\n\t\33[1mEnter your password: \33[0m")
    seperation()


    if (checkPassword(password)):
        print("\n\t\33[1m\33[32m     Your password is valid.\33[0m")
        seperation()
    else:
        seperation()
        print("\n\t\33[1m\33[31mSorry, your password is invalid!!\33[0m")
        seperation()

main()

