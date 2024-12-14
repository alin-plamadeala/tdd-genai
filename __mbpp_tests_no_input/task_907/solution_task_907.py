from itertools import count

def lucky_num(n):
    lucky_numbers = []
    sieve = list(range(1, n*4, 2))  # Generate odd numbers up to a reasonable limit
    for step in count(1):
        if step >= len(sieve):
            break
        step_value = sieve[step]
        sieve = [num for i, num in enumerate(sieve) if (i + 1) % step_value != 0]
    lucky_numbers = sieve[:n]
    return lucky_numbers