def check_Concat(full_string, sub_string):
    if not full_string or not sub_string:
        return False
    if len(full_string) % len(sub_string) != 0:
        return False
    repeat_count = len(full_string) // len(sub_string)
    return sub_string * repeat_count == full_string
