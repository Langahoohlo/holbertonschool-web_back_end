#!/usr/bin/env python3
"""Run time for four parallel comprehension"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measuring runtime
    """
    time.starttime = time.time()
    await asyncio.gather(async_comprehension())
    time.endtime = time.time()
    return time.endtime - time.starttime
