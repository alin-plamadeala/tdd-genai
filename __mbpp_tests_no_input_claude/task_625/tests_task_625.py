from solution_task_625 import swap_List

def test_0():
    assert swap_List([1,2,3]) == [3,2,1]

def test_1():
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]

def test_2():
    assert swap_List([4,5,6]) == [6,5,4]

