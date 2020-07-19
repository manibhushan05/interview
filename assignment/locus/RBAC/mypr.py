from collections import OrderedDict


class LRUCache:

    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()
    def get_cache(self):
        return self.cache
    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


cache = LRUCache(2)
cache.put(1, 2)
cache.put(2, 2)

print(cache.get(1))

