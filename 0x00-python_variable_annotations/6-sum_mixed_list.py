#!/usr/bin/env python3
'''
sum_mixed_list function module
'''


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sum_mixed_list function
    '''
    add: float = 0
    for i in mxd_lst:
        add += i
    return add
