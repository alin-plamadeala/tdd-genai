from functools import lru_cache

def super_seq(X, Y, m, n):
    @lru_cache(None)
    def lcs(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if X[i-1] == Y[j-1]:
            return 1 + lcs(i-1, j-1)
        return 1 + min(lcs(i-1, j), lcs(i, j-1))
    
    return lcs(m, n)