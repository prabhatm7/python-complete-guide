# dictionary is a key value pair store

fruit_basket = {
    "apple" : 2,
    "mango" : 3
}

print(fruit_basket.get("apple"))
print(fruit_basket["apple"])

print(fruit_basket.get("banana"))
# print(fruit_basket["banana"]) # KeyError : banana

print(fruit_basket.keys())
print(fruit_basket.values())

for key, value in fruit_basket.items():
    print(f"{key} quantity is : {value}")