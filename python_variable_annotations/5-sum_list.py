#!/usr/bin/env python3
"""
    Module has function that returns sum of two floats
"""


def sum_list(input_list: list[float]) -> float:
    """
        returns the sum of a and b

        Args:
            sum_list (float): float

        Returns:
            :param input_list:
    """
    sum_total = 0.0
    for i in input_list:
        sum_total += i
    return sum_total
