from solution_task_676 import remove_extra_char

def test_0():
    assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'

def test_1():
    assert remove_extra_char('****//Google Flutter//*** - 36. ') == 'GoogleFlutter36'

def test_2():
    assert remove_extra_char('**//Google Firebase// - 478. ') == 'GoogleFirebase478'

