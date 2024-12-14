def is_polite(n):
    count = 0
    current = n + 1
    while count < 2:
        if sum(range(1, current + 1)) % current == 0:
            count += 1
        current += 1
    return current - 1