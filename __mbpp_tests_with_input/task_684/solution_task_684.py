def count_Char(s: str, char: str, n: int) -> int:
    length_of_s = len(s)
    char_count_in_s = s.count(char)
    full_repetitions = n // length_of_s
    remaining_characters = n % length_of_s
    total_count = (char_count_in_s * full_repetitions) + s[:remaining_characters].count(char)
    return total_count
