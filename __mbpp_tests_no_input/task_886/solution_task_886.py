from typing import Tuple

def sum_num(numbers: Tuple[int, ...]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0