from solution_task_812 import road_rd

def test_0():
    assert road_rd("ravipadu Road")==('ravipadu Rd.')

def test_1():
    assert road_rd("palnadu Road")==('palnadu Rd.')

def test_2():
    assert road_rd("eshwar enclave Road")==('eshwar enclave Rd.')

