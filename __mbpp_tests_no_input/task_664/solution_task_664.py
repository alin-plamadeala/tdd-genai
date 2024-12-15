def average_Even(n):
    if n < 2:
        return 0
    even_numbers = [i for i in range(2, n + 1) if i % 2 == 0]
    return sum(even_numbers) // len(even_numbers)
