from solution_task_973 import left_rotate

def test_0():
    assert left_rotate("python",2) == "thonpy"   

def test_1():
    assert left_rotate("bigdata",3 ) == "databig" 

def test_2():
    assert left_rotate("hadoop",1 ) == "adooph" 

