#!/usr/bin/env python3
"""Module contains function that returns pagination range
Imports:
    Tuple: Tuple type annotation from typing module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function returns pagination range in the form of tuple

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple[int, int]: start to end range
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size

    return (start, end)