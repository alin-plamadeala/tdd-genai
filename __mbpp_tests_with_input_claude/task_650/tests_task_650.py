from solution_task_650 import are_Equal

def test_0():
    assert are_Equal([1,2,3],[3,2,1],3,3) == True

def test_1():
    assert are_Equal([1,1,1],[2,2,2],3,3) == False

def test_2():
    assert are_Equal([8,9],[4,5,6],2,3) == False

