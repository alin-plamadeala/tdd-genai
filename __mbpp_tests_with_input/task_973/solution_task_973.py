def left_rotate(string, n):
    n = n % len(string)  # Handle cases where n is larger than the string length
    return string[n:] + string[:n]
