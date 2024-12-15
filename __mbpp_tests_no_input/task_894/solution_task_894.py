from typing import Tuple

def float_to_tuple(input_string: str) -> Tuple[float, ...]:
    return tuple(map(float, input_string.split(", ")))