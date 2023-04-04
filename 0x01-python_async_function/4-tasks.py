#!/usr/bin/env python3
'''
task_wait_n function module
'''


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait_n function
    '''

    lint = []
    for i in range(n):
        lint.append(await task_wait_random(max_delay))
    return sorted(lint)
