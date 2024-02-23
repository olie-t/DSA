

def char_count(string_array: list):

    count = 0
    if len(string_array) == 0:
        return count
    for char in string_array[0]:
        count += 1
    return count + char_count(string_array[1:])

string_array = ["afger", "asdgkkg", "batman"]

print(char_count(string_array))

def even_nums(num_array: list):
    even_num = []
    if len(num_array) == 0:
        return even_num
    if num_array[0] % 2 == 0:
        even_num.append(num_array[0])
        return even_num + even_nums(num_array[1:])
    else:
        return even_nums(num_array[1:])

test_nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(even_nums(test_nums))

def triangle_numbers(num: int):
    if num == 1:
        return 1
    return triangle_numbers(num - 1) + num

print(triangle_numbers(8))

def letter_find(string: str):
    idx = 0
    if string[0] == 'x':
        return idx
    else:
        idx += 1
    return letter_find(string[1:]) + idx

print(letter_find("abctrfht"))