def min_sum_path(triangle):
    if not triangle:
        return 0

    # Start from the second to last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current cell with the sum of the current value and the minimum of the two adjacent cells in the row below
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top element will contain the minimum path sum
    return triangle[0][0]
