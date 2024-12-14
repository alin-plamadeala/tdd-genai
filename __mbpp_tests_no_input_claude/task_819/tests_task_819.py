from solution_task_819 import count_duplic

def test_0():
    assert count_duplic([1,2,2,2,4,4,4,5,5,5,5])==([1, 2, 4, 5], [1, 3, 3, 4])

def test_1():
    assert count_duplic([2,2,3,1,2,6,7,9])==([2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1])

def test_2():
    assert count_duplic([2,1,5,6,8,3,4,9,10,11,8,12])==([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

