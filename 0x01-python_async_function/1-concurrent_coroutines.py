#!/usr/bin/env python3
"""
Multiple coroutines at the same time
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    results = []
    promises = []
    for _ in range(0, n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda x: results.append(x.result()))
        promises.append(task)

    for promise in promises:
        await promise

    return results
