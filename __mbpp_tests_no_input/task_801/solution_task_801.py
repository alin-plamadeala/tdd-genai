def three_equal(a, b, c):
    count = 0
    if a == b:
        count += 1
    if a == c:
        count += 1
    if b == c:
        count += 1
    if count == 3:  # All three are equal
        return 3
    elif count == 1:  # Two of them are equal
        return 2
    else:  # None are equal
        return 0
