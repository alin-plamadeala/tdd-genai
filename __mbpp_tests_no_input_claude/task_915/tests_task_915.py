from solution_task_915 import rearrange_numbs

def test_0():
    assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10])==[2, 5, 7, 8, 9, -10, -3, -1]

def test_1():
    assert rearrange_numbs([10,15,14,13,-18,12,-20])==[10, 12, 13, 14, 15, -20, -18]

def test_2():
    assert rearrange_numbs([-20,20,-10,10,-30,30])==[10, 20, 30, -30, -20, -10]

