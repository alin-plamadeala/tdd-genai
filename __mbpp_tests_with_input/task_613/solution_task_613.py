# solution_task_613.py
def maximum_value(record_list):
    return [(key, max(values)) for key, values in record_list]
