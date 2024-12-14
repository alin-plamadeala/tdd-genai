def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    max_length = 0
    current_length = 0
    
    for i in range(n):
        current_sum += arr[i]
        current_length += 1
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_length = current_length
        
        if current_sum < 0:
            current_sum = 0
            current_length = 0
    
    return max_length