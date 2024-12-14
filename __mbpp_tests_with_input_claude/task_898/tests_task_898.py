from solution_task_898 import extract_elements

def test_0():
    assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]

def test_1():
    assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]

def test_2():
    assert extract_elements([0,0,0,0,0],5)==[0]

