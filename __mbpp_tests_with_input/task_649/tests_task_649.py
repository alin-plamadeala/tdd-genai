from solution_task_649 import sum_Range_list

def test_0():
    assert sum_Range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12],8,10) == 29

def test_1():
    assert sum_Range_list([1,2,3,4,5],1,2) == 5

def test_2():
    assert sum_Range_list([1,0,1,2,5,6],4,5) == 11

