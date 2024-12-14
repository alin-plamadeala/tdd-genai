from solution_task_972 import concatenate_nested

def test_0():
    assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)

def test_1():
    assert concatenate_nested((1, 2), (3, 4)) == (1, 2, 3, 4)

def test_2():
    assert concatenate_nested((4, 5), (6, 8)) == (4, 5, 6, 8)

