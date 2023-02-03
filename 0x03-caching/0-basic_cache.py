#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    implementing put and get methods
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
