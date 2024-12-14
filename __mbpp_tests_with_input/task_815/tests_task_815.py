from solution_task_815 import sort_by_dnf

def test_0():
    assert sort_by_dnf([1,2,0,1,0,1,2,1,1], 9) == [0, 0, 1, 1, 1, 1, 1, 2, 2]

def test_1():
    assert sort_by_dnf([1,0,0,1,2,1,2,2,1,0], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

def test_2():
    assert sort_by_dnf([2,2,1,0,0,0,1,1,2,1], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

