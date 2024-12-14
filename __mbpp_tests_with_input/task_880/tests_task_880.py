from solution_task_880 import Check_Solution

def test_0():
    assert Check_Solution(2,5,2) == "2 solutions"

def test_1():
    assert Check_Solution(1,1,1) == "No solutions"

def test_2():
    assert Check_Solution(1,2,1) == "1 solution"

