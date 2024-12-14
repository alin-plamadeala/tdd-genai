def max_sum_of_three_consecutive(nums, n):
    if n < 3:
        return sum(nums)
    
    max_sum = current_sum = sum(nums[:3])
    
    for i in range(3, n):
        current_sum = current_sum - nums[i-3] + nums[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum