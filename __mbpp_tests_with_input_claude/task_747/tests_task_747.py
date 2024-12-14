from solution_task_747 import lcs_of_three

def test_0():
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA', 6, 7, 5) == 2

def test_1():
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels', 5, 8, 13) == 5 

def test_2():
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea', 7, 6, 5) == 3

