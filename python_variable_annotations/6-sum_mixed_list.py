#!/usr/bin/env python3
"""
    Module has a function that returns the sum of a list of floats.
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        mxd_lst (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    float_total = 0.0
    for i in mxd_lst:
        float_total += i
    return float_total
