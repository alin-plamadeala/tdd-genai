from solution_task_804 import is_Product_Even

def test_0():
    assert is_Product_Even([1,2,3],3) == True

def test_1():
    assert is_Product_Even([1,2,1,4],4) == True

def test_2():
    assert is_Product_Even([1,1],2) == False

