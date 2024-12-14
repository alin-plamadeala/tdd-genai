from solution_task_743 import rotate_right

def test_0():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[8, 9, 10, 1, 2, 3, 4, 5, 6]

def test_1():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

def test_2():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

