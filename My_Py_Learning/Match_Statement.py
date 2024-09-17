# write a program to print positive or negative number

# num = int(input("enter a interger number"))
#
# match num :
#     case num if num > 0:
#         print("positive number")
#     case num if num <0 :
#         print("negative number")
#     case _:
#         print("Invalid")
###############################################################################333

# basic program
# name = "Python"
#
# match name:
#     case "Python":
#         print("Python is a programming language")
#     case "Java":
#         print("Java is a programming language")
#     case _:
#         print("No match found")

# print("end of the program ")


################################################################################
#to Find the substring in the a string

string = input(" Enter the string ")
subString = "Python"

match string:
    case x if subString in x:
        print("Sub-string found")
    case _:
        print("Sub-string not found") #code not working need to check again

