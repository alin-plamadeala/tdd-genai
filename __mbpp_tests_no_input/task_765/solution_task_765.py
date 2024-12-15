def is_polite(n):
    def find_next_polite_number(start):
        current = start + 1
        while True:
            if is_polite_number(current):
                return current
            current += 1

    def is_polite_number(num):
        count = 0
        for i in range(1, num):
            total = 0
            for j in range(i, num):
                total += j
                if total == num:
                    count += 1
                    break
                elif total > num:
                    break
        return count > 0

    polite_count = 0
    current_number = 0
    while polite_count < n:
        current_number = find_next_polite_number(current_number)
        polite_count += 1

    return current_number
