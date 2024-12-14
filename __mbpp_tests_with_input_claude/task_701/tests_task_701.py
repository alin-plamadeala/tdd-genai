from solution_task_701 import equilibrium_index

def test_0():
    assert equilibrium_index([1, 2, 3, 4, 1, 2, 3]) == 3

def test_1():
    assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3

def test_2():
    assert equilibrium_index([1, 2, 3]) == -1

