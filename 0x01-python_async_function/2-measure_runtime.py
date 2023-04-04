#!/usr/bin/env python3
'''
measure_time function module
'''


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measure_time function
    '''

    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    elasped = time.time() - s
    return (elasped/n)
