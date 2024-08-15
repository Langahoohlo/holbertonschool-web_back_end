#!/usr/bin/env python3
"""Module contains a function that returns a list of tuples,
   where each tuple contains a sequence and its length.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function returns a list of tuples, where each tuple contains
       a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., lists, strings, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
