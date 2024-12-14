def find_Min_Swaps(arr, n):
    count_ones = arr.count(1)
    max_ones_in_window = 0
    current_ones_in_window = 0
    
    for i in range(count_ones):
        if arr[i] == 1:
            current_ones_in_window += 1
    
    max_ones_in_window = current_ones_in_window
    
    for i in range(count_ones, n):
        if arr[i] == 1:
            current_ones_in_window += 1
        if arr[i - count_ones] == 1:
            current_ones_in_window -= 1
        
        max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
    
    return count_ones - max_ones_in_window