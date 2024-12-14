from solution_task_793 import last

def test_0():
    assert last([1,2,3],1,3) == 0

def test_1():
    assert last([1,1,1,2,3,4],1,6) == 2

def test_2():
    assert last([2,3,2,3,6,8,9],3,8) == 3

