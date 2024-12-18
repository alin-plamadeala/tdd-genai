from typing import List

def div_of_nums(numbers: List[int], m: int, n: int) -> List[int]:
    return list(filter(lambda x: x % m == 0 and x % n == 0, numbers))