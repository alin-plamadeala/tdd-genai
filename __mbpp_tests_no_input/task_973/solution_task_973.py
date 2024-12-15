def left_rotate(s, n):
    if not isinstance(s, str) or not isinstance(n, int):
        raise ValueError("Input must be a string and an integer")
    n = n % len(s)  # Handle cases where n is greater than the length of the string
    return s[n:] + s[:n]
