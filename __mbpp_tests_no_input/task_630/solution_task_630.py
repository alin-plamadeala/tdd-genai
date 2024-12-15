def get_coordinates(center):
    x, y = center
    coordinates = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            coordinates.append([i, j])
    return coordinates
