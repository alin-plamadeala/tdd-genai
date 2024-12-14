from solution_task_918 import coin_change

def test_0():
    assert coin_change([1, 2, 3],3,4)==4

def test_1():
    assert coin_change([4,5,6,7,8,9],6,9)==2

def test_2():
    assert coin_change([4,5,6,7,8,9],6,4)==1

