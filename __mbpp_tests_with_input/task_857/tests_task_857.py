from solution_task_857 import listify_list

def test_0():
    assert listify_list(['Red', 'Blue', 'Black', 'White', 'Pink'])==[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

def test_1():
    assert listify_list(['python'])==[['p', 'y', 't', 'h', 'o', 'n']]

def test_2():
    assert listify_list([' red ', 'green',' black', 'blue ',' orange', 'brown'])==[[' ', 'r', 'e', 'd', ' '], ['g', 'r', 'e', 'e', 'n'], [' ', 'b', 'l', 'a', 'c', 'k'], ['b', 'l', 'u', 'e', ' '], [' ', 'o', 'r', 'a', 'n', 'g', 'e'], ['b', 'r', 'o', 'w', 'n']]

