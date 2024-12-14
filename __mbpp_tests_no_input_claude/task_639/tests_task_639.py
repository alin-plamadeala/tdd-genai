from solution_task_639 import sample_nam

def test_0():
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16

def test_1():
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10

def test_2():
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6

