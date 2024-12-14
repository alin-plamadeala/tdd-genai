from solution_task_631 import replace_spaces

def test_0():
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'

def test_1():
    assert replace_spaces('The Avengers') == 'The_Avengers'

def test_2():
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

