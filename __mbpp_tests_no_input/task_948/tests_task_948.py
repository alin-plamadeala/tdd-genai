from solution_task_948 import get_item

def test_0():
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==('e')

def test_1():
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-4)==('u')

def test_2():
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-3)==('r')

