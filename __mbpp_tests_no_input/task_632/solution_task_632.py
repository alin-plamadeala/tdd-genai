from typing import List

def move_zero(nums: List[int]) -> List[int]:
    non_zero = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zero))
    return non_zero + zeros