from typing import List

def min_Num(arr: List[int], n: int) -> int:
    min_greater_or_equal = float('inf')
    smallest = float('inf')
    
    for num in arr:
        if num >= n and num < min_greater_or_equal:
            min_greater_or_equal = num
        if num < smallest:
            smallest = num
    
    if min_greater_or_equal == float('inf'):
        return smallest
    
    return min_greater_or_equal