from itertools import islice

# take only the first few items from any iterable
items = range(10)
print(list(islice(items, 5)))
print(list(islice(range(1, 20), 2, 8)))
