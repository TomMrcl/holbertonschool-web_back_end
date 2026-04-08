#!/usr/bin/env python3
"""Module that provides a floor function with type annotations."""

import math


def floor(n: float) -> int:
    """Return the floor of a float.

    Args:
        n: A float number

    Returns:
        The floor of n as an int
    """
    return math.floor(n)
