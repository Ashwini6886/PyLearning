# basic function example

# print("START ")
# def sayHello():
#     print("Hello! from the function")
#
# print("END")
#
# sayHello()

###################################################################

# Understanding on Local and Global variables

# name = "Python"  # Global variable

# def func():
#     age = 38 # this is a local variable and cant be used outside function
#     print(name)
#     print(age)
#
# print("added again",name)
# #print(age) # calling a local variable so error is thrown once executed
#
# func()

#######################################################################

# how the functions can be called multiple times

# def printIfloop():
#     for i in range(1,11):
#         print(i)
#
#
#
# printIfloop()
#
# print("-----------------")

#######################################################################
#simple program to call a fucntion from a function

# def greet():
#     print("hello")
#
# def f ():
#     print ("calling from f function")
#     greet()
#
# f() #--> Check once by commenting this statement

##################################################################################

# taking user input and multiplying by 10

# user_input = int(input("Enter the number to multiply by 10: "))
#
# def multiplyBy10(num): #num is going to take the input
#     print("multiplying  by 10")
#     return num * 10 # the output to be returned if not given nothing will be returned
#
# result = multiplyBy10(user_input) # here we are calling the function with user input
# print(result)

######################################################################################

#simple program to multiply 2 numbers

# user_input1 = int(input("Enter the 1st number"))
# user_input2 = int(input("Enter the 2nd number"))
#
# def multiply(n1, n2):
#     return n1 * n2
#
# result = multiply(user_input1, user_input2)
# print("The Multiplcation result is", result)
#
# def sub(n1,n2):
#     suba=n1-n2
#     return suba
# result1=sub(user_input1 , user_input2)
# print("The subtraction result is", result1)



#####################################################################################
# examples of some in build fucntions

# print (pow(2,3))
# print(round(3.12444,3))

##################################################################################

# to find the greatest of 2 numbers

# user_input1 = int(input("Enter the 1st number"))
# user_input2 = int(input("Enter the 2nd number"))
#
# def greater(num1 , num2):
#     if(num1>num2):
#         return num1
#     else:
#         return num2
#
# result = greater(user_input1, user_input2)
# print( "the greater number is ",result)

#

