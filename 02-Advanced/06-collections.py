from collections import defaultdict, Counter, deque, namedtuple, OrderedDict

# 1. defaultdict  (most used)
# automatically creates a default value for missing keys

word_count = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
    word_count[word] += 1
print(dict(word_count))   # {'apple': 3, 'banana': 2, 'cherry': 1}

# group items by first letter
grouped = defaultdict(list)
for word in ["ant", "bear", "ape", "bat", "cat"]:
    grouped[word[0]].append(word)
print(dict(grouped))      # {'a': ['ant', 'ape'], 'b': ['bear', 'bat'], 'c': ['cat']}

# nested defaultdict
nested = defaultdict(lambda: defaultdict(int))
nested["fruits"]["apple"] += 5
nested["fruits"]["banana"] += 3
print(dict(nested["fruits"]))  # {'apple': 5, 'banana': 3}


# 2. Counter  (most used)
# counts hashable objects; subclass of dict

c = Counter("mississippi")
print(c)                          # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(c.most_common(3))           # [('i', 4), ('s', 4), ('p', 2)]
print(c["s"])                     # 4
print(c["z"])                     # 0  (no KeyError)

# arithmetic
c1 = Counter(a=3, b=2, c=1)
c2 = Counter(a=1, b=4, d=2)
print(c1 + c2)                    # Counter({'b': 6, 'a': 4, 'd': 2, 'c': 1})
print(c1 - c2)                    # Counter({'a': 2, 'c': 1})
print(c1 & c2)                    # intersection (min): Counter({'a': 1, 'b': 2})
print(c1 | c2)                    # union (max):        Counter({'b': 4, 'a': 3, 'd': 2, 'c': 1})

# count words in a sentence
words = "the cat sat on the mat the cat".split()
print(Counter(words).most_common(2))   # [('the', 3), ('cat', 2)]


# 3. deque  (double-ended queue)
# O(1) appends and pops from both ends; use instead of list for queues/stacks

d = deque([1, 2, 3])
d.append(4)        # add to right
d.appendleft(0)    # add to left
print(d)           # deque([0, 1, 2, 3, 4])

d.pop()            # remove from right -> 4
d.popleft()        # remove from left  -> 0
print(d)           # deque([1, 2, 3])

d.extend([4, 5])
d.extendleft([-1, -2])   # each item prepended -> reverses order
print(d)           # deque([-2, -1, 1, 2, 3, 4, 5])

d.rotate(2)        # rotate right by 2
print(d)           # deque([4, 5, -2, -1, 1, 2, 3])

# bounded deque — keeps only the last N items
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)
print(recent)      # deque([3, 4, 5], maxlen=3)


# ─────────────────────────────────────────────
# 4. namedtuple
# ─────────────────────────────────────────────
# Lightweight, immutable data class; memory-efficient like a tuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)        # 3 4
print(p[0], p[1])      # 3 4  (index access still works)
print(p._asdict())     # {'x': 3, 'y': 4}

# Default values (Python 3.6.1+)
Employee = namedtuple("Employee", ["name", "dept", "salary"], defaults=["Engineering", 50000])
e = Employee("Alice")
print(e)               # Employee(name='Alice', dept='Engineering', salary=50000)

# Replace a field (returns a new instance)
p2 = p._replace(x=10)
print(p2)              # Point(x=10, y=4)

# Unpack like a regular tuple
x, y = p
print(x, y)            # 3 4


# ─────────────────────────────────────────────
# 5. OrderedDict
# ─────────────────────────────────────────────
# Remembers insertion order (relevant pre-3.7; still useful for move_to_end / LRU)

od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3
print(list(od.keys()))      # ['one', 'two', 'three']

# move_to_end — unique to OrderedDict
od.move_to_end("one")       # move to last
print(list(od.keys()))      # ['two', 'three', 'one']

od.move_to_end("one", last=False)   # move to first
print(list(od.keys()))      # ['one', 'two', 'three']

# Order matters for equality (unlike regular dict)
d1 = OrderedDict([("a", 1), ("b", 2)])
d2 = OrderedDict([("b", 2), ("a", 1)])
print(d1 == d2)             # False

# Simple LRU cache pattern using OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

lru = LRUCache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
lru.get("a")        # access "a" -> moves to end
lru.put("d", 4)     # evicts "b" (least recently used)
print(list(lru.cache.keys()))   # ['c', 'a', 'd']

