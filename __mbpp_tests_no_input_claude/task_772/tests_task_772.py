from solution_task_772 import remove_length

def test_0():
    assert remove_length('The person is most value tet', 3) == 'person is most value'

def test_1():
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'

def test_2():
    assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'

