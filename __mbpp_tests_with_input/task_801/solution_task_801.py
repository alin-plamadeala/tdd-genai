def three_equal(a, b, c):
    count = 0
    if a == b == c:
        count = 3
    elif a == b or a == c or b == c:
        count = 2
    return count
