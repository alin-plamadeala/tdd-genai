from solution_task_607 import find_literals

def test_0():
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)

def test_1():
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)

def test_2():
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)

