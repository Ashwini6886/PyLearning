# some fuctions


# password = ("ashwini123")
#
# print(password.isnumeric())
# print(password.isalpha())
# print(password.isalnum())
# print(password.islower())
# print(password.isupper())

#using these fucnitons in Match checking the password is strong weak

password = input("Enter the password ")

match password:
    case password if(len(password) <6):
        print(" weak password")
    case password if (password.isnumeric()):
        print(" NUMERIC ONLY !!! add Alpha numeric characters")
    case password if(password.islower()):
        print(" LOWER CASE ONLY !!! add upper case characters")
    case password if (password.isupper()):
        print(" UPPER CASE ONLY !!! add lower case characters")
    case _:
        print("strong password")



