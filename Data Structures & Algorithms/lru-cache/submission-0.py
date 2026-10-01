from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as Most Recently Used (MRU)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark it as MRU
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
            
        self.cache[key] = value
        # If capacity is exceeded, pop the first item (Least Recently Used)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
