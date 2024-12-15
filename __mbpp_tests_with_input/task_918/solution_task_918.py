def coin_change(coins, n, target):
    # dp[i] will store the number of ways to make value i
    dp = [0] * (target + 1)
    dp[0] = 1  # There is 1 way to make the value 0 (using no coins)

    # Iterate over each coin
    for coin in coins:
        # Update dp array for all values >= coin
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]
