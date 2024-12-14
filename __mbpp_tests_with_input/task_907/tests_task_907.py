from solution_task_907 import lucky_num

def test_0():
    assert lucky_num(10)==[1, 3, 7, 9, 13, 15, 21, 25, 31, 33] 

def test_1():
    assert lucky_num(5)==[1, 3, 7, 9, 13]

def test_2():
    assert lucky_num(8)==[1, 3, 7, 9, 13, 15, 21, 25]

