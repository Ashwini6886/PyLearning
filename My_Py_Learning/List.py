# my_list= 12345 , "hi this is automation" , 5.0
# print(my_list)
#
# String1 = "Hello, I'm a Pramod"
# list1 = list(String1)
# print(list1)
# list1[2] = 'p'
# String2 = '-'.join(list1)
# print(String2)
# #deleting a character from string
#del String2[2] #this will give error as string is immutable
#print(String2) #as expected the error is displayed

# list continuation after the data types
#using the insert function
my_marks = []
my_marks.insert(0, 100)
my_marks.insert(1, 90)
my_marks.insert(2, 80)

#using append function
my_marks.append(70)
print(my_marks)

#using other functions with list
my_marks.clear()
print(len(my_marks))

#using remove function
# my_marks.remove(90)
# print(my_marks)

#Nested list
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0])
print(my_list[1])

#changing the values in the nested list
my_list[0] = "10", "20", "30"
print(my_list)

#range function in list
sq = [i**2 for i in range(10)]
print(sq)

num = list(range(1,10))
print(num)

#list built in fucntions
my_list = [1, 2, 3]
print(my_list[0])

#slicing
print (my_list[0:2])
print (my_list[2:])
print (my_list[:2])
print (my_list[:-1])
print (my_list[:-2])

#extend function
my_list.extend([4, 5 , 5, 7,8 ,1])
print(my_list)

#pop function
i = my_list.pop(1)
print(i)
print(my_list)
print(my_list.count(1)) # count helps in returning the number of times the element is present in the list

# reverse function
my_list.reverse()
print(my_list)




