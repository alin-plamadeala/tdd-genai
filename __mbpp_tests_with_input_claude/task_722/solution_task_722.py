def filter_data(students, height, weight):
    return {name: values for name, values in students.items() if values[0] >= height and values[1] >= weight}