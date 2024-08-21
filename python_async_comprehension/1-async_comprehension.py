from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    numbers = [num async for num in async_generator()]
    return numbers
