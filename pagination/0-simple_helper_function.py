#!/usr/bin/env Python3
"""
    A script to return a tuple containing page and page size
"""
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
