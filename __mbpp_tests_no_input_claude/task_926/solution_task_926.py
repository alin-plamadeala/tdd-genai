def rencontres_number(n, k):
    if k > n:
        return 0
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    if n > 0:
        dp[1][0] = 0  # Base case for derangement of 1 element
        dp[1][1] = 1  # Base case for 1 element with 1 fixed point
    for i in range(2, n+1):
        dp[i][0] = (i - 1) * (dp[i-1][0] + dp[i-2][0])
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = (i - 1) * dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]
