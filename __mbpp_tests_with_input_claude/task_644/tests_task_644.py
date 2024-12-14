from solution_task_644 import reverse_Array_Upto_K

def test_0():
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]

def test_1():
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]

def test_2():
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

