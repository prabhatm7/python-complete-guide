from collections import OrderedDict

# keeps insertion order and supports move_to_end
od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3
print(list(od.keys()))

od.move_to_end("one")
print(list(od.keys()))

# simple LRU style use
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

lru = LRUCache(2)
lru.put("a", 1)
lru.put("b", 2)
lru.get("a")
lru.put("c", 3)
print(list(lru.cache.keys()))
