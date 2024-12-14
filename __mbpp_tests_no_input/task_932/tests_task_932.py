from solution_task_932 import remove_duplic_list

def test_0():
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises"])==['Python', 'Exercises', 'Practice', 'Solution']

def test_1():
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","Java"])==['Python', 'Exercises', 'Practice', 'Solution', 'Java']

def test_2():
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","C++","C","C++"])==['Python', 'Exercises', 'Practice', 'Solution','C++','C']

