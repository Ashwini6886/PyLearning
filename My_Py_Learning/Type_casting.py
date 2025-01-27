#type casting examples

#conveting str to int

user_input = int(input("Enter a number: "))
num = user_input+10
print(num)

#converting the Boolean value to int
bool_val = int(False)
print(bool_val)

print(type(bool_val))

#binary to interger conversion
bin = int("1010",2)
print(bin)
print(type(bin))

#Example 1 - build in fucntions
user_input = input("enter the age") # this will return string only
#print(user_input)
#print(type(user_input))
user_input = int(user_input)
user_input = user_input + 10
print(user_input)

# conversion from int to float
num = float(10)
print(num) # answer will be 10.0

pie = "3.14"
con = float(pie)
print(con)

# bool to str
bool_val = str("TRUE")
print(bool_val)

#example on List

marks = [96, 90, 97, 94]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
#print(marks[4]) #out of range error

#example of string to list
name = "ashwini"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
#print(name[7]) #out of range error

#same above example we can give as below also
name = "ashwini"
list_name = list(name)
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#example on list to string
list_name = ['a', 's', 'h', 'w', 'i', 'n', 'i']
string_list = str(list_name)
print(string_list) # not possible to print as list

#boolean converstion to list
zero = bool(0)
one = bool(1)
anynumber = bool(30)
neg = bool(-1)
print(zero)
print(one)
print(anynumber) #any number other than 0 is true
print(neg) #any number other than 0 is true

#empty string in bool
empty = bool("")
nonempty = bool("ashwini")
nonestring = bool(None)
print(empty) #empty strings will always return false
print(nonempty)
print(nonestring) # will return true as none is not empty

__name__ = "ashwini"
print(__name__)






