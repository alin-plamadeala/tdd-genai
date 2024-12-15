from typing import Tuple

def str_to_tuple(input_str: str) -> Tuple[int, ...]:
    return tuple(map(int, input_str.split(", ")))