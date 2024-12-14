from solution_task_699 import min_Swaps

def test_0():
    assert min_Swaps("1101","1110") == 1

def test_1():
    assert min_Swaps("1111","0100") == "Not Possible"

def test_2():
    assert min_Swaps("1110000","0001101") == 3

