#!/usr/bin/env python3
"""
this script contains a method get_page that takes two integer arguments page
 with default value 1 and page_size with default value 10
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this method takes two args and returns tuple
    of size two containing the start and end indices
    """
    start_index = 0
    end_index = 0
    for i in range(page):
        start_index = end_index
        end_index += page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """this function takes 2 int args page = 1 and page_size = 10 and
        return appropriate page of the dataset
        """
        assert type(page) == int and type(page_size) == int and\
            page > 0 and page_size > 0
        data = self.dataset()
        try:
            index = index_range(page, page_size)
            return data[index[0]: index[1]]
        except IndexError:
            return []
