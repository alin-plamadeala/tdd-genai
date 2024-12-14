from solution_task_879 import text_match

def test_0():
    assert text_match("aabbbbd") == 'Not matched!'

def test_1():
    assert text_match("aabAbbbc") == 'Not matched!'

def test_2():
    assert text_match("accddbbjjjb") == 'Found a match!'

