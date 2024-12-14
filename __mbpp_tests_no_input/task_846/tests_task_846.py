from solution_task_846 import find_platform

def test_0():
    assert find_platform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000],6)==3

def test_1():
    assert find_platform([100,200,300,400],[700,800,900,1000],4)==4

def test_2():
    assert find_platform([5,6,7,8],[4,3,2,1],4)==1

