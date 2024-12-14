def find_Index(n):
    if n < 1:
        return None
    index = 1
    for i in range(1, n + 1):
        index = index * i + i
    return index
