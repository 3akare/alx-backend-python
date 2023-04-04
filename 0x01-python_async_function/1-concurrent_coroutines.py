#!/usr/bin/env python3
'''
wait_n function module
'''


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait_n function
    '''

    lint = []
    for i in range(n):
        lint.append(await wait_random(max_delay))
    return sorted(lint)
