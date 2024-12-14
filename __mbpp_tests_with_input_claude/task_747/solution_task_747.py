def lcs_of_three(X, Y, Z, l, m, n):
    L = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(l+1)]
    
    for i in range(l+1):
        for j in range(m+1):
            for k in range(n+1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0
                elif X[i-1] == Y[j-1] == Z[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1])
    
    return L[l][m][n]