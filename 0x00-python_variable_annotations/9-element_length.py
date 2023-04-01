#!/usr/bin/env python3
'''
element_length function module
'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    element_length function
    '''

    return [(len(i) for i in lst)]
