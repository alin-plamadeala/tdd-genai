def geometric_sum(n):
    result = 0
    for i in range(n):
        result += 1 / (2 ** (i+1))
    return 1 + result