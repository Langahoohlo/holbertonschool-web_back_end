#!/usr/bin/env python3
"""
    Module has a function that returns the sum of a list of floats.
"""
from typing import List, Union


def to_kv(k: str, v: [Union[int, float]]) -> tuple:
    """Function takes to args and returns them in tuple

    Args:
        k (str): string arg
        v (int): int OR float arg

    Returns:
        tuple[str, int]: _description_
    """
    return k, v ** 2
