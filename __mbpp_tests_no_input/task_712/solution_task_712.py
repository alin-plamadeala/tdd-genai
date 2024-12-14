from typing import List, Any

def remove_duplicate(input_list: List[Any]) -> List[Any]:
    seen = set()
    result = []
    for item in input_list:
        item_check = tuple(item) if isinstance(item, list) else item
        if item_check not in seen:
            seen.add(item_check)
            result.append(item if not isinstance(item, list) else list(item_check))
    return result
