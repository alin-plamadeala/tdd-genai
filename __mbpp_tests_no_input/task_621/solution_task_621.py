from typing import List

def increment_numerics(lst: List[str], increment: int) -> List[str]:
    return [str(int(item) + increment) if item.isdigit() else item for item in lst]