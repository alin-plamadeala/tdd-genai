from solution_task_693 import remove_multiple_spaces

def test_0():
    assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'

def test_1():
    assert remove_multiple_spaces('Quad      Core') == 'Quad Core'

def test_2():
    assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'

