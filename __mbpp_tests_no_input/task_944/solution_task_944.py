import re

def num_position(s):
    # Find all numbers in the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    
    # Find the largest number
    largest_number = max(numbers)
    
    # Calculate the sum of the positions of the digits in the largest number
    return sum(int(digit) for digit in str(largest_number))
