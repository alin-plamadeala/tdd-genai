from solution_task_860 import check_alphanumeric

def test_0():
    assert check_alphanumeric("dawood@") == 'Discard'

def test_1():
    assert check_alphanumeric("skdmsam326") == 'Accept'

def test_2():
    assert check_alphanumeric("cooltricks@") == 'Discard'

