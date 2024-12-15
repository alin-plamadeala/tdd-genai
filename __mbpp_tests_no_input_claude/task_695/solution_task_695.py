def check_greater(tuple1, tuple2):
    count = 0
    for i in range(len(tuple1)):
        if tuple1[i] < tuple2[i]:
            count += 1
    return count == len(tuple1)