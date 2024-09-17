my_list= 12345 , "hi this is automation" , 5.0
print(my_list)

String1 = "Hello, I'm a Pramod"
list1 = list(String1)
print(list1)
list1[2] = 'p'
String2 = '-'.join(list1)
print(String2)
#deleting a character from string
del String2[2] #this will give error as string is immutable
print(String2) #as expected the error is displayed


