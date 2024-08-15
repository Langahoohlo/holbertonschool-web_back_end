#!/usr/bin/env python3
"""Module contains a function that takes a float multiplier
    as an argument and returns a function that multiplies a float by the
    multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.
    """
    def multiply(f: float) -> float:
        """Multiplies the given float by the multiplier.

        Args:
            f (float): The float value to be multiplied by the multiplier.

        Returns:
            float: The product of the float and the multiplier.
        """
        return f * multiplier

    return multiply
