class Convert:
    def __call__(self, input_string):
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string")
        return input_string.split()

Convert = Convert()
