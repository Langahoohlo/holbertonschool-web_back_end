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
        max_delay (intnumber of seceonds to delay

    Returns:
        List[float]: list of wait random returns
    """
    myList: List[float] = []
    i: int = 0

    while i < n:
        result = await random_wait(max_delay)
        myList.append(result)
        i += 1

    for end in range(len(myList), 1, -1):
        for j in range(1, end):
            if myList[j - 1] > myList[j]:
                myList[j - 1], myList[j] = myList[j], myList[j - 1]
    return myList