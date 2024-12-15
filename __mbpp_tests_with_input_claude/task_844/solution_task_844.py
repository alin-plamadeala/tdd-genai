def get_Number(n, k):
    odd = []
    even = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    result = odd + even
    return result[k - 1]