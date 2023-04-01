#!/usr/bin/env python3
'''
zoom_array function module
'''


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int) -> List:
    '''
    zoom_array function
    '''

    factor = int(factor)
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array, 0)

zoom_3x = zoom_array(array, 3)
