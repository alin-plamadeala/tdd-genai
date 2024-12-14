from typing import List, Tuple

def sort_list(lst: List[Tuple[int, ...]]) -> str:
    sorted_lst = sorted(lst, key=lambda x: (len(x), x))
    return f"'{str(sorted_lst)}'"