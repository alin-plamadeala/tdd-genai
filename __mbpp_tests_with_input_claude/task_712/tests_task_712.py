from solution_task_712 import remove_duplicate

def test_0():
    assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[[10, 20], [30, 56, 25], [33], [40]] 

def test_1():
    assert remove_duplicate(["a", "b", "a", "c", "c"] )==["a", "b", "c"]

def test_2():
    assert remove_duplicate([1, 3, 5, 6, 3, 5, 6, 1] )==[1, 3, 5, 6]

