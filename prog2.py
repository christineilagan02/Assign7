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

def checkPassword(password):

    SpecialSym = ['"', "'", '[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':', ']', '`', '+', '=', '-', '.', ',', ':', ';', '~', "'\'"]
    val = True

    if len(password) <= 15:
        print ("The letters must be greater than 15.")
        val = False

    if not any(char.isupper() for char in password):
        print("Password should have at least one capital letter.")
        val = False

    if not any(char.isdigit() for char in password):
        print("Password should have at least one number.")
        val = False

    if not any(char in SpecialSym for char in password):
        print("Password should at least one special character !@#$%^&*()_+ etc.")
        val = False

    if val:
        return val

def main():
    password = input("Enter your password: ")

    if (checkPassword(password)):
        print("valid")
    else:
        print("Invalid Password!!!")

main()

