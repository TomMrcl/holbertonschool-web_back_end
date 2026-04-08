#!/usr/bin/env python3
"""Module that provides an element_length function with type annotations."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with sequence elements and their lengths.

    Args:
        lst: An iterable of sequences

    Returns:
        A list of tuples containing each sequence and its length
    """
    return [(i, len(i)) for i in lst]
