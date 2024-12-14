from solution_task_883 import div_of_nums

def test_0():
    assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],2,4)==[ 152,44]

def test_1():
    assert div_of_nums([1, 2, 3, 5, 7, 8, 10],2,5)==[10]

def test_2():
    assert div_of_nums([10,15,14,13,18,12,20],10,5)==[10,20]

