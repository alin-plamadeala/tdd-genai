def min_sum_path(triangle):
    n = len(triangle)
    dp = triangle[-1]
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    
    return dp[0]