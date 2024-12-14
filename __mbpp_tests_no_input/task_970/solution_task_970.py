def min_of_two(a, b):
    return a if a < b else b

def test_0():
    assert min_of_two(10, 20) == 10

def test_1():
    assert min_of_two(19, 15) == 15

def test_2():
    assert min_of_two(-10, -20) == -20
