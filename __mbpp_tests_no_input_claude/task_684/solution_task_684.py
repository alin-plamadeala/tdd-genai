def count_Char(s, c):
    count = 0
    for i, char in enumerate(s):
        if char == c:
            count += i + 1
    count += len(s)
    return count