#!/usr/bin/env python3
"""Module contains function that takes two integers

Imports:
    typing: module for list type annotation
    random_wait: function delays for n seconds and returns n
"""
from typing import List
random_wait = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for n seconds, then returns a list of n floats representing the time waited for each iteration.
    
    Args:
        n (int): The number of times to wait and record the time.
        max_delay (int): The maximum number of seconds to wait for each iteration.
    
    Returns:
        List[float]: A list of n floats representing the time waited for each iteration.
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