#!/usr/bin/env Python3
"""
    A script to return a tuple containing page and page size
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function o fthe module

    Args:
        page (_type_): page index
        page_size (_type_): page size of items to display

    Returns:
        _type_: A tiple of both page and page size
    """
    start = (page - 1) * page_size
    end = page * page_size
    page_tuple = (start, end)
    return page_tuple



class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert page > 0
        assert page_size > 0
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        myRange = index_range(page, page_size)
        start = myRange[0]
        end = myRange[1]
        filtered_list = self.dataset()

        if start >= len(filtered_list):
            return []
        return filtered_list[start:end]
    