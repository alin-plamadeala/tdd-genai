def sum_in_Range(l, r):
    return sum(num for num in range(l, r + 1) if num % 2 != 0)