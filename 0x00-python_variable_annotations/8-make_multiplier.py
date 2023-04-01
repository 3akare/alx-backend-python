#!/usr/bin/env python3
'''
make_multiplier function module
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    make_multiplier function
    '''

    def inside(n: float) -> float:
        '''
        inside function
        '''

        return n * multiplier
    return inside
