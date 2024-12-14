from solution_task_718 import alternate_elements

def test_0():
    assert alternate_elements(["red", "black", "white", "green", "orange"])==['red', 'white', 'orange']

def test_1():
    assert alternate_elements([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])==[2, 3, 0, 8, 4]

def test_2():
    assert alternate_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]

