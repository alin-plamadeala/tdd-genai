def is_polite(n):
    count = 0
    num = 1
    while count < n:
        if num & (num - 1) != 0:  # Check if num is not a power of 2
            count += 1
        num += 1
    return num - 1
