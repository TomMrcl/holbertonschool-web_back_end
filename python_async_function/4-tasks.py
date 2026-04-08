#!/usr/bin/env python3
"""Module that provides a task_wait_n async function."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute n task_wait_random tasks and return sorted delays.

    Args:
        n: Number of tasks to spawn
        max_delay: Maximum delay for each task

    Returns:
        List of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    return delays
