#!/usr/bin/env python3

import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def __str__(self):
      for key in self.cache.keys():
          print('%d -> %d' % (key,self.cache[key]))

cache = LRUCache(2)
cache.set(1,10)
cache.set(5,12)
print(cache.get(5))
print(cache.get(1))
print(cache.get(10))
cache.set(6,14)
print(cache.get(5))
print(cache)
