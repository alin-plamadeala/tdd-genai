def move_zero(nums):
    non_zero = [num for num in nums if num != 0]
    zeros = [0] * (len(nums) - len(non_zero))
    return non_zero + zeros