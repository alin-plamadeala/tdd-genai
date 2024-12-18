def maxAverageOfPath(matrix, n):
    dp = [[0.0] * n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    return round(dp[n-1][n-1] / (2*n - 1), 1)