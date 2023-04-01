#!/usr/bin/env python3
'''
safe_first_element function module
'''


from typing import Sequence, Union, Any, List


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    safe_first_element function
    '''

    if lst:
        return lst[0]
    else:
        return None
