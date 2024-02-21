
def char_counter(string_array: list):
    char_count = 0
    if len(string_array) == 0:
        return char_count

    char_counter(string_array - string_array[0])

    for idx_str in string_array:
        char_count += 1
