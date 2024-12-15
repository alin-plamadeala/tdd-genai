def find_Min_Swaps(arr, n):
    # Count the total number of 1s in the array
    ones_count = sum(arr)
    
    # If there are no 1s or all elements are 1s, no swaps are needed
    if ones_count == 0 or ones_count == n:
        return 0

    # Extend the array to handle circular cases
    arr_extended = arr + arr

    # Initialize variables for sliding window
    max_ones_in_window = 0
    current_ones = 0
    window_size = ones_count

    # Calculate the number of 1s in the first window
    for i in range(window_size):
        current_ones += arr_extended[i]

    max_ones_in_window = current_ones

    # Slide the window across the extended array
    for i in range(window_size, len(arr_extended)):
        current_ones += arr_extended[i] - arr_extended[i - window_size]
        max_ones_in_window = max(max_ones_in_window, current_ones)

    # The minimum swaps required is the difference between the total 1s
    # and the maximum number of 1s in any window of size `ones_count`
    return ones_count - max_ones_in_window
