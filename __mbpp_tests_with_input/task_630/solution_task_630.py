def get_coordinates(coord):
    x, y = coord
    adjacent_coordinates = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            adjacent_coordinates.append([i, j])
    return adjacent_coordinates
