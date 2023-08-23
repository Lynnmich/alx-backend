#!/usr/bin/env python3
""" BaseCache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching class """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_data_list[0])
                deleted_item = self.cache_data_list.pop(0)
                print("DISCARD: {}".format(deleted_item))

    def get(self, key):
        """ Get item by key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
