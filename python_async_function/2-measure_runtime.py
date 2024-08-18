#!/usr/bin/env python3
"""Module contains function that checks async run time

Imports:
    1-concurrent_coroutines: async function to check
    time: time module for getting time elapsed
    asyncio: async module
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the total runtime of running the `wait_n` function `n` times with a maximum delay of `max_delay`.
    
    Args:
        n (int): The number of times to run `wait_n`.
        max_delay (int): The maximum delay for each call to `wait_n`.
    
    Returns:
        float: The total runtime divided by the number of calls to `wait_n`.
    """
        
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


n = 5
max_delay = 9

print(measure_time(n, max_delay))