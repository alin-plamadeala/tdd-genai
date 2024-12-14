def max_sum_of_three_consecutive(nums, n):
    if n < 3:
        return sum(nums)
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = nums[0] + nums[1]
    dp[2] = max(dp[1], nums[1] + nums[2], nums[0] + nums[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i])
    
    return dp[n-1]