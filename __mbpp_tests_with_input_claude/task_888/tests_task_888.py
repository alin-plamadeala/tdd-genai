from solution_task_888 import substract_elements

def test_0():
    assert substract_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((-5, -4), (1, -4), (1, 8), (-6, 7))

def test_1():
    assert substract_elements(((13, 4), (14, 6), (13, 10), (12, 11)), ((19, 8), (14, 10), (12, 2), (18, 4))) == ((-6, -4), (0, -4), (1, 8), (-6, 7))

def test_2():
    assert substract_elements(((19, 5), (18, 7), (19, 11), (17, 12)), ((12, 9), (17, 11), (13, 3), (19, 5))) == ((7, -4), (1, -4), (6, 8), (-2, 7))

