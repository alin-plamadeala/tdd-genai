def sum_in_Range(l, r):
    total = 0
    for num in range(l, r + 1):
        if num % 2 != 0:
            total += num
    return total