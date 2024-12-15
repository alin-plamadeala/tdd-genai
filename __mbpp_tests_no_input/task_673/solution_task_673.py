from typing import List

def convert(numbers: List[int]) -> int:
    return int("".join(map(str, numbers)))