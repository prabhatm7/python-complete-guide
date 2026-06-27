from itertools import chain

# join multiple iterables into one stream
numbers = [1, 2]
letters = ["a", "b"]
combined = list(chain(numbers, letters))
print(combined)
