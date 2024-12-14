from solution_task_942 import check_element

def test_0():
    assert check_element((4, 5, 7, 9, 3),  [6, 7, 10, 11]) == True

def test_1():
    assert check_element((1, 2, 3, 4),  [4, 6, 7, 8, 9]) == True

def test_2():
    assert check_element((3, 2, 1, 4, 5),  [9, 8, 7, 6]) == False

