#!/usr/bin/env python3
'''
async generator function module
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    async_generator function
    '''

    await asyncio.sleep(1)
    for i in range(10):
        rand: float = random.uniform(0, 10)
        yield rand
