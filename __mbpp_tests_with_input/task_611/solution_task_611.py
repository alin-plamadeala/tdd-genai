from typing import List, Tuple

def max_of_nth(tuple_list: List[Tuple[int, ...]], n: int) -> int:
    return max(row[n] for row in tuple_list)