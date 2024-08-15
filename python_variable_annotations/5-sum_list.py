#!/usr/bin/env python3
"""
    Module has a function that returns the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    sum_total = 0.0
    for i in input_list:
        sum_total += i
    return sum_total
