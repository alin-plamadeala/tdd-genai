def chinese_zodiac(year):
    zodiacs = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 
        'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'
    ]
    return zodiacs[(year - 1900) % 12]
