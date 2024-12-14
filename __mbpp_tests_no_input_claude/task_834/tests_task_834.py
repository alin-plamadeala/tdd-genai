from solution_task_834 import generate_matrix

def test_0():
    assert generate_matrix(3)==[[1, 2, 3], [8, 9, 4], [7, 6, 5]] 

def test_1():
    assert generate_matrix(2)==[[1,2],[4,3]]

def test_2():
    assert generate_matrix(7)==[[1, 2, 3, 4, 5, 6, 7], [24, 25, 26, 27, 28, 29, 8], [23, 40, 41, 42, 43, 30, 9], [22, 39, 48, 49, 44, 31, 10], [21, 38, 47, 46, 45, 32, 11], [20, 37, 36, 35, 34, 33, 12], [19, 18, 17, 16, 15, 14, 13]]

