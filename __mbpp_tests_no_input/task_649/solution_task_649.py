from typing import List

def sum_Range_list(lst: List[int], start: int, end: int) -> int:
    if start < 0 or end >= len(lst) or start > end:
        raise ValueError("Invalid range")
    return sum(lst[start:end+1])