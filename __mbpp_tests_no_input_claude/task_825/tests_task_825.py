from solution_task_825 import access_elements

def test_0():
    assert access_elements([2,3,8,4,7,9],[0,3,5]) == [2, 4, 9]

def test_1():
    assert access_elements([1, 2, 3, 4, 5],[1,2]) == [2,3]

def test_2():
    assert access_elements([1,0,2,3],[0,1]) == [1,0]

