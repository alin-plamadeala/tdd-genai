def left_rotate(s, n):
    n = n % len(s)
    return s[n:] + s[:n]
