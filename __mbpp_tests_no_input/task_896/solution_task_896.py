from typing import List, Tuple

def sort_list_last(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return sorted(lst, key=lambda x: x[1])