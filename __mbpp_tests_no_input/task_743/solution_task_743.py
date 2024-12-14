def rotate_right(lst, n, m):
    total_rotation = n % len(lst)
    rotated = lst[-total_rotation:] + lst[:-total_rotation]
    result = rotated[-m:] + rotated[:-m]
    return result

def test_0():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4) == [8, 9, 10, 1, 2, 3, 4, 5, 6]

def test_1():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 2) == [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

def test_2():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 2) == [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]