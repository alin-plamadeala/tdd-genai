def get_Number(n, k):
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
    even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]
    combined = odd_numbers + even_numbers
    return combined[k - 1]
