def coin_change(coins, m, n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for j in range(m):
        for i in range(coins[j], n + 1):
            dp[i] += dp[i - coins[j]]

    return dp[n]
