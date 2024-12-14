from solution_task_700 import count_range_in_list

def test_0():
    assert count_range_in_list([10,20,30,40,40,40,70,80,99],40,100)==6

def test_1():
    assert count_range_in_list(['a','b','c','d','e','f'],'a','e')==5

def test_2():
    assert count_range_in_list([7,8,9,15,17,19,45],15,20)==3

