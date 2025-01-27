my_list = [1, 2, 3, 4, 5]
#iterate over each element

def double_Me(x):
    return x * 2

result = map(double_Me, my_list)
print(list(result))

for i in result:
    print(i)

#filter function
def check_even(x):
    return x % 2 == 0
result = filter(check_even, my_list)
print(list(result))

#finding the largest number in the list
def find_largest(numbers):
    larger_element = numbers[0]
    for i in numbers:
        if numbers > larger_element:
            larger_element = numbers
        return larger_element

    result = find_largest(my_list)
    print(result)

#to check if th elist is empty or not
my_list=[]
non_empty =[2, 3, 4]

def check_list(temp_list):
    if len(temp_list) == 0:
        print("list is empty")
    else:
        print("list is not empty")

check_list(my_list)
check_list(non_empty)

#example : to add a number by cheking if it duplicate or not in the list

my_list = [1, 2, 3, 4, 5, 1]
my_set = set(my_list)
print(my_set)

