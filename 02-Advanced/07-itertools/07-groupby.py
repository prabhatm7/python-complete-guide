from itertools import groupby

# group consecutive items with the same key
words = ["ant", "apple", "bear", "bat", "cat", "car"]
for key, group in groupby(words, key=lambda word: word[0]):
    print(key, list(group))
