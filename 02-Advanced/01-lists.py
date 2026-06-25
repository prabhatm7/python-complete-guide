mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

first_item = mylist[0]
print(first_item)

last_item = mylist[-1]
print(last_item)

for fruit in mylist:
    print(fruit)

if "banana" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))
mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("banana")
print(mylist)

mylist2.clear()
print(mylist2)

numbers = [5, 2, 9, 1, 7]
numbers.sort() # in place
print(numbers)

newlist = sorted(numbers) # returns a new list
print(newlist)

zero_list = [0] * 5
print(zero_list)

union_list = mylist + newlist
print(union_list)

# slicing 
numbers = [5, 2, 9, 1, 7]
print(numbers[1:4]) # [2, 9, 1] 
print(numbers[:3])  # [5, 2, 9]
print(numbers[2:])  # [9, 1, 7]
print(numbers[:])   # [5, 2, 9, 1, 7]

print(numbers[::2]) # [5, 9, 7] every second element
# reverse the list
print(numbers[::-1]) # [7, 1, 9, 2, 5] reverse the list

list_ord = ["banana", "cherry", "apple"]
list_cpy = list_ord # both list point to the same object
print(list_ord)
list_cpy.append("lemon")
print(list_ord) # ['banana', 'cherry', 'apple', 'lemon']

# three ways to create a deep copy of a list
list_cpy = list_ord.copy() # list_cpy is a new list object with the same elements as list_ord(deep copy)
list_cpy.append("blueberry")
print(list_ord) # ['banana', 'cherry', 'apple', 'lemon']
print(list_cpy) # ['banana', 'cherry', 'apple', 'lemon', 'blueberry']


# slice copy behaviour
list1 = ["banana", "cherry", "apple"]
list2 = list1[:] # list2 is a new list object with the same elements as list1(deep copy)
list2.append("lemon")
print(list1) # ['banana', 'cherry', 'apple']
print(list2) # ['banana', 'cherry', 'apple', 'lemon']

# new list() behaviour
list1 = ["banana", "cherry", "apple"]
list2 = list(list1) # list2 is a new list object with the same elements as list1(deep copy)
list2.append("lemon")
print(list1) # ['banana', 'cherry', 'apple']
print(list2) # ['banana', 'cherry', 'apple', 'lemon']


# list comprehension
numbers = [5, 2, 9, 1, 7]
squared = [x * x for x in numbers]
print(squared) # [25, 4, 81, 1, 49