class Average:
    def __new__(cls, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)