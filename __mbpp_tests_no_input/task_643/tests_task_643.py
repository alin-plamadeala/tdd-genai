from solution_task_643 import text_match_wordz_middle

def test_0():
    assert text_match_wordz_middle("pythonzabc.")==('Found a match!')

def test_1():
    assert text_match_wordz_middle("xyzabc.")==('Found a match!')

def test_2():
    assert text_match_wordz_middle("  lang  .")==('Not matched!')

