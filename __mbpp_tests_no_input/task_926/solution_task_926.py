def rencontres_number(n, k):
    if k > n:
        return 0
    if k == 0:
        if n == 0:
            return 1
        derangements = [0] * (n + 1)
        derangements[0] = 1
        if n > 0:
            derangements[1] = 0
        for i in range(2, n + 1):
            derangements[i] = (i - 1) * (derangements[i - 1] + derangements[i - 2])
        return derangements[n]
    
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(0, min(i, k)+1):
            if j == 0:
                dp[i][j] = (i - 1) * dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
    return dp[n][k]
