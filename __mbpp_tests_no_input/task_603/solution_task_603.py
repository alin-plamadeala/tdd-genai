def get_ludic(n):
    if n < 1:
        return []
    
    ludics = list(range(1, n + 1))
    idx = 1
    while idx < len(ludics):
        step = ludics[idx]
        ludics = [num for i, num in enumerate(ludics) if (i + 1) % step != 0 or i == 0]
        idx += 1
    return ludics
