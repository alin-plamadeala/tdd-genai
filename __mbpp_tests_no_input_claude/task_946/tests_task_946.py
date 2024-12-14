from solution_task_946 import most_common_elem

def test_0():
    assert most_common_elem('lkseropewdssafsdfafkpwe',3)==[('s', 4), ('e', 3), ('f', 3)] 

def test_1():
    assert most_common_elem('lkseropewdssafsdfafkpwe',2)==[('s', 4), ('e', 3)]

def test_2():
    assert most_common_elem('lkseropewdssafsdfafkpwe',7)==[('s', 4), ('e', 3), ('f', 3), ('k', 2), ('p', 2), ('w', 2), ('d', 2)]

