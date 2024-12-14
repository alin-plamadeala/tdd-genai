from solution_task_878 import check_tuples

def test_0():
    assert check_tuples((3, 5, 6, 5, 3, 6),[3, 6, 5]) == True

def test_1():
    assert check_tuples((4, 5, 6, 4, 6, 5),[4, 5, 6]) == True

def test_2():
    assert check_tuples((9, 8, 7, 6, 8, 9),[9, 8, 1]) == False

