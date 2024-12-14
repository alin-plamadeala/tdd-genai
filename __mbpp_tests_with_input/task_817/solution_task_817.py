from typing import List

def div_of_nums(numbers: List[int], div1: int, div2: int) -> List[int]:
    return [num for num in numbers if num % div1 == 0 or num % div2 == 0]