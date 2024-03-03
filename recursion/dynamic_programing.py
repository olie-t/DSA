def max_array(array: list):
    #Big o testing, first version
    print("RECURSION")
    if len(array) == 1:
        return array[0]
    if array[0] > max_array(array[1:]):
        return array[0]
    else:
        return max_array(array[1:])

def better_max_array(array: list):
    print("RECURSION")
    if len(array) == 1:
        return array[0]
    max_remainder = better_max_array(array[1:])
    if array[0] > max_remainder:
        return array[0]
    else:
        return max_remainder

test_array = [ 1, 2, 3, 4]

print(max_array(test_array))
print(better_max_array(test_array))

#implementing memoization

def fib(n: int, memo: dict = {}) -> int:
    if n == 0 or n == 1:
        return n
    if not memo.get(n):
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]

print(fib(7))


def add_till_100(array: list) -> int:
    if len(array) == 0:
        return 0
    array_remainder = add_till_100(array[1:])
    if array[0] + array_remainder > 100:
        return array_remainder
    else:
        return array[0] + array_remainder


def golomb(n: int, memo: dict = {}) -> int:
    if n == 1:
        return 1
    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]


def unique_paths(rows: int, cols: int, memo: dict == {}) -> int:
    if rows == 1 or cols == 1:
        return 1
   # Use tuples of rows cols as the key for the hasmap ( dict)
    if not memo.get((rows, cols)):
        memo[(rows, cols)] = unique_paths(rows - 1, cols, memo) + unique_paths(rows, cols - 1, memo)
    return memo[(rows, cols)]

