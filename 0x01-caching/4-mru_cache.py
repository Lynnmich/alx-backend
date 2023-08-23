#!/usr/bin/env python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching class """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                length = len(self.cache_data_list)
                popped_item = self.cache_data_list.pop(length)
                del self.cache_data[popped_item]
                print("DISCARD: {}".format(str(popped_item)))

    def get(self, key):
        """ Get item by key """
        if key in self.cache_data:
            self.cache_data_list.remove(key)
            self.cache_data_list.append(key)
            return self.cache_data[key]
        return None
