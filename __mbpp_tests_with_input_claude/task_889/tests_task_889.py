from solution_task_889 import reverse_list_lists

def test_0():
    assert reverse_list_lists([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])==[[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]

def test_1():
    assert reverse_list_lists([[1,2],[2,3],[3,4]])==[[2,1],[3,2],[4,3]]

def test_2():
    assert reverse_list_lists([[10,20],[30,40]])==[[20,10],[40,30]]

