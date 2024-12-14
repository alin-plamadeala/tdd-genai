from typing import List

def equilibrium_index(arr: List[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0
    
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i
        left_sum += num
    
    return -1