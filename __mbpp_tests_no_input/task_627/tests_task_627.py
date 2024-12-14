from solution_task_627 import find_First_Missing

def test_0():
    assert find_First_Missing([0,1,2,3],0,3) == 4

def test_1():
    assert find_First_Missing([0,1,2,6,9],0,4) == 3

def test_2():
    assert find_First_Missing([2,3,5,8,9],0,4) == 0

