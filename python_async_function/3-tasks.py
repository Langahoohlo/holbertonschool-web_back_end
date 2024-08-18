#!/usr/bin/env python3
"""Module contains function that takes two integers

Imports:
    asyncio: module contains create_task
    wait_random: function delays for n seconds and returns n
    typing: code contains type annotations
"""
import asyncio
random_wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Asynchronously waits for a random number of seconds and returns the result as an asyncio.Task.
    
    Args:
        max_delay (int): The maximum number of seconds to wait.
    
    Returns:
        asyncio.Task: An asyncio.Task that will complete after waiting a random number of seconds between 0 and max_delay.
    """
        
    result = asyncio.create_task(random_wait(max_delay))
    return result