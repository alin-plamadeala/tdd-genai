from solution_task_801 import three_equal

def test_0():
    assert three_equal(1,1,1) == 3

def test_1():
    assert three_equal(-1,-2,-3) == 0

def test_2():
    assert three_equal(1,2,2) == 2

