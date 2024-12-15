def min_k(data, k):
    if not isinstance(data, list) or not all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], (int, float)) for item in data):
        raise ValueError("Input data must be a list of tuples with the second element as a number.")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")
    sorted_data = sorted(data, key=lambda x: x[1])
    return sorted_data[:k]
