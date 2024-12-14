from solution_task_674 import remove_duplicate

def test_0():
    assert remove_duplicate("Python Exercises Practice Solution Exercises")==("Python Exercises Practice Solution")

def test_1():
    assert remove_duplicate("Python Exercises Practice Solution Python")==("Python Exercises Practice Solution")

def test_2():
    assert remove_duplicate("Python Exercises Practice Solution Practice")==("Python Exercises Practice Solution")

