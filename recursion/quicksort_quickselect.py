


def product_of_three(arr: list) -> int:
    sorted_arr = sorted(arr)
    return sum(sorted_arr[-3:])






test_arr = [ 8, 3, 4, 10, 4, 10, 3, 10]

print(product_of_three(test_arr))
print(test_arr)
