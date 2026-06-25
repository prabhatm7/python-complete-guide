# unordered, mutable, and iterable data structure, no duplicate elements
myset = {1, 2, 3, 4, 5}
print("myset:", myset)

myset.add(6)
print("myset after adding 6:", myset)

myset.add(3)  # adding duplicate element, will not change the set
print("myset after adding duplicate 3:", myset)

# observation
myset2 = set("Hello")
print("myset2 from string 'Hello':", myset2)

# observation
myset3 = {}
print(type(myset3))  # dict, not set

myset3 = set()
print(type(myset3))  # set

myset3.discard(1)  # discard does not raise an error if the element is not present
print("myset3 after discarding 1:", myset3)
# myset.remove(10)  # remove raises an error if the element is not present
# print("myset after removing 1:", myset)


for i in myset:
    print(i)

if "3" in myset:
    print("3 is present in myset")


odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)

intersection = odds.intersection(primes)
print(intersection)

difference = odds.difference(primes)
print(difference)

sym_diff = odds.symmetric_difference(primes)
print(sym_diff)

# inplace operations
# update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

# intersection update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

# difference update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)

# symmetic difference update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)


# subset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # True
# superset
print(set2.issuperset(set1))  # True

# copy
set1 = {1, 2, 3}
set2 = set1.copy() # or use set2 = set(set1)
set2.add(4)
print(set1)  # {1, 2, 3}
print(set2)  # {1, 2, 3, 4}


# frozenset(immutable set)
fset = frozenset([1, 2, 3, 4])
# fset.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
print(fset)