from solution_task_890 import find_Extra

def test_0():
    assert find_Extra([1,2,3,4],[1,2,3],3) == 3

def test_1():
    assert find_Extra([2,4,6,8,10],[2,4,6,8],4) == 4

def test_2():
    assert find_Extra([1,3,5,7,9,11],[1,3,5,7,9],5) == 5

