from solution_task_665 import move_last

def test_0():
    assert move_last([1,2,3,4]) == [2,3,4,1]

def test_1():
    assert move_last([2,3,4,1,5,0]) == [3,4,1,5,0,2]

def test_2():
    assert move_last([5,4,3,2,1]) == [4,3,2,1,5]

