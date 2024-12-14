from solution_task_865 import ntimes_list

def test_0():
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],3)==[3, 6, 9, 12, 15, 18, 21]

def test_1():
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],4)==[4, 8, 12, 16, 20, 24, 28]

def test_2():
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],10)==[10, 20, 30, 40, 50, 60, 70]

