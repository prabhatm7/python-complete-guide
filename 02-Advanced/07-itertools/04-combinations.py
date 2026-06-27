from itertools import combinations, combinations_with_replacement

# choose items without repeating order
items = ["A", "B", "C"]
print(list(combinations(items, 2)))
print(list(combinations_with_replacement(items, 2)))
