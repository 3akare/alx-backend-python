#!/usr/bin/env python3
'''
to_kv fcuntion module
'''


from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    to_kv function
    '''

    return (k, v**2)
