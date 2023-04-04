#!/usr/bin/env python3
'''
measure_runtime function module
'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure_runtime function
    '''

    start: float = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    elapsed_time: float = time.time() - start
    return elapsed_time
