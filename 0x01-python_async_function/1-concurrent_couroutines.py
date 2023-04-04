#!/usr/bin/env python3
'''
wait_n function module
'''


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    '''
    wait_n function
    '''

    lint = []
    for i in range(n):
        lint.append(await wait_random(max_delay))
    return sorted(lint)
