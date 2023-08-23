#!/usr/bin/env python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching class """
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
                second_last_key = len(self.cache_ata_list) - 2
                last_key = self.cache_data_list.pop(second_last_key)
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """ Get item by key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
