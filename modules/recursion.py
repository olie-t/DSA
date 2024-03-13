

def char_count(string_array: list):
    #count the number of characters in an array of strings
    if len(string_array) == 0:
        return 0
    return len(string_array[0]) + char_count(string_array[1:])

string_array = ["afger", "asdgkkg", "batman"]

print(char_count(string_array))

def even_nums(num_array: list):
    #return an array of even numbers from an array of numbers
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

def letter_find(string: str, letter: str) -> int:
    #find the index of a given letter within a string
    if string[0] == letter:
        return 0
    return letter_find(string[1:]) + 1

print(letter_find("abctrfxht"))

def find_routes(x: int, y: int) -> int:
    #find the amount of shortest routes over a grid described by x * y
    if x == 1 or y == 1:
        return 1
    return find_routes(x - 1, y) + find_routes(x, y - 1)

print(find_routes(5,3))
