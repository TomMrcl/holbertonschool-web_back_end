#!/usr/bin/env python3
"""Module that provides a make_multiplier function with type annotations."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier: A float to use as the multiplier

    Returns:
        A function that takes a float and returns its product with multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
