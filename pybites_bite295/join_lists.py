from functools import reduce
from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None

    return reduce(lambda x, y: x + [sep] + y, lst_of_lst)