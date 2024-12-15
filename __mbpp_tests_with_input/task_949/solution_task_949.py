from typing import List, Tuple

def sort_list(tuple_list: List[Tuple[int]]) -> str:
    return str(sorted(tuple_list, key=lambda x: sum(len(str(num)) for num in x)))