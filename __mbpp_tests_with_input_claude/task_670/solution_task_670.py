def decreasing_trend(nums):
    if len(nums) < 2:
        return True
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return False
    return True