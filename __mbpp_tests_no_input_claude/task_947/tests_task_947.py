from solution_task_947 import len_log

def test_0():
    assert len_log(["win","lose","great"]) == 3

def test_1():
    assert len_log(["a","ab","abc"]) == 1

def test_2():
    assert len_log(["12","12","1234"]) == 2

