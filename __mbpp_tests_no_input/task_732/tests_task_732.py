from solution_task_732 import replace_specialchar

def test_0():
    assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')

def test_1():
    assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')

def test_2():
    assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')

