from solution_task_689 import min_jumps

def test_0():
    assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3

def test_1():
    assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3

def test_2():
    assert min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 10

