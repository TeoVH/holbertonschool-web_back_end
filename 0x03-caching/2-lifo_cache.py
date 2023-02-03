#!/usr/bin/env python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.last_key_added = str()

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm
        """
        if key and item:
            if self.cache_data.get(key):
                self.cache_data[key] = item
                self.last_key_added = key
            else:
                if self.MAX_ITEMS > 0:
                    self.cache_data[key] = item
                    self.last_key_added = key
                    self.MAX_ITEMS -= 1

                else:
                    print(f"DISCARD: {self.last_key_added}")
                    self.cache_data.pop(self.last_key_added)
                    self.cache_data[key] = item
                    self.last_key_added = key

    def get(self, key):
        """
        Get an item by key
        """
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
