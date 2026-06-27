from collections import defaultdict

# missing keys get a default value automatically
word_count = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
    word_count[word] += 1

print(dict(word_count))

# group values by key
grouped = defaultdict(list)
for word in ["ant", "bear", "ape", "bat", "cat"]:
    grouped[word[0]].append(word)

print(dict(grouped))
