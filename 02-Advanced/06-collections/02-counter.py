from collections import Counter

# count hashable items
c = Counter("mississippi")
print(c)
print(c.most_common(3))
print(c["s"])

# count words
words = "the cat sat on the mat the cat".split()
print(Counter(words).most_common(2))

c2 = Counter({"a": 3, "b": 2, "c": 1})
for key, count in c2.items():
    print(f"{key}: {count}")
