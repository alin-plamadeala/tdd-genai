def largest_subset(nums, n):
    nums.sort()
    dp = [1] * n
    max_len = 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    
    return max_len