from solution_task_842 import get_odd_occurence

def test_0():
    assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5

def test_1():
    assert get_odd_occurence([1, 2, 3, 2, 3, 1, 3], 7) == 3

def test_2():
    assert get_odd_occurence([5, 7, 2, 7, 5, 2, 5], 7) == 5

