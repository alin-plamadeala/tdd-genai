from typing import Tuple, Any

def remove_nested(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    result = []
    for item in t:
        if not isinstance(item, tuple):
            result.append(item)
    return tuple(result)