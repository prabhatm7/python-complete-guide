# key value pair, mutable and unordered data structure
mydict = {"name": "John", "age": 30, "city": "New York"}
print("mydict:", mydict)

mydict2 = dict(name="Alice", age=25, city="Los Angeles")
print("mydict2:", mydict2)

mydict["age"] = 31
print("Updated mydict:", mydict)

del mydict["city"]
print("mydict after deletion:", mydict)

mydict.pop("age")
print("mydict after popping age:", mydict)

mydict.popitem()
print("mydict after popping an item:", mydict)

mydict = {"name": "John", "age": 30, "city": "New York"}
print("mydict keys:", mydict.keys())
print("mydict values:", mydict.values())

if "name" in mydict:
    print("Name is present in mydict")


try:
    print("mydict['country']:", mydict["country"])
except KeyError:
    print("KeyError: 'country' not found in mydict")


for index, (key, value) in enumerate(mydict.items()):
    print(f"Item {index}: {key} = {value}")


mydict_cpy = mydict
# observation: mydict_cpy is a reference to mydict, not a copy
mydict_cpy["age"] = 35
print("mydict after modifying mydict_cpy:", mydict)
print("mydict_cpy:", mydict_cpy)


# so to create a deep copy of a dictionary, we can use the copy() method
mydict_deepcopy = mydict.copy()
mydict_deepcopy["age"] = 40
print("mydict after modifying mydict_deepcopy:", mydict)
print("mydict_deepcopy:", mydict_deepcopy)


# update 
person1 = {"name": "John", "age": 30}
person2 = {"city": "New York", "age": 25}
person1.update(person2)
print("Updated person1:", person1)


# int and tuple can be used as keys 
mydict = {1: "one", (2, 3): "tuple"}
print("mydict with int and tuple keys:", mydict)