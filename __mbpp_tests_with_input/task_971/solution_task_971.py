def maximum_segments(n, a, b, c):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        if i >= a and dp[i - a] != -1:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i >= b and dp[i - b] != -1:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)
    return dp[n] if dp[n] != -1 else 0