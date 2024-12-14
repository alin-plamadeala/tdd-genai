from solution_task_852 import remove_negs

def test_0():
    assert remove_negs([1,-2,3,-4]) == [1,3]

def test_1():
    assert remove_negs([1,2,3,-4]) == [1,2,3]

def test_2():
    assert remove_negs([4,5,-6,7,-8]) == [4,5,7]

