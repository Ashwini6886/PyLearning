#prolem : 1 basic for loop check

# for i in range(10):
#     print("PYTHON")
#     print(i)

# Problem 2 checking the multiple range

# for i in range(1, 7):
#     print("PYTHON")
#     print(i) # when Run keep in mind that it will print only till 6 and 7 wont be printed


# While Loop examples

# while True:
#     print("PYTHON") # enters into infinte loops of printing

# problem 3 : to write an exit condition

# print ('start')
# while True:
#     user_input = input("Enter a number or type exit to break the loop  ")
#     print ("you have entered the following number " + user_input)
#     #adding the exit condition
#     if user_input =='exit':
#         break
#
# print ("end")

# Problem 4 - on while loop with condition

# i = 0
# while i < 5:
#  print(i)
#  i += 1
#
# print("end")

#Prblem 5 -to match the number

# while True:
#     user_input = input("Enter a number or type and if you match my number then i will exit the loop ")
#     print("you have entered " + user_input) # dont put coma , i did the mistake
#     user_input = int(user_input) # important
#     if user_input == 5:
#         print("you have matched the correct number ") # spacing is important , made mistake
#         break

########################################################################
# Problem 6 : to find the lucky number in 3 tries

# import random
# lucky_number = random.randint(1, 10)
# no_tries = 3
# guess_number = None
#
# while guess_number != lucky_number:
#     guess_number = int(input("enter the number from 1 to 10") )
#     if lucky_number > guess_number:
#         print("your guess is too low")
#
#     elif lucky_number < guess_number:
#         print("your guess is too high")

# print( "you have found the lucky number")

######################################################################################3
#Problem 7: choose 1 number of the the 3

choice = None

while choice != 3:
    print ("1. Hello \n 2. Do nothing \n, 3. Bye")
    choice = input("choice 1 -3 ")

    if choice == '1':
     print ("Hello")

    elif choice == '2':
     print("do Nothing")

    elif choice == '3':
     print("bye")
     break
    else:
     print("Invalid choice. Please try again.")

#############################################################################

#problem 8 :

