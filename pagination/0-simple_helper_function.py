#!/usr/bin/env python3
"""
Module for index_range helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page: page number (1-indexed)
        page_size: number of items per page

    Returns:
        tuple: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
