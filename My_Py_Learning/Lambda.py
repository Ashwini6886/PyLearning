#Lambda exapmle - without using fucntion name we can use this
# this is a anonymous fucntion which is defined in python
# a = lambda a : a*2
# print(a(19))
#
# #Finding power 2
#
# user_input= int(input ("enter the number"))
#
# result = lambda user_input : pow(2, user_input)
# print(result(user_input))
#
# #find the sum of 2 numbers
# add = lambda a,b : a+b
# print(add(10,20))
#
# # how Lambda saves the lines
#
# r = lambda x , y ,z : x+y+z
# print(r(10,20,30))
# print(r(100, 200, 300)) # can use it any number of times , can call that r as many as we want
#
# #can have multiple no of lambda expressions also
# r2 = lambda x , y ,z ,a : x+y+z+a
# print(r2(10, 20, 30, 40))
# print(r2(100, 200, 300, 400))
#
# #example1
#
# var = lambda p, g, r : p[0]+g[0]+r[0]
# print (var ("world", "wide" ,"web") )
#
#
# # using loops with Lambda
# r = lambda num : "greater than 50" if num >50 else "less than 50"
# print(r(45))
# print(r(67))

# using else if with lambda in a specific way
rx = lambda n1 : n1 ** 2 if n1 > 0 else ( n1 * 2 if n1 < 0 else 0)
print(rx(5))
print(rx(-1))
print(rx(0))