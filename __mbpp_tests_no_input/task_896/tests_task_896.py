from solution_task_896 import sort_list_last

def test_0():
    assert sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])==[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 

def test_1():
    assert sort_list_last([(9,8), (4, 7), (3,5), (7,9), (1,2)])==[(1,2), (3,5), (4,7), (9,8), (7,9)] 

def test_2():
    assert sort_list_last([(20,50), (10,20), (40,40)])==[(10,20),(40,40),(20,50)] 

