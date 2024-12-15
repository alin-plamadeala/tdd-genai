def max_sub_array_sum(arr, n):
    max_sum = arr[0]  # Initialize max_sum to the first element
    current_sum = arr[0]  # Initialize current_sum to the first element

    # Iterate through the array starting from the second element
    for i in range(1, n):
        current_sum += arr[i]  # Add the current element to current_sum

        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
