from solution_task_966 import remove_empty

def test_0():
    assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  

def test_1():
    assert remove_empty([(), (), ('',), ("python"), ("program")])==[('',), ("python"), ("program")]  

def test_2():
    assert remove_empty([(), (), ('',), ("java")])==[('',),("java") ]  

