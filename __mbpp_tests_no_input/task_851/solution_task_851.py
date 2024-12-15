def Sum_of_Inverse_Divisors(start, end):
    def inverse_divisors_sum(num):
        # Calculate the sum of the inverses of the divisors of `num`
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return sum(1 / d for d in divisors)

    count = 0
    for n in range(start, end + 1):
        if inverse_divisors_sum(n).is_integer():
            count += 1
    return count
