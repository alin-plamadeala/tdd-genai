from solution_task_862 import n_common_words

def test_0():
    assert n_common_words("python is a programming language",1)==[('python', 1)]

def test_1():
    assert n_common_words("python is a programming language",1)==[('python', 1)]

def test_2():
    assert n_common_words("python is a programming language",5)==[('python', 1),('is', 1), ('a', 1), ('programming', 1), ('language', 1)]

