from solution_task_648 import exchange_elements

def test_0():
    assert exchange_elements([0,1,2,3,4,5])==[1, 0, 3, 2, 5, 4] 

def test_1():
    assert exchange_elements([5,6,7,8,9,10])==[6,5,8,7,10,9] 

def test_2():
    assert exchange_elements([25,35,45,55,75,95])==[35,25,55,45,95,75] 

