def get_noOfways(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 2
    if n == 4:
        return 3
    if n == 5:
        return 5
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2
    dp[4] = 3
    dp[5] = 5
    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]
    return dp[n]
