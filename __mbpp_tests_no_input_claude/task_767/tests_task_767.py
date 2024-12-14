from solution_task_767 import get_Pairs_Count

def test_0():
    assert get_Pairs_Count([1,1,1,1],4,2) == 6

def test_1():
    assert get_Pairs_Count([1,5,7,-1,5],5,6) == 3

def test_2():
    assert get_Pairs_Count([1,-2,3],3,1) == 1

