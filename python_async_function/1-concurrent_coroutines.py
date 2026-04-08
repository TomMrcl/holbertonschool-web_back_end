#!/usr/bin/env python3
"""Module that provides a wait_n async function."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute n concurrent wait_random coroutines and return sorted delays.

    Args:
        n: Number of coroutines to spawn
        max_delay: Maximum delay for each coroutine

    Returns:
        List of delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    return delays
