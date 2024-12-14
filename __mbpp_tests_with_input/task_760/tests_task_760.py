from solution_task_760 import unique_Element

def test_0():
    assert unique_Element([1,1,1],3) == 'YES'

def test_1():
    assert unique_Element([1,2,1,2],4) == 'NO'

def test_2():
    assert unique_Element([1,2,3,4,5],5) == 'NO'

