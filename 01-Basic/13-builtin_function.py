# Basic introspection functions
name = "Python"
numbers = [10, 20, 30, 40]

print("len(name):", len(name))
print("type(numbers):", type(numbers))
print("id(numbers):", id(numbers))
print("dir(name) sample:", dir(name)[:5])

# Math and sorting functions
values = [5, 2, 9, 1, 7]

print("sum(values):", sum(values))
print("max(values):", max(values))
print("min(values):", min(values))
print("sorted(values):", sorted(values))

# Iteration helper functions
fruits = ["apple", "banana", "mango"]
prices = [100, 40, 60, 11]

print("enumerate(fruits):")
for index, fruit in enumerate(fruits):
	print(index, fruit)

print("zip(fruits, prices):", list(zip(fruits, prices)))

# map() applies a function to every item
squared = list(map(lambda x: x * x, values))
print("map(square):", squared)

# filter() keeps items that match a condition
even_values = list(filter(lambda x: x % 2 == 0, values))
print("filter(even):", even_values)

checks = [True, True, False]
print("any(checks):", any(checks))
print("all(checks):", all(checks))

for fruit, price in zip(fruits, prices):
	print(f"fruit : {fruit} and price : {price}")
