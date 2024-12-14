from solution_task_940 import heap_sort

def test_0():
    assert heap_sort([12, 2, 4, 5, 2, 3]) == [2, 2, 3, 4, 5, 12]

def test_1():
    assert heap_sort([32, 14, 5, 6, 7, 19]) == [5, 6, 7, 14, 19, 32]

def test_2():
    assert heap_sort([21, 15, 29, 78, 65]) == [15, 21, 29, 65, 78]

