def mul_consecutive_nums(nums):
    if not nums or len(nums) < 2:
        return []
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] * nums[i + 1])
    return result
