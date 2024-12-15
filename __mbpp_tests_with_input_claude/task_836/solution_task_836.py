def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    curr_sum = 0
    start = 0
    end = 0
    temp_start = 0
    max_length = 0
    
    for i in range(n):
        curr_sum += arr[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
            max_length = end - start + 1
            
        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1
            
    return max_length