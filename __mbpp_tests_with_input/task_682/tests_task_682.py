from solution_task_682 import mul_list

def test_0():
    assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]

def test_1():
    assert mul_list([1,2],[3,4])==[3,8]

def test_2():
    assert mul_list([90,120],[50,70])==[4500,8400]

