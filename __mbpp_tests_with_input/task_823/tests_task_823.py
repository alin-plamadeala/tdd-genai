from solution_task_823 import check_substring

def test_0():
    assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'

def test_1():
    assert check_substring("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'

def test_2():
    assert check_substring("Its been a long day", "been") == 'string doesnt start with the given substring'

