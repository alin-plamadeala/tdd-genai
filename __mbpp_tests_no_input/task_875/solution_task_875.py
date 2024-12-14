from typing import List, Tuple

def min_difference(pairs: List[Tuple[int, int]]) -> int:
    differences = [abs(a - b) for a, b in pairs]
    return min(differences)