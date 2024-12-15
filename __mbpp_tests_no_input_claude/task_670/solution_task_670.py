def decreasing_trend(nums):
    if len(nums) < 2:
        return True
    
    diff = nums[1] - nums[0]
    
    for i in range(1, len(nums)-1):
        curr_diff = nums[i+1] - nums[i]
        if (diff > 0 and curr_diff <= 0) or (diff < 0 and curr_diff >= 0):
            return False
        if curr_diff != 0:
            diff = curr_diff
            
    return diff > 0