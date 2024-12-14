from solution_task_670 import decreasing_trend

def test_0():
    assert decreasing_trend([-4,-3,-2,-1]) == True

def test_1():
    assert decreasing_trend([1,2,3]) == True

def test_2():
    assert decreasing_trend([3,2,1]) == False

