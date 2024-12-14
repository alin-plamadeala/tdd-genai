class Sum:
    @staticmethod
    def digit_sum(n):
        return sum(int(digit) for digit in str(n))

    def __new__(cls, number):
        return cls.digit_sum(number)