from solution_task_695 import check_greater

def test_0():
    assert check_greater((10, 4, 5), (13, 5, 18)) == True

def test_1():
    assert check_greater((1, 2, 3), (2, 1, 4)) == False

def test_2():
    assert check_greater((4, 5, 6), (5, 6, 7)) == True

