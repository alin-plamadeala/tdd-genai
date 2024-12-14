from solution_task_647 import split_upperstring

def test_0():
    assert split_upperstring("PythonProgramLanguage")==['Python','Program','Language']

def test_1():
    assert split_upperstring("PythonProgram")==['Python','Program']

def test_2():
    assert split_upperstring("ProgrammingLanguage")==['Programming','Language']

