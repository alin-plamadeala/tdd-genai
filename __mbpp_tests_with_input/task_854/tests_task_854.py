from solution_task_854 import raw_heap

def test_0():
    assert raw_heap([25, 44, 68, 21, 39, 23, 89])==[21, 25, 23, 44, 39, 68, 89]

def test_1():
    assert raw_heap([25, 35, 22, 85, 14, 65, 75, 25, 58])== [14, 25, 22, 25, 35, 65, 75, 85, 58]

def test_2():
    assert raw_heap([4, 5, 6, 2])==[2, 4, 6, 5]

