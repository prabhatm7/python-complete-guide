fruits = ["apple", "banana", "mango"]
fruits.append("guava")
fruits.remove("apple")
fruits.insert(1, "avocado")
fruits.sort()
fruits.reverse()
fruits.pop()


print(f"expect : ", ["mango", "gauva", "banana"])
print(f"got :", fruits)

fruits.insert(0, "apple")
print(fruits)


# list comprehension
squares = [x **2 for x in range(1, 6)]
print(squares)