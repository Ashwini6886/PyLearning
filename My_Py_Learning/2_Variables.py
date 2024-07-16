#int data type
a = 5
print(a)
#again assigning a to other number a = 10
a = 10
print(a)
#adding
a + a
#ressigning a like below  and check thw value of a
a = a + a
print(a)
#check the data type of a
type(a)
#reassigning the a to floating point number
a = 30.1
print(a)
#check the type
type(a)
#next problem
my_income = 100
tax_on_income = 0.5
tax_taken = my_income * tax_on_income
print(tax_taken)


#dynamically typed
age = 65
print (type(age))
age = "Ashwini"
print (type(age))

#problem1 guess the output ---> its is Int
age=70
age =-90
roll_number=123
phone_number =  1234567890
print(type(age))

# the variables can be assigned in the following ways also
name = "Ashwini"
name1 = 'Ashwini'
# tripple inverted comas means we can added multiple times
name2 = """Ashwini"""
name3 = '''Ashwini'''
print( type(name))
print( type(name1))
print( type(name2))
print( type(name3))


#different ways to define the variables
#a = 5
#b = 6
#c = 7
#print(a+b+c)
#below in another method to write the same code
a,b,c = 5,6,7
print(a+b+c)
