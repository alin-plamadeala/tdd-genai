from solution_task_827 import sum_column

def test_0():
    assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],0)==12

def test_1():
    assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],1)==15

def test_2():
    assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],3)==9

