from solution_task_680 import increasing_trend

def test_0():
    assert increasing_trend([1,2,3,4]) == True

def test_1():
    assert increasing_trend([4,3,2,1]) == False

def test_2():
    assert increasing_trend([0,1,4,9]) == True

