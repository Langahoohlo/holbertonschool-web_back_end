#!/usr/bin/env python3
"""Module contains function that takes two integers

Imports:
    List: module for list type annotation
    wait_random: function delays for n seconds and returns n
"""
from typing import List
random_wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): number of random
        max_delay (number of seconds to delay)

    Returns:
        List[float]: list of wait random returns
    """

    my_list: List[float] = []
    i: int = 0

    while i < n:
        result = await random_wait(max_delay)
        my_list.append(result)
        i += 1

    for end in range(len(my_list), 1, -1):
        for j in range(1, end):
            if my_list[j - 1] > my_list[j]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
    return my_list
