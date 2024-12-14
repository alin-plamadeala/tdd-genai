from solution_task_794 import text_starta_endb

def test_0():
    assert text_starta_endb("aabbbb")==('Found a match!')

def test_1():
    assert text_starta_endb("aabAbbbc")==('Not matched!')

def test_2():
    assert text_starta_endb("accddbbjjj")==('Not matched!')

