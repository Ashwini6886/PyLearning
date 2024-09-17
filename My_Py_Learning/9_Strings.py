name = "Ashwini"
name1 = 'Ashwini'
# triple inverted comas means we can added multiple times
name2 = """Ashwini"""
name3 = '''Ashwini'''
print( type(name))
print( type(name1))
print( type(name2))
print( type(name3))

print("hello world one")
print("hello world two ")
#this will print both the statements


print("hello \n \n world")
# \n will be considered as a new line to be printed

#when directory name is given its not going to take to the path hence to over come that we need to use Raw string
dir = r'C:\noname\dir'
print (dir)

print("hello \t world")
#tabing using \t

#formating of the strings , F--> IS USED FOR FORMATING and will replace the values in the variables , {} this will be used to replace the values
first_name = "Ashwini"
last_name = "T K"
print ( first_name , last_name)
print(first_name+" "+last_name)
full_name = print(f"YOUR FULL NAME IS {first_name} {last_name}")


#example1
#instead of using like print(5*1)
num=90
print(f"the number is{num*2}")
print(f"the number is{num*3}")
print(f"the number is{num*4}")

#example2
num1 = 5
print(f"{num1}*1 is {num1*1}")
print(f"{num1}*2 is {num1*2}")
print(f"{num1}*3 is {num1*3}")
print(f"{num1}*4 is {num1*4}")
print(f"{num1}*5 is {num1*5}")
print(f"{num1}*6 is {num1*6}")
print(f"{num1}*7 is {num1*7}")
print(f"{num1}*8 is {num1*8}")
print(f"{num1}*9 is {num1*9}")
print(f"{num1}*10 is {num1*10}")

#example3
b=1
print(f"{b}*1={b}")
