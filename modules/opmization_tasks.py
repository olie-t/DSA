basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
]


def plays_both(fst_lst: list, scnd_lst: list) -> list:
    fst_map = {}
    plays_both = []
    for i in range(0, len(fst_lst)):
        fst_map[fst_lst[i]["first_name"] + " " + fst_lst[i]["last_name"]] = True

    for j in range(0, len(scnd_lst)):
        if scnd_lst[j]["first_name"] + " " + scnd_lst[j]["last_name"] in fst_map:
            plays_both.append(
                scnd_lst[j]["first_name"] + " " + scnd_lst[j]["last_name"]
            )

    return plays_both


def find_missing_int(nums: list) -> int:
    # given a list of ints, find the one that is missing
    sorted_nums = sorted(nums)
    for i in range(0, len(sorted_nums) - 1):
        if sorted_nums[i + 1] - sorted_nums[i] > 1:
            return sorted_nums[i] + 1
    return "list complete"


numbers = [1, 5, 4, 2, 6, 10, 9, 8, 7]


def stock_trader(nums: list) -> int:
    # from a list of stock prices find the greatest profit that can be made from a single buy and sell
    current_low = float("inf")
    profit = 0
    for i in nums:
        if i < current_low:
            current_low = i
        if i - current_low > profit:
            profit = i - current_low
    return profit


prices = [10, 7, 5, 8, 11, 2, 6]


def highest_product(nums: list) -> int:
    # find the highest product from a list of ints
    lowest = 0
    second_lowest = 0
    highest = 0
    second_highest = 0
    for i in nums:
        if i < lowest:
            second_lowest = lowest
            lowest = i
        elif i < second_lowest:
            second_lowest = i
        elif i > highest:
            second_highest = highest
            highest = i
        elif i > second_highest:
            second_highest = i
    if highest * second_highest > lowest * second_lowest:
        return highest * second_highest
    return lowest * second_lowest


ints = [5, -10, -6, 9, 4]
more_ints = [3, 6, 10, -7, 12, -3]


def int_in_sequence(nums: list) -> int:
    # return the length of the longest sequence of ints
    nums_hash = {}
    longest_sequence = 0
    for num in nums:
        if num not in nums_hash:
            nums_hash[num] = True
    for num in nums_hash.keys():
        if num - 1 not in nums_hash:
            current_num = num
            current_sequence = 1

            while current_num + 1 in nums_hash:
                current_num += 1
                current_sequence += 1
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence


test_seq = [10, 5, 12, 3, 55, 30, 4, 11, 2]
test_seq2 = [19, 13, 15, 12, 18, 14, 17, 11]


def sort_temperatures(temps: list[float]) -> list[float]:
    temps_hash = {}
    for temp in temps:
        if temp not in temps_hash:
            temps_hash[temp] = 1
        else:
            temps_hash[temp] += 1
    sorted_array = []
    for temperature in range(970, 991):
        temp_float = temperature / 10.0
        if temp_float in temps_hash:
            sorted_array.extend([temp_float] * temps_hash[temp_float])
    return sorted_array


temps = [
    97.0,
    97.1,
    98.6,
    98.1,
    97.3,
    99.0,
    98.5,
    98.5,
    97.1,
    97.5,
    97.4,
    98.3,
    98.3,
    97.1,
    98.9,
]


if __name__ == "__main__":
    print(plays_both(basketball_players, football_players))
    print(find_missing_int(numbers))
    print(stock_trader(prices))
    print(highest_product(ints))
    print(highest_product(more_ints))
    print(int_in_sequence(test_seq))
    print(int_in_sequence(test_seq2))
    print(sort_temperatures(temps))
