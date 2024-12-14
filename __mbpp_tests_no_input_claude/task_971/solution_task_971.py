def maximum_segments(n, a, b, c):
    max_segments = 0
    for i in range(n // a + 1):
        for j in range((n - i * a) // b + 1):
            remaining = n - i * a - j * b
            if remaining >= 0 and remaining % c == 0:
                segments = i + j + remaining // c
                max_segments = max(max_segments, segments)
    return max_segments