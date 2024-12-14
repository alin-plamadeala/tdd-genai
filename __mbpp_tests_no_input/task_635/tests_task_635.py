from solution_task_635 import heap_sort

def test_0():
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_1():
    assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]

def test_2():
    assert heap_sort( [7, 1, 9, 5])==[1,5,7,9]

