from itertools import count

def lucky_num(n):
    lucky_numbers = []
    sieve = list(range(1, n*10, 2))  # Start with odd numbers only
    index = 1  # Start with the second number (index 1)

    while len(lucky_numbers) < n:
        if index >= len(sieve):
            break
        step = sieve[index]
        sieve = [num for i, num in enumerate(sieve) if (i + 1) % step != 0]
        index += 1

    lucky_numbers = sieve[:n]
    return lucky_numbers