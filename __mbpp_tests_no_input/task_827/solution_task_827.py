from typing import List

def sum_column(matrix: List[List[int]], column_index: int) -> int:
    return sum(row[column_index] for row in matrix)