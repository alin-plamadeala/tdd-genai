def lcs_of_three(X, Y, Z, m, n, o):
    dp = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif X[i-1] == Y[j-1] == Z[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    return dp[m][n][o]
