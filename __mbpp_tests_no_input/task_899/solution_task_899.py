from typing import List

def check(arr: List[int], target: int) -> bool:
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == target:
                return True
    return False