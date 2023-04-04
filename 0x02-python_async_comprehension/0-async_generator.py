#!/usr/bin/env python3
'''
async generator function module
'''


import asyncio
import random


async def async_generator():
    '''
    async_generator function
    '''

    await asyncio.sleep(1)
    for i in range(10):
        rand: float = random.uniform(0, 10)
        yield rand
