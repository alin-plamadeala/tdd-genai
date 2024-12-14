def min_Jumps(x, y, d):
    if d <= x:
        return 0
    distance_to_cover = d - x
    jump_distance = y - x
    if jump_distance >= distance_to_cover:
        return 1
    jumps = distance_to_cover / jump_distance
    return max(1, jumps)