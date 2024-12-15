def geometric_sum(n):
    if n == 1:
        return 1
    return 1/(2**(n-1)) + geometric_sum(n-1)