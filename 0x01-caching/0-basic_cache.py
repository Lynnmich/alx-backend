#!/usr/bin/python3
""" BaseCache module """
from base_caching import BaseCaching


class BaseCache(BaseCaching):
    """ BaseCache class that inherits from BaseCaching class """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get item by key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
