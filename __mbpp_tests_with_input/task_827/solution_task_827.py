def sum_column(matrix, column_index):
    return sum(row[column_index] for row in matrix if column_index < len(row))
