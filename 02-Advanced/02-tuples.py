# ordered, immutable, allows duplicates

mytuple = (1, 2, 3, 4, 5)
print(mytuple)

# observation 1
tuple2 = ("apple")
print(type(tuple2)) # str

tuple2 = ("apple",)
print(type(tuple2)) # tuple

# create a tuple from a list
tuple3 = tuple([1, 2, "Boston", True, 5])
print(tuple3)

first_element = mytuple[0]
print(first_element)

last_element = mytuple[-1]
print(last_element)

# slicing
sub_tuple = mytuple[1:4]
print(sub_tuple)

# tuple3[1] = 100  TypeError: 'tuple' object does not support item assignment

for i, item in enumerate(mytuple):
    print(i, item)

if 5 in mytuple:
    print("5 is present in mytuple")
else:
    print("5 is not present in mytuple")

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = tuple(filter(lambda x: x % 2 == 0, my_tuple))
print(even_numbers)
print(len(my_tuple))
print(my_tuple.count(5))
print(my_tuple.index(5))


print("min(my_tuple):", min(my_tuple))
print("max(my_tuple):", max(my_tuple))
print("sum(my_tuple):", sum(my_tuple))


details = "John", 25, "New York"
name, age, city = details
print(type(details))

# use * to unpack the remaining values
details = "John", 25, "New York", "USA", "Engineer"
name, age, city, *other_details = details
print(name, age, city)
print(other_details)  # ['USA', 'Engineer']


# when to use tuples over lists?
# 1. When you want to create a collection of items that should not be changed (immutable)
# 2. When you want to use the collection as a key in a dictionary (tuples are hashable, lists are not)
# 3. When you want to return multiple values from a function (tuples can be used to return multiple values)


# tuples vs list 
# 1. Tuples are immutable, while lists are mutable.
# 2. Tuples can be used as keys in dictionaries, while lists cannot.
# 3. Tuples are generally faster than lists for iteration and access becuase of their immutability, python optimizes memory usage and performance for immutable objects.


import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print("Size of list:", sys.getsizeof(my_list), "bytes")
print("Size of tuple:", sys.getsizeof(my_tuple), "bytes")

import timeit
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("Time taken to create list:", list_time)
print("Time taken to create tuple:", tuple_time)