#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
"""


from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: Function to generate 10 random floats

    Yields:
        Iterator[AsyncGenerator[float, None]]: 
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
