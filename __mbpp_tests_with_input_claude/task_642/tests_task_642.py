from solution_task_642 import remove_similar_row

def test_0():
    assert remove_similar_row([[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]] ) == {((2, 2), (4, 6)), ((3, 2), (4, 5))}

def test_1():
    assert remove_similar_row([[(5, 6), (4, 3)], [(3, 3), (5, 7)], [(4, 3), (5, 6)]] ) == {((4, 3), (5, 6)), ((3, 3), (5, 7))}

def test_2():
    assert remove_similar_row([[(6, 7), (5, 4)], [(4, 4), (6, 8)], [(5, 4), (6, 7)]] ) =={((4, 4), (6, 8)), ((5, 4), (6, 7))}

