#!/usr/bin/env python3
'''
task_wait_random function module
'''


import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    '''
    task_wait_random function
    '''
    task = asyncio.create_task(wait_random(max_delay))
    return task
