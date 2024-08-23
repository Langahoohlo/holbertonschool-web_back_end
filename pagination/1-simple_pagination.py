#!/usr/bin/env python3
"""Module contains function that returns pagination range
Imports:
    Tuple: Tuple type annotation
    List: List type anotaton
    csv: csv module
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function returns pagination range

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple[int, int]: start to end range
    """
    start = (page - 1) * page_size
    end = page * page_size

    return ((start, end))


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
        """Gets specific data
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