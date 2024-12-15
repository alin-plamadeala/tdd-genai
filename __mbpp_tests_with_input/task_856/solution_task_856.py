def find_Min_Swaps(arr, n):
    # Count the total number of 1's in the array
    ones_count = sum(arr)
    
    # If there are no 1's or all elements are 1's, no swaps are needed
    if ones_count == 0 or ones_count == n:
        return 0

    # Create an extended array to handle circular cases
    extended_arr = arr + arr

    # Initialize the number of zeros in the first window of size ones_count
    current_window_zeros = sum(1 for i in range(ones_count) if extended_arr[i] == 0)
    min_swaps = current_window_zeros

    # Slide the window across the extended array
    for i in range(1, n + 1):  # Slide within the range of the original array
        # Add the new element to the window
        if extended_arr[i + ones_count - 1] == 0:
            current_window_zeros += 1
        # Remove the element that is sliding out of the window
        if extended_arr[i - 1] == 0:
            current_window_zeros -= 1
        # Update the minimum swaps
        min_swaps = min(min_swaps, current_window_zeros)

    return min_swaps
