random_string = "This is a random string"

print(random_string.find("is"))
print(random_string.replace("is" , "was"))
print(random_string.upper())
print(random_string.lower())

#string format
string1 = "{author} is beautiful teacher ".format(author="Divya")
#string2 = "{author} is teaching a lesson ".format(author="Divya")

print(string1)

#join - string in list
l=['a','b','c']
print('>>'.join(l))

#this is not available in anyother language
name= "Divya is a good girl" *3
print(name)

