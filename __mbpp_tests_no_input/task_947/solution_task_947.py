from typing import List

def len_log(strings: List[str]) -> int:
    return min(map(len, strings))
