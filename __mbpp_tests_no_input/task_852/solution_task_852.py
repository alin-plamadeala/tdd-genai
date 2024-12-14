from typing import List

def remove_negs(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num >= 0]