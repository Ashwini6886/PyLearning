my_dict = {"name": "John", "age": 25, "city": "New York"}
print(my_dict)

# update the value of a key
my_dict["age"] = 26
print(my_dict)

#adding new keys
my_dict["country"] = "USA"
print(my_dict)

#deleting a key
del my_dict["country"]
print(my_dict)

#mixed dictionary
my_dict = {"name": "John", "age": 25, "city": "New York", "grades": [85.1, 90, 78]}
print(my_dict)
#to iterate over the dictionary
for key in my_dict:
    print(key, my_dict[key])
    print(key)
# checking if the name is present in the dictionary
if "name" in my_dict:
    print("name is present in the dictionary")
#print all the keys and valies
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
#dictionary within the disctionary
# my_dict = {
#             "dict1" : {"name": "John", "age": 25, "city": "New York"},
#             "dict2" : {"name": "Alice", "age": 65, "city": "York"},
#             "dict3" : {"name": "Bob", "age": 45, "city": "New York"}
#             }
# print(my_dict)
# print(my_dict["dict3"]["name"])


# relationship with dictionary and the JSON format
