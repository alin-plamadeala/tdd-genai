def min_Jumps(x, y, d):
    distance = (x**2 + y**2)**0.5
    if d == 0:
        return 0 if distance == 0 else float('inf')
    jumps = distance / d
    return jumps
