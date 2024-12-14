def check_Concat(string, substring):
    if len(string) % len(substring) != 0:
        return False
    return string == substring * (len(string) // len(substring))