from solution_task_965 import camel_to_snake

def test_0():
    assert camel_to_snake('PythonProgram')==('python_program')

def test_1():
    assert camel_to_snake('pythonLanguage')==('python_language')

def test_2():
    assert camel_to_snake('ProgrammingLanguage')==('programming_language')

