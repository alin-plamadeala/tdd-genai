def coin_change(coins, m, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(m):
        for j in range(coins[i], n + 1):
            dp[j] += dp[j - coins[i]]
            
    return dp[n]