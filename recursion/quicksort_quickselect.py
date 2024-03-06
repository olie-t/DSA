
def product_of_three(arr: list[int]) -> int:
    sorted_arr = sorted(arr)
    return sorted_arr[-1] * sorted_arr[-2] * sorted_arr[-3]


def missing_number(arr: list[int]) -> int:
    sorted_arr = sorted(arr)
    for i in sorted_arr:
        if sorted_arr[i + 1] - sorted_arr[i] > 1:
            return sorted_arr[i] + 1
    return True


# 3 functions to find the greatest number in an array
def highest_number_square(arr: list[int]) -> int:
    for i in arr:
        is_greatest = True
        for j in arr:
            if i < j:
                is_greatest = False
        if is_greatest:
            return i


def highest_number_log(arr: list[int]) -> int:
    sorted_arr = sorted(arr)
    return sorted_arr[-1]


def highest_number_n(arr: list[int]) -> int:
    highest = arr[0]
    for i in arr:
        if i > highest:
            highest = i
    return highest


test_arr = [8, 3, 4, 10, 4, 10, 3, 10]
test_arr2 = [6, 8, 3, 4, 10, 1, 5, 7, 2]
print(product_of_three(test_arr))
print(missing_number(test_arr2))
print(highest_number_square(test_arr2))
print(highest_number_log(test_arr2))
print(highest_number_n(test_arr2))
