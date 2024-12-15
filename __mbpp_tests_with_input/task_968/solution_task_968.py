def floor_Max(a, b, c):
    smallest = min(a, b, c)
    candidates = [x for x in (a, b, c) if x < smallest]
    return max(candidates) if candidates else smallest
