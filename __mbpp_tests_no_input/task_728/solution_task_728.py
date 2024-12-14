from typing import List

def sum_list(list1: List[int], list2: List[int]) -> List[int]:
    return [x + y for x, y in zip(list1, list2)]