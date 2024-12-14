from solution_task_863 import find_longest_conseq_subseq

def test_0():
    assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3

def test_1():
    assert find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7) == 4

def test_2():
    assert find_longest_conseq_subseq([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11) == 5

