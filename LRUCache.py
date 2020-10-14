from collections import OrderedDict

class LRU:
    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.length = 0

    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self,val):
        self.cache[val]=val
        self.cache.move_to_end(val)
        self.length+=1
        if self.length > self.capacity:
            self.cache.popitem(last=False)
            self.length-=1
        
lru = LRU(2)
lru.put(1)
lru.put(2)
print(lru.get(1))
lru.put(3)
print(lru.get(1))
lru.put(4)
print(lru.cache)