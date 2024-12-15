def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    curr_sum = 0
    count = 0
    max_count = 0
    
    for i in range(n):
        if curr_sum <= 0:
            curr_sum = arr[i]
            count = 1
        else:
            curr_sum += arr[i]
            count += 1
            
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_count = count
            
    return max_count